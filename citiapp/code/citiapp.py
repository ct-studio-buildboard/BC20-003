from flask import Flask, redirect, url_for, render_template, url_for, request, session, flash
import sqlite3
import json
from collections import defaultdict
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from werkzeug.utils import secure_filename
from data_uploader import upload_data
import os
import utils

app = Flask(__name__)
app.secret_key = '1jfEi4fjJ@3iFso9'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/write_data/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))

    result_message = upload_data(f.filename)
    flash(result_message)
    os.remove(f.filename)

    return redirect('/')

@app.route('/report-investor/', defaults={'acct': 9601})
@app.route('/report-investor/<acct>')
def report_investor(acct):

    conn = sqlite3.connect("citi.db")
    query = """SELECT * from interactions_roadshow
                where acct = {}
                order by 'date' """.format(acct)
    df = pd.read_sql_query(query, conn)
    conn.close()

    print(df.columns)
    print(df.head())

    stats = {}
    stats['unique_corporates'] = df.corporate_id.nunique()
    stats['unique_industries'] = df.company_industry.nunique()
    stats['mgmt'] = str(round(100 * df.management_flag.mean(), 1)) + '%'

    #getting interactions by year
    temp_df = df.groupby('year')['date'].count().reset_index().rename(columns={'date':'ct'})
    int_year = []
    for i, r in temp_df.iterrows():
        int_year.append({'year':r['year'], 'value':r['ct']})

    #getting interactions by type
    temp_df = df['meeting_type'].value_counts().to_frame().reset_index()
    temp_df.columns = ['meeting_type', 'ct']
    if (temp_df['ct'] < 0.05*df.shape[0]).sum() > 1:
        temp_df.loc[temp_df['ct'] < 0.05*df.shape[0], 'meeting_type'] = 'Other'
    temp_df = temp_df.groupby('meeting_type')['ct'].sum().reset_index().sort_values('ct', ascending=False)
    pcts = list((temp_df['ct']/df.shape[0]).round(2))
    int_type_positions = utils.get_donut_lines(pcts)
    int_type = {}
    for i, r in temp_df.iterrows():
        int_type[r['meeting_type']] = round(100 * r['ct'] / df.shape[0], 1)

    #getting interactions by market cap
    temp_df = df['market_bucket'].value_counts().to_frame().reset_index()
    temp_df.columns = ['market_bucket', 'ct']
    if (temp_df['ct'] < 0.05*df.shape[0]).sum() > 1:
        temp_df.loc[temp_df['ct'] < 0.05*df.shape[0], 'market_bucket'] = 'Other'
    temp_df = temp_df.groupby('market_bucket')['ct'].sum().reset_index().sort_values('ct', ascending=False)
    pcts = list((temp_df['ct']/df.shape[0]).round(2))
    int_bucket_positions = utils.get_donut_lines(pcts)
    int_bucket = {}
    for i, r in temp_df.iterrows():
        dict_key = r['market_bucket']
        if dict_key == 'Private/unknown':
            dict_key = 'NA'
        int_bucket[dict_key] = round(100 * r['ct'] / df.shape[0], 1)

    #getting interactions by company region
    temp_df = df['company_region'].value_counts().to_frame().reset_index()
    temp_df.columns = ['company_region', 'ct']
    if (temp_df['ct'] < 0.05*df.shape[0]).sum() > 1:
        temp_df.loc[temp_df['ct'] < 0.05*df.shape[0], 'company_region'] = 'Other'
    temp_df = temp_df.groupby('company_region')['ct'].sum().reset_index().sort_values('ct', ascending=False)

    pcts = list((temp_df['ct']/df.shape[0]).round(2))
    int_region_positions = utils.get_donut_lines(pcts)
    int_region = {}
    for i, r in temp_df.iterrows():
        int_region[r['company_region']] = round(100 * r['ct'] / df.shape[0], 1)


    return render_template('report_investor.html',
                            stats=stats,
                            int_year=int_year,
                            int_type=int_type,
                            int_type_positions=int_type_positions,
                            int_bucket=int_bucket,
                            int_bucket_positions=int_bucket_positions,
                            int_region=int_region,
                            int_region_positions=int_region_positions)

@app.route('/investors/', defaults={'acct': None})
@app.route('/investors/<acct>')
def investors(acct):

    if acct == None:
        conn = sqlite3.connect("citi.db")
        query = """SELECT * from roadshow_investor
                    order by total_interactions desc limit 1000"""
        investors = pd.read_sql_query(query, conn)
        conn.close()

        top_investors = investors.groupby('acct')['total_interactions'].sum().reset_index()\
                                    .sort_values('total_interactions', ascending=False)\
                                    .reset_index(drop=True)
        top_investors['total_interactions'] = top_investors['total_interactions'].astype(int)
        top_investors = top_investors.head(10).values.tolist()

        cols_to_show = ['acct', 'investor_region', 'year', 'global_access', 'total_interactions',
                        'unique_corporates', 'unique_industries', 'one_on_one_pct',
                        'management_pct', 'vid_call_pct']
        investors = investors[cols_to_show]

        pct_cols = ('one_on_one_pct', 'management_pct', 'vid_call_pct')
        for colname in pct_cols:
            investors[colname] = (investors[colname]*100).round(1)

        html_colnames = ['Acct', 'Region', 'Year', 'Global Access Tier', 'Total Interactions',
                            'Unique Corporates', 'Unique Industries',
                             '1:1 %', 'Mgmt %', 'Video Call %']

        select_values = {}
        select_values['years'] = sorted(list(set(investors['year'])), reverse=True)
        select_values['regions'] = sorted(list(set(investors['investor_region'])))
        select_values['tiers'] = sorted(list(set(investors['global_access'])))

        return render_template('investors.html',
                                data = investors.values.tolist(),
                                colnames = cols_to_show,
                                html_colnames = html_colnames,
                                top_investors = top_investors,
                                select_values = select_values)

    else:
        conn = sqlite3.connect("citi.db")
        query = """SELECT * from interactions_roadshow
                    where acct == {}
                    order by 'date' """.format(acct)
        df = pd.read_sql_query(query, conn)
        conn.close()

        df['management_presence'] = np.where(df['management_flag'] == 1, 'Yes', 'No')
        df['video_flag'] = np.where(df['medium'] == 'Video Conference', 'Yes', 'No')
        df = df.sort_values('date', ascending=False).reset_index(drop=True)

        year_set = sorted(list(set(df['year'])), reverse = True)

        investor_info = {}
        investor_info['acct'] = acct


        html_colnames = {'acct':'Account ID', 'sgp':'SGP', 'investor_region':'Investor Region',
                        'equity_tier': 'Equity Tier', 'global_access': 'Global Access',
                        'company_name': 'Corporate Name', 'ric':'RIC',
                        'company_industry':'Industry', 'product_region':'Product Region',
                        'company_region': 'Corporate Region', 'company_country':'Corporate Country',
                        'market_cap':'Market Cap', 'market_bucket':'Market Bucket',
                        'ratings':'Ratings', 'date': 'Date', 'event_type':'Event Type',
                        'meeting_type':'Meeting Type', 'global_region_visited':'Region Visited',
                        'city':'City', 'management_presence':'Management Present',
                        'video_flag': 'Video'}

        return render_template('view_investor.html',
                                year_set = year_set,
                                investor_info = investor_info,
                                data = json.dumps(df.values.tolist()),
                                colnames = list(df.columns),
                                html_colnames = html_colnames)


@app.route('/investors/<acct>/similar_investors.html')
def similar_investors(acct):
    conn = sqlite3.connect("citi.db")
    query = """SELECT * from roadshow_investor"""
    investors = pd.read_sql_query(query, conn)
    conn.close()

    investors.fillna(0, inplace=True)

    correlation_columns = ['total_interactions', 'unique_corporates', 'unique_industries', 'one_on_one_pct',
                  'group_pct', 'management_pct', 'market_cap_mean', 'market_cap_median', 'large_pct',
                  'private_pct', 'us_pct', 'meeting_pct', 'conf_call_pct', 'vid_call_pct', 'open_ex_pct']
    knn_investor = NearestNeighbors(n_neighbors=3).fit(investors.loc[:, correlation_columns])
    neighbors = knn_investor.kneighbors(return_distance=False)

    acct_index = investors.index[investors['acct'] == acct]
    acct_neighbors = [investors.iloc[n]['acct'] for n in neighbors[acct_index][0]]

    year_set = sorted(list(set(investors['year'])), reverse = True)

    investor_info = {}
    investor_info['acct'] = acct
    investor_info['neighbors'] = acct_neighbors

    return render_template('similar_investors.html',
                            year_set = year_set,
                            investor_info = investor_info,
                            data = json.dumps(investors.values.tolist()),
                            colnames = list(investors.columns))


@app.route('/search')
def search():
    search_term = request.args.get('search')
    c_columns = []
    i_columns = []
    text = "No results found."

    if search_term.strip()=='' or search_term == None:
        return render_template('search.html',
                                searched = text,
                                results = 0,
                                c_results = [],
                                i_results = [],
                                c_columns = c_columns,
                                i_columns = i_columns)

    else:
        conn = sqlite3.connect("citi.db")
        query = """SELECT * FROM corporates
                    WHERE company_name LIKE '%"""+search_term+"""%'
                    ORDER BY company_name limit 100"""
        corporates = pd.read_sql_query(query, conn)

        query = """SELECT distinct acct, account_name, investor_region, global_access FROM roadshow_investor
                    WHERE account_name LIKE '%"""+search_term+"""%'
                    ORDER BY account_name limit 100"""
        investors = pd.read_sql_query(query, conn)
        conn.close()

        grp = ['acct','account_name']
        # i_results = investors.groupby(grp, as_index=False)['investor_region'].apply(', '.join).reset_index()
        aggregation_functions = {'global_access': 'first', 'investor_region': 'last'}
        i_results = investors.groupby(grp, as_index=False).aggregate(aggregation_functions).reindex(columns=investors.columns)

        if len(corporates)+len(i_results)>0:
            text = "Results for: \""+search_term+"\""

        if len(corporates)>0:
            c_columns = ['Name', 'Company Region', 'Company Country', 'Company Industry']
        if len(i_results)>0:
            i_columns = ['Acct.', 'Account Name', 'Region(s)', 'Global Access Tier']

        return render_template('search.html',
                                searched = text,
                                results = len(corporates)+len(i_results),
                                c_results = corporates.values.tolist(),
                                i_results = i_results.values.tolist(),
                                c_columns = c_columns,
                                i_columns = i_columns)

@app.route('/corporates/', defaults={'corporate_id': None})
@app.route('/corporates/<corporate_id>')
def corporates(corporate_id):

    if corporate_id == None:

        conn = sqlite3.connect("citi.db")
        query = """SELECT * from roadshow_company
                    order by total_interactions desc limit 1000"""
        corporates = pd.read_sql_query(query, conn)
        conn.close()

        top_corporates = corporates.groupby('company_name')['total_interactions'].sum().reset_index()\
                                    .sort_values('total_interactions', ascending=False)\
                                    .reset_index(drop=True)
        top_corporates['total_interactions'] = top_corporates['total_interactions'].astype(int)
        top_corporates = top_corporates.head(10).values.tolist()

        corporates['company_type'] = np.where(corporates['private_flag'] == 0, 'Public', 'Private')
        cols_to_show = ['corporate_id', 'company_name', 'company_region', 'company_type', 'year', 'total_interactions',
                        'unique_investors', 'one_on_one_pct', 'management_pct', 'vid_call_pct']
        corporates = corporates[cols_to_show]

        pct_cols = ('one_on_one_pct', 'management_pct', 'vid_call_pct')
        for colname in pct_cols:
            corporates[colname] = (corporates[colname]*100).round(1)

        html_colnames = ['Corporate', 'Region', 'Type', 'Year', 'Interactions',
                            'Unique Investors', '1:1 %', 'Mgmt %', 'Video Call %']

        select_values = {}
        select_values['years'] = sorted(list(set(corporates['year'])), reverse=True)
        select_values['regions'] = sorted(list(set(corporates['company_region'])))

        return render_template('corporates.html',
                                data = corporates.values.tolist(),
                                colnames = cols_to_show,
                                html_colnames = html_colnames,
                                top_corporates = top_corporates,
                                select_values = select_values)

    else:

        conn = sqlite3.connect("citi.db")
        query = """SELECT * FROM interactions_roadshow
                    WHERE corporate_id = {}
                    ORDER BY 'date' asc """.format(corporate_id)
        df = pd.read_sql_query(query, conn)
        conn.close()

        df['management_presence'] = np.where(df['management_flag'] == 1, 'Yes', 'No')
        df['video_flag'] = np.where(df['medium'] == 'Video Conference', 'Yes', 'No')

        #Readable Column Names
        html_colnames = {'acct':'Account ID', 'sgp':'SGP', 'investor_region':'Investor Region',
                        'equity_tier': 'Equity Tier', 'global_access': 'Global Access',
                        'company_name': 'Corporate Name', 'ric':'RIC',
                        'company_industry':'Industry', 'product_region':'Product Region',
                        'company_region': 'Corporate Region', 'company_country':'Corporate Country',
                        'market_cap':'Market Cap', 'market_bucket':'Market Bucket',
                        'ratings':'Ratings', 'date': 'Date', 'event_type':'Event Type',
                        'meeting_type':'Meeting Type', 'global_region_visited':'Region Visited',
                        'city':'City', 'management_presence':'Management Present',
                        'video_flag': 'Video'}



        year_set = sorted(list(set(df['year'])), reverse = True)

        corporate_info = {}
        corporate_info['region'] = df['company_region'][0]
        corporate_info['country'] = df['company_country'][0]
        corporate_info['company_name'] = df['company_name'][0]
        corporate_info['company_industry'] = df['company_industry'][0]
        corporate_info['corporate_id'] = corporate_id

        df = df.sort_values('date', ascending=False).reset_index(drop=True)

        #get investor-level summary
        df_investors = df.groupby(['acct', 'investor_region', 'global_access']).apply(
                        lambda x: pd.Series({'total_interactions': x.count(),
                                            'last_interaction': x['date'].max()})).reset_index()

        return render_template('view_corporate.html',
                                year_set = year_set,
                                corporate_info = corporate_info,
                                data = json.dumps(df.values.tolist()),
                                colnames = list(df.columns),
                                html_colnames = json.dumps(html_colnames),
                                df_investors = df_investors)

@app.route('/corporates/<corporate_id>/similar_corporates.html')
def similar_corporates(corporate_id):
    conn = sqlite3.connect("citi.db")
    query = """SELECT * from roadshow_company"""
    corporates = pd.read_sql_query(query, conn)
    conn.close()

    corporates.fillna(0, inplace=True)

    correlation_columns = ['corporate_id', 'company_name', 'total_interactions', 'unique_investors', 'one_on_one_pct',
                  'group_pct', 'management_pct', 'market_cap_avg', 'platinum_pct',
                  'meeting_pct', 'conf_call_pct', 'vid_call_pct', 'open_ex_pct']
    corporates_correlation = corporates.loc[:, correlation_columns]
    corporates_correlation_grouped = corporates_correlation.groupby(['company_name']).apply(lambda x: pd.Series({'total_interactions': x['total_interactions'].sum(),
                                                                'unique_investors': x['unique_investors'].mean(),
                                                                'one_on_one_pct': x['one_on_one_pct'].mean(),
                                                               'group_pct': x['group_pct'].mean(),
                                                               'management_pct': x['management_pct'].mean(),
                                                               'market_cap_avg': x['market_cap_avg'].mean(),
                                                               'platinum_pct': x['platinum_pct'].mean(),
                                                              'meeting_pct': x['meeting_pct'].mean(),
                                                              'conf_call_pct': x['conf_call_pct'].mean(),
                                                              'vid_call_pct': x['vid_call_pct'].mean(),
                                                             'open_ex_pct': x['open_ex_pct'].mean(),
                                                             'corporate_id': x['corporate_id'][0]
                                                                })).reset_index()

    correlation_columns = ['total_interactions', 'unique_investors', 'one_on_one_pct',
                  'group_pct', 'management_pct', 'market_cap_avg', 'platinum_pct',
                  'meeting_pct', 'conf_call_pct', 'vid_call_pct', 'open_ex_pct']
    knn_corporate = NearestNeighbors(n_neighbors=3).fit(corporates_correlation_grouped.loc[:, correlation_columns])
    neighbors = knn_corporate.kneighbors(return_distance=False)

    acct_index = corporates_correlation_grouped.index[corporates_correlation_grouped['corporate_id'] == float(corporate_id)]
    acct_neighbors = [int(corporates_correlation_grouped.iloc[n]['corporate_id']) for n in neighbors[acct_index][0]]
    acct_neighbors_names = [corporates_correlation_grouped.iloc[n]['company_name'] for n in neighbors[acct_index][0]]

    corporate_info = {}
    corporate_info['company_name'] = corporates_correlation_grouped.iloc[acct_index]['company_name'].to_string().split(' ', 1)[1]
    corporate_info['corporate_id'] = corporate_id
    corporate_info['neighbors'] = acct_neighbors
    corporate_info['neighbor_names'] = acct_neighbors_names

    return render_template('similar_corporates.html', corporate_info = corporate_info)



if __name__ == '__main__':
    app.run(debug = True)
