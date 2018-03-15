import requests, json


url = 'https://v3.exchangerate-api.com/bulk/fe12dc4317270c8c24e99e6a/PKR'

# Making our request
response = requests.get(url)
curr_json = json.loads(response.text)
print (curr_json['rates']['GBP'])
