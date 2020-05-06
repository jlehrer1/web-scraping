import requests, sys, getopt
import json 
import tqdm 
import urllib.request
import os
import argparse

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Use case: {} <num images> <write location>'.format(sys.argv[0]))
        quit()

    if os.path.isdir(sys.argv[2]) == False:
        check = input('Current write location does not exist. Would you like to create it? [y/n]')
        if check == 'y':
            try:
                os.mkdir(sys.argv[2])
            except FileExistsError:
                print('Directory already exists. Contuinuing...')
        else:
            quit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('ERROR: {} could not be converted to an int'.format(sys.argv[1]))
        quit()
    
    tqdm.tqdm.write('Scraping images...')
    for i in tqdm.tqdm(range(n)):
        try:
            urllib.request.urlretrieve('https://picsum.photos/256', sys.argv[2] + '/{}.png'.format(i))
        except:
            i += 1
            continue
