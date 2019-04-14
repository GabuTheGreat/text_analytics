#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 22:27:46 2019

@author: mutuandunda
"""
#import required librariea
import pandas as pd
import requests
import urllib
import tweepy


tweets = [{"user":"@DonaldBKipkorir", "text":"Year in, Year out, Kenya faces shortage of Maize, Wheat, Milk & Sugar yet we’ve abundance of land & ideal climate for production & export .. That we’ve been unable to have a working Food Policy & Strategy speaks volumes about our leadership, integrity & intellectual deficiency."},
 {"user":"@Tsharz", "text":"When your SDA boyfriend finds out that you have a tattoo."}]

results = []

for tweet in tweets:
    data = {"q":tweet["text"],"key":"5bcd8b088b96c563aecc9e82"}
    url = "https://api.textgain.com/age?" + urllib.parse.urlencode(data)
    print(url)
    result = requests.get(url).json()
    result['user'] = tweet["user"]
    result['message'] = tweet["text"]
    print(result)
    results.append(result)
    
analyzed_results = pd.DataFrame(results)