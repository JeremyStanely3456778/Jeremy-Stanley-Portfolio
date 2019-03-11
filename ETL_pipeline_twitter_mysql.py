#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:32:55 2019

@author: JeremyStanley

ETL datapipeline using python, mysql, tweepy, and NLTK to gather text data from twitter'
accounts for NLP  analysis.

"""
#-------------------------------------Imports/APIs----------------------------

import mysql.connector, json, time, os
from mysql.connector import Error
import tweepy
from dateutil import parser

#----------------------------------Environment Variables--------------------------------------------
 #set environment variables to connect twitter api and mysql
consumer_key = os.environ['CONSUMER_KEY'] = 'unknown'
consumer_secret = os.environ['CONSUMER_SECRET'] = 'unknown'
access_token = os.environ['ACESS_TOKEN'] = 'unknown'
access_token_secret = os.environ['ACCESS_TOKEN_SECRET'] = 'unknown'
env_password = os.environ['ENV_PASSWORD'] = 'unknown' 

#-----------------------------------------Classes and Functions--------------------------------------

def connect(username, created_at, tweet, retweet_count, place, location):
    
    #connect to the MySQL database twitterdb and insert data from twitter
    
    try:
        conn = mysql.connector.connect(host = 'localhost', database='twitterdb', user='root', password = env_password, charset = 'utf8')
        
        if conn.is_connected():
            
            #insert the data from twitter
            
            cursor = conn.connected()
            
            #twitter, comment
            
            query = "INSERT INTO COMMENT (username, created_at, tweet, retweet_count, place, location) VALUES (%s, %s, %s, %s, %s, %s)"
            
            cursor.execute(query, (username, created_at, tweet, retweet_count, place, location))
            
            conn.commit()
    
    except Error as e:
        print(e)
    
    cursor.close()
    
    conn.close()
    
    return

#-------------------------------Tweepy class to access twitter api-------------------------------
    
class Streamlistener(tweepy.StreamListener):
    
    def on_connect(self):

        print("Connected to the Twitter API")
        
        
    def on_error(self):
        
        if status_code != 200:
            
            print("error found")
            
            # if false is returned than the stream is disconnected
            return False 
        
        
    
    # This function reads in tweets as json data and then extracts the desired data      
    
    def on_data(self,data):
        
        try:
            raw_data = json.loads(data)
            
            if 'text' in raw_data:
                
                username = raw_data['user']['screen_name']
                
                created_at = parser.parse(raw_data['created_at'])
                
                tweet = raw_data['text']
                
                retweet_count = raw_data['retweet_count']
                
                if raw_data['place'] is not None:
                    
                    place = raw_data['place']['country']
                    
                    print(place)
                
                else:
                
                    place = None
            
            
            location = raw_data['user']['location']
            
            #call method function to insert collected data in MySQL database
            
            connect(username, created_at, tweet, retweet_count, place, location)
            
            print("Tweet collected at: {}".format(str(created_at)))
            
        
        except Error as e:
            print(e)
                
#---------------------------------Main--------------------------------------------
            
if __main__== '__main__':
    
    #authentication data so we can access twitter api
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth, wait_on_rate_limit = True)
    
    
    # create an instance of streamlistener
    
    listener = Streamlistener(api = api)
    
    stream = tweepy.Stream(auth, listener = listener)
    
    track = ['customer service', 'help', 'service', 'deals']
    
    stream.filter(track = track, langauges = ['en'])
    
    
    
    
    
    
    
    





 

 