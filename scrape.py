import requests, sys, getopt
import json 
import tqdm 
import numpy as np
import urllib.request
import os
import argparse

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Use case: scrape.py <search term> <write location>')
        sys.exit()

    for i in tqdm.tqdm(range(1,11)):
        params = {
            ('key','KEY'),
            ('cx', 'CX'),
            ('q', sys.argv[1]),
            ('searchType', 'image'),
            ('num', 10), #max per day?
            ('safe', 'off'),
            # ('imgColorType', 'grey')
            ('start', i),
        }

        response = requests.get('https://www.googleapis.com/customsearch/v1?', params=params)
        if response.status_code == 200:
            for j, responses in tqdm.tqdm(enumerate(response.json()['items'])):
                urllib.request.urlretrieve(responses['link'], sys.argv[2] + '/{}{}.png'.format(i,j))
        else:
            print('API Error')
            sys.exit()
