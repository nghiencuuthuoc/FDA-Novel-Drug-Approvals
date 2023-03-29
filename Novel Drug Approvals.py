import pandas as pd

def Novel_Drug_Approval_2021(url):
	df = pd.read_html(url)
	df1 = df[0]
	df2 = pd.DataFrame(df1)
	data_2021 = df2.to_csv('2021.csv', index=None)
	return data_2021
 
def Novel_Drug_Approval_2020(url):
	df = pd.read_html(url)
	df1 = df[0]
	df2 = pd.DataFrame(df1)
	data_2020 = df2.to_csv('2020.csv', index=None)
	return data_2020

def Novel_Drug_Approval_2019(url):
	df = pd.read_html(url)
	df1 = df[0]
	df2 = pd.DataFrame(df1)
	data_2019 = df2.to_csv('2019.csv', index=None)
	return data_2019

def Novel_Drug_Approval_2018(url):
	df = pd.read_html(url)
	df1 = df[0]
	df2 = pd.DataFrame(df1)
	data_2018 = df2.to_csv('2018.csv', index=None)
	return data_2018

def Novel_Drug_Approval_2017(url):
	df = pd.read_html(url)
	df1 = df[0]
	df2 = pd.DataFrame(df1)
	data_2017 = df2.to_csv('2017.csv', index=None)
	return data_2017

def Novel_Drug_Approval_2016(url):
	df = pd.read_html(url)
	df1 = df[0]
	df2 = pd.DataFrame(df1)
	data_2016 = df2.to_csv('2016.csv', index=None)
	return data_2016

def Novel_Drug_Approval_2015(url):
	df = pd.read_html(url)
	df1 = df[0]
	df2 = pd.DataFrame(df1)
	data_2015 = df2.to_csv('2015.csv', index=None)
	return data_2015


print(Novel_Drug_Approval_2021('https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/novel-drug-approvals-2021'))
print(Novel_Drug_Approval_2020('https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/novel-drug-approvals-2020'))
print(Novel_Drug_Approval_2019('https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/novel-drug-approvals-2019'))
print(Novel_Drug_Approval_2018('https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/novel-drug-approvals-2018'))
print(Novel_Drug_Approval_2017('https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/novel-drug-approvals-2017'))
print(Novel_Drug_Approval_2016('https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/novel-drug-approvals-2016'))
print(Novel_Drug_Approval_2015('https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/novel-drug-approvals-2015'))
      