#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:23:21 2019

@author: JeremyStanley

Analyze data created from twitterdb and create a word cloud and perform rudimentry scentiment analysis.

"""
#------------------------------------Import Libraries-------------------------------------------

import mysql.connector, os, re, nltk

from mysql.connector import Error

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer

from wordcloud import WordCloud, STOPWORDS

import numpy as np

import matplotlib as plt
 
from textblob import TextBlob

import pandas as pd

#-----------------------------------Classes and Method Functions---------------------------------

#passes authentication variables

class TweetObjects():
    
    def __init__(self, host, database, user):
        
        self.password = 'unknown'
        
        self.host = host
        
        self.database = database
        
        self.user = user
        
    
    def MySQLConnect(self, query):
        
        # connects with database and pulls raw tweets made by customers and other columns we specify
        # the arguemnt is a string SQL query and returns a pandas dataframe
        
        try:
            
            con = mysql.connector.connect(host = self.host, database = self.database, user = self.user, password = self.password, charset = 'utf8')
        
            if con.is_connected():
                
                print("Database Connection Sucessful")
                
                
                
                cursor = con.cursor()
                
                query = query
                
                cursor.execute(query)
                
                
                data = cursor.fetchall()
                
                #stores it in a dataframe
                df = pd.DataFrame(data, columns = ['data', 'tweet'])
                
        except Error as e:
            print(e)
        
        
        cursor.close()
        
        con.close()
        
        return df

    
    def clean_tweet(self, df):
        
        """
        takes in raw tweet data inorder to analyze it
        
        cleans tweets by getting ridd of stopwords, punctuations,  lowercase, html code, emoticons,
        
        using regex for this operation
        
        """
        
        # text preprocessing
        
        stopword_list = stopwords.words('english')
        
        ps = PortStemmer()
        
        df = ["clean_tweets"] = None
        
        df = ['len'] = None
        
        for i in range(0, len(df['tweet'])):
            
            #removes characters that are not a letters
            
            exclusive_list = ['[a-zA-Z]', 'rt', 'http', 'co', 'RT']
            
            exclusions = '|'.join(exclusion_list)
            
            text = re.sub(exclusions, ' ', df['tweet'][i])
            
            text = text.lower()
            
            words = [word for words in words if not word in stop_word_list]
            
            # if you only want to usee stem words
            
            #words = [ps.stem(word) for word in words]
            
            df['clean_tweets'][i] = ''.join(words)
            
       # make column with data length
       
        df['len'] = np.array([len(tweet) for tweet in data["clean_tweets"]])
    
        return df
   
    
    def sentiment(self, tweet):
        
        """
        this part calculates sentiment from our clean tweets
        
        use textblob to calculate  polarity.
        
        arguement is one row of dataframe (one tweet)
        """
    
        analysis = TextBlob(tweet)
        
        if analysis.sentiment.polarity > 0:
            return 1
        
        elif analysis.sentiment.polarity == 0:
            return 0
        
        else:
            
            return -1
        
        
    def save_to_csv(self, df):
        
        # save cleaned data to a csv file so as to perform analysis later on
        
        # the arguement is the pandas dataframe which was created
        
        try: 
            
            df.to_csv("clean_tweets.csv")
            
            print("\n")
            
            print("csv was saved with success. \n")
            
        except Error as e:
            print(e)
            
       
    def word_cloud(self, df):
        
        plt.subplots(figsize = (12, 10))
        
        word.cloud = WordCloud(background_color = 'white', width = 1000, height = 800).generate(" ".join(df['clean_tweets']))
        
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()

#-----------------------------------Main--------------------------------------------------------------
        

if __main__ == '__main__':
    
    t = TweetObject(host = 'localhost', database = 'twitterdb', user = 'root')
    
    data = t.MySQLConnect("SELECT created_at, tweet FROM `TwitterDB`. `COMMENT`;")
    
    data = t.clean_tweets(data)
    
    data['Sentiment'] = np.array([t.sentiment(x) for x in data['clean_tweets']])
    
    t.word_cloud(data)
    
    t.save_to_csv(data)
    
    # time to calculate percentages of positive, negative, and neutral tweets and display resutls to console
    
    pos_tweets = [tweet for index, tweet in enumerate(data["clean_tweets"]) if data["Sentiment"][index] > 0]
    
    neg_tweets = [tweet for index, tweet in enumerate(data["clean_tweets"]) if data["Sentiment"][index] < 0]
    
    pos_tweets = [tweet for index, tweet in enumerate(data["clean_tweets"]) if data["Sentiment"][index] == 0]
    
    print("positive tweets: {}%".format(100 *(len(pos_tweets) / len(data['clean_tweets']))))
    
    print("negative tweets: {}%".format(100 *(len(pos_tweets) /len(data['clean_tweets']))))
    
    print("neutral tweets: {}%".format(100 *(len(pos_tweets) / len(data['clean_tweets']))))



    
    
    
    
    