import requests, sys, getopt
import json 
import tqdm 
import urllib.request
import os
import argparse

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Use case: scrape.py <search term> <write location>')
        quit()

    if os.path.isdir(sys.argv[2]) == False:
        try:
            os.mkdir(sys.argv[2])
        except OSError:
            print('Attempt to make directory failed')


    for i in tqdm.tqdm(range(1,11)):
        params = {
            ('key','AIzaSyDA2z-ZOZcnkIjVKkwaAxXnYblHHY3lNUM'),
            ('cx', '017930800208229040610:cpgopip5no8'),
            ('q', sys.argv[1]),
            ('searchType', 'image'),
            ('num', 10), #max per day?
            ('safe', 'off'),
            # ('imgColorType', 'grey')
            ('start', i),
        }

        response = requests.get('https://www.googleapis.com/customsearch/v1?', params=params)
        if response.status_code >= 400:
            print('API error: {}'.format(str(response.status_code)))
            quit()
        else:
            for j, responses in tqdm.tqdm(enumerate(response.json()['items'])):
                urllib.request.urlretrieve(responses['link'], sys.argv[2] + '/{}{}.png'.format(i,j))
    