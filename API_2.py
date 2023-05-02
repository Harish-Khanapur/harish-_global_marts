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





