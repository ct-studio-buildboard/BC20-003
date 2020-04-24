import pandas as pd
import sqlite3
import time
import numpy as np

def upload_data(filename):

	conn = sqlite3.connect("citi.db")

	#Load interactions data
	query = "select * from interactions_roadshow"

	interactions = pd.read_sql_query(query, conn)
	interactions['market_cap'] = interactions['market_cap'].astype(float)



	df = pd.read_csv('../sample_input_data.csv')
	df['Region Visited'] = df['Country Visited']
	cols = list(df.columns)
	print(df.shape)



	query = "select * from corporates"

	corporates = pd.read_sql_query(query, conn)

	#Adding Null Columns

	df = pd.merge(df, corporates, how='left', 
					left_on = ['Company Name', 'Company Region', 
								'Company Country', 'Company Industry'],
					right_on = ['company_name', 'company_region',
								'company_country', 'company_industry'])

	new_corporates = df.loc[pd.isnull(df['corporate_id']), :]

	df = df[cols]

	new_corporates = new_corporates[['Company Name', 'Company Region', 
								'Company Country', 'Company Industry']].drop_duplicates()
	new_corporates.columns = ['company_name', 'company_region',
								'company_country', 'company_industry']

	new_corporates.to_sql('corporates', conn, if_exists='append', index=False)

	query = "select * from corporates"
	corporates = pd.read_sql_query(query, conn)

	df = pd.merge(df, corporates, how='left', 
					left_on = ['Company Name', 'Company Region', 
								'Company Country', 'Company Industry'],
					right_on = ['company_name', 'company_region',
								'company_country', 'company_industry'])

	df = df[cols + ['corporate_id']]

	df['management_flag'] = 1
	df.loc[df['Mgmt'] == 'N', 'management_flag'] = 0
	df['Date'] = pd.to_datetime(df['Date'])
	df['month'] = df['Date'].dt.month
	df['year'] = df['Date'].dt.year
	df['month_start'] = df.apply(lambda x: pd.to_datetime('{}-{}-01'.format(x['year'], x['month'])), axis=1)


	print(df.columns)

	cols = ['Event Name', 'PM/Contact', 'Analyst', 'Account Name',
			'Acct.', 'SGP', 'Investor Region', 'Equity Tier',
			'Global Access', 'Company Name', 'RIC', 'Company Industry',
			'Product Region', 'Company Region', 'Company Country', 
			'Market Cap ($mm)', 'Market Bucket', 'Ratings', 'Date',
			'Event Type', 'Meeting Type', 'Global Region Visited',
			'Region Visited',
			'Country Visited', 'City', 'Medium', 'Webcast',
			'Open Exchange Indicator', 'management_flag', 'Meeting Corporate Title',
			'year', 'month', 'month_start', 'corporate_id'
			]
	print(len(cols))

	df = df[cols]

	df.columns = ['event_name', 'pm', 'analyst_name', 'account_name', 
					'acct', 'sgp', 'investor_region', 'equity_tier', 
					'global_access', 'company_name', 'ric', 'company_industry', 
					'product_region', 'company_region', 'company_country', 
					'market_cap', 'market_bucket', 'ratings', 'date', 'event_type',
					 'meeting_type', 'global_region_visited', 'region_visited', 
					 'country_visited', 'city', 'medium', 'webcast', 
					 'open_exchange_indicator', 'management_flag', 'corporate_title', 
					 'year', 'month', 'month_start', 'corporate_id']

	df = df.loc[df['company_name'] != 'Industry Experts', :]
	df = df.loc[df['event_type'].isin(('Reverse Roadshow', 'Non Deal Roadshow')), :]

	# print(df.dtypes)
	# print(interactions.dtypes)
	# exit()



	df['date'] = pd.to_datetime(df['date'])
	df['month_start'] = pd.to_datetime(df['month_start'])
	df['acct'] = df['acct'].astype(str)

	interactions['date'] = pd.to_datetime(interactions['date'])
	interactions['month_start'] = pd.to_datetime(interactions['month_start'])
	interactions['acct'] = interactions['acct'].astype(str)

	print(df.dtypes)
	print('~~~~~~~~~')
	print(interactions.dtypes)

	df = df.append(interactions)

	trial = df.loc[df['company_name'] == 'Right Direction', :]

	# print()

	print(trial.nunique())






	# exit()

	start = time.time()
	df = df.drop_duplicates(ignore_index=True)
	print(time.time() - start)

	print(df.dtypes)

	df.to_sql('interactions_roadshow', conn, if_exists='replace', index=False)



	# Write to investor summary table
	grp = ['acct', 'investor_region', 'year', 'global_access']
	roadshow_investor = interactions.groupby(grp).apply(lambda x: pd.Series({'total_interactions': x['company_name'].count(),
																																	'unique_corporates': x['company_name'].nunique(),
																																	'unique_industries': x['company_industry'].nunique(),
																																 'one_on_one_pct': (x['meeting_type'] == '1:1').mean(),
																																 'group_pct': (x['meeting_type'] == 'Group').mean(),
																																 'management_pct': x['management_flag'].mean(),
																																 'market_cap_mean': x['market_cap'].mean(),
																																 'market_cap_median': x['market_cap'].median(),
																																 'large_pct': (x['market_bucket'] == 'Large').mean(),
																																 'private_pct': (x['market_bucket'] == 'Private/unknown').mean(),
																																'us_pct': (x['company_region'] == 'US').mean(),
																																'meeting_pct': (x['medium'] == 'Meeting').mean(),
																																'conf_call_pct': (x['medium'] == 'Conference Call').mean(),
																																'vid_call_pct': (x['medium'] == 'Video Call').mean(),
																																'webcast_pct': (x['webcast'] == 'Y').mean(),
																																'open_ex_pct': (x['open_exchange_indicator'] == 'Y').mean()

																																	}))\
			.reset_index()

	roadshow_investor.to_sql('roadshow_investor', conn, if_exists='replace', index=False)

	# Write to corporate summary table
	grp = ['corporate_id', 'company_name', 'company_region', 'year']
	roadshow_company = interactions.groupby(grp).apply(lambda x: pd.Series({'total_interactions': x['date'].count(),
																																	'unique_investors': x['date'].nunique(),
																																 'one_on_one_pct': (x['meeting_type'] == '1:1').mean(),
																																 'group_pct': (x['meeting_type'] == 'Group').mean(),
																																 'management_pct': x['management_flag'].mean(),
																																	 'market_cap_avg': x['market_cap'].mean(),
																																	'platinum_pct': (x['global_access'] == 'Global Access Platinum').mean(),
																																	'meeting_pct': (x['medium'] == 'Meeting').mean(),
																																'conf_call_pct': (x['medium'] == 'Conference Call').mean(),
																																'vid_call_pct': (x['medium'] == 'Video Call').mean(),
																																'webcast_pct': (x['webcast'] == 'Y').mean(),
																																'open_ex_pct': (x['open_exchange_indicator'] == 'Y').mean(),

																																	}))\
			.reset_index()
	roadshow_company['private_flag'] = np.where(pd.isnull(roadshow_company['market_cap_avg']), 1, 0)

	roadshow_company.to_sql('roadshow_company', conn, if_exists='replace', index=False)



	conn.close()
