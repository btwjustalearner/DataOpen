import pandas as pd 
import numpy as np 
import glob

def read_df(fn):
	df = pd.read_csv(fn, header = 0)
	return df

code_legends_dir = '/Users/vuthaiha/Documents/datathon/Oct_2019_Citadel/table_headers/code_legends'
code_legends_fn_list = glob.glob(code_legends_dir + "/*.csv")
code_legends_name_list = map(lambda x: (x.split('/')[-1]).split('.')[0], code_legends_fn_list)
# print "code_legends_fn_list"
# print code_legends_fn_list
# print 
# print "code_legends_name_list"
# print code_legends_name_list
# print
IMMIGRANT_CODE = 0
SOC_CODE = 1
ONET_CODE = 2
LABOR_MARKET_CODE = 3

def read_immigrant_code_df ():
	immigrant_code_df = read_df(code_legends_fn_list[IMMIGRANT_CODE])
	immigrant_code_df.columns = ['code', 'geo_region', 'nationality']
	return immigrant_code_df

def read_soc_code_df():
	soc_code_df = read_df(code_legends_fn_list[SOC_CODE])
	soc_code_df.columns = ['major', 'sub_major', 'minor', 'unit', 'group_title']
	return soc_code_df

def read_onet_code_df(): 
	onet_code_df = read_df(code_legends_fn_list[ONET_CODE])
	onet_code_df.columns = ['code', 'title', 'description']
	onet_code_df['soc_sub_major'] = (onet_code_df['code']).apply(lambda x: x.split('-')[0])
	onet_code_df['soc_unit'] = (onet_code_df['code']).apply(lambda x: (x.split('-')[1]).split('.')[0]) # 11-1011.00 --> 1011
	return onet_code_df

def read_labor_market_df():
	labor_market_code_df = read_df(code_legends_fn_list[LABOR_MARKET_CODE])
	labor_market_code_df = labor_market_code_df.dropna(how = 'all', axis = 1) # drop columns that contain all missisng values
	return labor_market_code_df

soc_code_df = read_soc_code_df()
immigrant_code_df = read_immigrant_code_df()
onet_code_df = read_onet_code_df()
labor_market_code_df = read_labor_market_df()
