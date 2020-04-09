from flask import Flask, redirect, url_for, render_template, url_for, request, session
import sqlite3
import json
from collections import defaultdict
import pandas as pd
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

        investors_html = investors.to_html(classes = ['table', 'table-striped', 'datatable'],
                                            border=0,
                                            table_id = 'investor_table')



        return render_template('investors.html', 
                                tables=[investors_html], 
                                titles=investors.columns.values,
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
    query = "SELECT * from roadshow_company limit 20"
    corporates = pd.read_sql_query(query, conn)
    conn.close()

    cols_to_show = ['company_name', 'company_region', 'year', 'total_interactions',
                    'unique_investors']
    corporates = corporates[cols_to_show]

    corporates_html = corporates.to_html(classes = ['table', 'table-striped', 'datatable'],
                                        border=0,
                                        table_id = 'corporate_table')



    return render_template('corporates.html', 
                            tables=[corporates_html])



if __name__ == '__main__':
    print('hello world!')
    app.run(debug = True)