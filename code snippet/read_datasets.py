import pandas as pd 
import numpy as np 
import glob

job_list_fn = '/Users/vuthaiha/Documents/datathon/Oct_2019_Citadel/table_headers/dataset_1.csv'
uk_emp_data_fn = '/Users/vuthaiha/Documents/datathon/Oct_2019_Citadel/table_headers/dataset_2.csv'
labor_market_fn = '/Users/vuthaiha/Documents/datathon/Oct_2019_Citadel/table_headers/dataset_3.csv'
citi_app_fn = '/Users/vuthaiha/Documents/datathon/Oct_2019_Citadel/table_headers/dataset_4.csv'
lse_fn =='/Users/vuthaiha/Documents/datathon/Oct_2019_Citadel/table_headers/dataset_5.csv' # london stock exchange
public_act_fn = '/Users/vuthaiha/Documents/datathon/Oct_2019_Citadel/table_headers/dataset_6.csv'

def read_df(fn):
	df = pd.read_csv(fn, header = 0)
	return df

def change_to_datetime_job_list_df (column):
	column = column.apply(lambda x: x[:10])
	column = pd.to_datetime(column, format = '%Y-%m-%d')
	return column 

def read_job_list_df():
	job_list_df = read_df(job_list_fn)
	job_list_df['created'] = change_to_datetime_job_list_df(job_list_df['created'])
	job_list_df['last_checked'] = change_to_datetime_job_list_df(job_list_df['last_checked'])
	#job_list_df['last_updated'] = change_to_datetime_job_list_df(job_list_df['last_updated'])
	job_list_df['delete_date'] = change_to_datetime_job_list_df(job_list_df['delete_date'])
	return job_list_df


def read_uk_emp_data_df ():
	df = read_df(uk_emp_data_fn)
	df = df.dropna(how = 'all', axis = 1) # drop columns that contain all missisng values
	# what I can do: number of people in employment by each category: [u'year', u'soc_occupation_code', u'soc_major', u'soc_minor', u'soc_unit', u'description', u'sex', u'emp_type', u'fp_time', u'value'] 
	# use example code df.groupby(['Name', 'Fruit'])['Number'].agg('sum')
	return df

def read_labor_market_df ():
	df = read_csv(labor_market_fn)
	# what we can do: this is time series data of the number of each of the categories in the labor market code dataframe. We can potentially regress against time to see what categories have been increasing over time
	df =  df.dropna(how = 'all', axis = 1) # drop columns that contain all missisng values
	return df

def read_citi_app_df (): # df of citizenship applications
	df = read_csv(citi_app_fn)
	df =  df.dropna(how = 'all', axis = 1) # drop columns that contain all missisng values
	df['total'] = df[df.columns[2:]].sum(axis=1) # total number of citizenship applications over each time window
	# what we can do: investigate the trends of number of citizenship applications over time
	return df

def read_lse_df():
	df = read_csv(lse_fn)
	df =  df.dropna(how = 'all', axis = 1) # drop columns that contain all missisng values
	df['list_date'] = pd.to_datetime(df['list_date'], format = '%m/%d/%Y')
	return df

def read_public_act_df():
	df = read_csv(public_act_fn)
	return df # I still have to change the date_of_act column but I think this dataset is not that useful. 
