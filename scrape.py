import requests, sys, getopt
import json 
import tqdm 
import urllib.request
import os
import argparse

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Use case: scrape.py <params file> <search term> <write location>')
        quit()

    if os.path.isdir(sys.argv[3]) == False:
        check = input('Current write location does not exist. Would you like to create it? [y/n]')
        if check == 'y':
            try:
                os.mkdir(sys.argv[3])
            except OSError:
                print('Attempt to make directory failed...')
        else:
            quit()
    try:
        params = open(sys.argv[1])
    except:
        raise FileNotFoundError
    
    key = params.readline().rstrip()
    cx = params.readline().rstrip()

    for i in tqdm.tqdm(range(1,11)):
        params = {
            ('key', key),
            ('cx', cx),
            ('q', sys.argv[2]),
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
                try:
                    urllib.request.urlretrieve(responses['link'], sys.argv[3] + '/{}{}.png'.format(i,j))
                except:
                    continue
    