#!/usr/bin/env python
# coding: utf-8

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