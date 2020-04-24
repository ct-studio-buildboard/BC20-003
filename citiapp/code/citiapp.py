from flask import Flask, redirect, url_for, render_template, url_for, request, session, flash
import sqlite3
import json
from collections import defaultdict
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from werkzeug import secure_filename
from data_uploader import upload_data
import os

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
                  'private_pct', 'us_pct']
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



if __name__ == '__main__':
    app.run(debug = True)
