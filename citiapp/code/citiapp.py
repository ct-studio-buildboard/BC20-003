from flask import Flask, redirect, url_for, render_template, url_for, request, session
import sqlite3
import json
from collections import defaultdict
import pandas as pd
import numpy as np
app = Flask(__name__)
app.secret_key = '1jfEi4fjJ@3iFso9'

@app.route('/')
def index():

    conn = sqlite3.connect("citi.db")
    query = "SELECT * from interactions_raw limit 20"
    interactions = pd.read_sql_query(query, conn)
    conn.close()

    return render_template('index.html')

@app.route('/investors/', defaults={'acct': None})
@app.route('/investors/<acct>')
def investors(acct):

    if acct == None:
        conn = sqlite3.connect("citi.db")
        query = "SELECT * from roadshow_investor limit 20"
        investors = pd.read_sql_query(query, conn)
        conn.close()

        cols_to_show = ['acct', 'investor_region', 'year', 'global_access', 
                        'total_interactions', 'unique_corporates', 'unique_industries']
        investors = investors[cols_to_show]

        return render_template('investors.html', 
                                data = investors.values.tolist(),
                                colnames = cols_to_show,
                                acct=None)

    else:
        conn = sqlite3.connect("citi.db")
        query = "SELECT * from interactions_raw where acct == {} limit 20".format(acct)
        records = pd.read_sql_query(query, conn)
        conn.close()

        cols_to_show = ['date', 'company_name', 'company_industry', 'meeting_type',
                        'company_country', 'market_cap']
        records = records[cols_to_show]

        records_html = records.to_html(classes = ['table', 'table-striped', 'datatable'],
                                            border=0,
                                            table_id = 'investor_table')

        return render_template('investors.html', 
                                acct=acct,
                                tables=[records_html], 
                                titles=records.columns.values)




@app.route('/corporates/')
def corporates():

    conn = sqlite3.connect("citi.db")
    query = """SELECT * from roadshow_company 
                order by total_interactions desc limit 100"""
    corporates = pd.read_sql_query(query, conn)
    conn.close()

    top_corporates = corporates.groupby('company_name')['total_interactions'].sum().reset_index()\
                                .sort_values('total_interactions', ascending=False)\
                                .reset_index(drop=True)
    top_corporates['total_interactions'] = top_corporates['total_interactions'].astype(int)
    top_corporates = top_corporates.head(10).values.tolist()

    corporates['company_type'] = np.where(corporates['private_flag'] == 0, 'Public', 'Private')
    cols_to_show = ['company_name', 'company_region', 'company_type', 'year', 'total_interactions',
                    'unique_investors', 'one_on_one_pct', 'management_pct', 'vid_call_pct']
    corporates = corporates[cols_to_show]

    pct_cols = ('one_on_one_pct', 'management_pct', 'vid_call_pct')
    for colname in pct_cols:
        corporates[colname] = (corporates[colname]*100).round(1)

    html_colnames = ['Corporate', 'Region', 'Type', 'Year', 'Interactions',
                        'Unique Investors', '1:1 %', 'Mgmt %', 'Video Call %']

    select_values = {}
    select_values['years'] = sorted(list(set(corporates['year'])))
    select_values['regions'] = sorted(list(set(corporates['company_region'])))

    return render_template('corporates.html', 
                            data = corporates.values.tolist(),
                            colnames = cols_to_show,
                            html_colnames = html_colnames,
                            top_corporates = top_corporates,
                            select_values = select_values)



if __name__ == '__main__':
    print('hello world!')
    app.run(debug = True)