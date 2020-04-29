import requests, sys, getopt
import json 
import tqdm 
import numpy as np

# if len(sys.argv) != 3:
#     print('Use case: scrape.py <search term> <write location>')
#     quit()

params = {
    ('key','AIzaSyDA2z-ZOZcnkIjVKkwaAxXnYblHHY3lNUM'),
    ('cx', '017930800208229040610:cpgopip5no8'),
    ('q','dogs'),
    ('searchType', 'image'),
    ('num', 10) #max per day?
}

response = requests.get('https://www.googleapis.com/customsearch/v1?', params=params)
print(response.status_code)
# print(response.text)


