#!/usr/bin/env python
# coding: utf-8


import requests
# Edpoint URL
url = "https://globalmart-api.onrender.com/mentorskool/v1/sales?offset=1&limit=100"
#access token
access_token= "fe66583bfe5185048c66571293e0d358"
# header access token
headers = {
    "access_token":"fe66583bfe5185048c66571293e0d358"
}
# make request to the API with the headers
response = requests.get(url, headers = headers)
# check the response status code
if response.status_code == 200:
#process response data
    data = response.json()
    print(data)
else:
    print("Request failed with status code: ", response.status_code)




import requests

url='https://globalmart-api.onrender.com/mentorskool/v1/sales'

headers={"access_token":"fe66583bfe5185048c66571293e0d358"}

response=requests.get(url, headers=headers)
response

response_json=response.json()
response_json

base_url='https://globalmart-api.onrender.com'
endpoint="/mentorskool/v1/sales?offset=0&limit=100"
url =base_url+endpoint
final_list=[]
next= ""
for i in range(5):
    if next != "":
        url=base_url+next
    response = requests.get(url, headers=headers)
    data=response.json()["data"]
    next = response.json()["next"]
    final_list.extend(data)       

import pandas as pd
sales_df =pd.json_normalize(final_list)
sales_df



#defining input values
import requests
n_records=int(input(f'no of records:'))
limit= int(input(f'limit: '))
sales_data=[]

for offset in range(0,n_records,limit):
#define the url
    url=f'https://globalmart-api.onrender.com/mentorskool/v1/sales?offset={offset}&limit={limit}'
#exception handleing
    try:
        response=requests.get(url,headers={"access_token":"fe66583bfe5185048c66571293e0d358"})
        response.raise_for_status()
        sales_data.extend(response.json()['data'])
        print(f'retriving data...{offset+limit} records obtained')
    except requests.exceptions.HTTPError as err:
        print(f'HTTP error while fetchinfg data: {err}')
        break
    except requests.exceptions.RequestExpection as err:
        print(f'request error while fetchinfg data: {err}')
        break
    except IndexError as err:
        print(f'Index out of range error occurred: {err}')
        break
              
print(f'data collection completed with {len(sales_data)} records obtained.')
#define the index
n=int(input('access which index: '))
try:
    print(sales_data[n])
except IndexError as err:
    print(f'index out of range error occurred: {err}')





