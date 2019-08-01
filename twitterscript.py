#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "VJf9sJ6d7h6M3ZXjh88LOj329"
consumer_secret = "gUlXNLFcuVp74iHYvHkHAIhF5jopenZLq7a4vCM3cjiARUACyE"
access_key = "1106777766-jNNqrcKTfumdIka92MprUWXdAakUcttxAISzlWa"
access_secret = "x1Ugc82GPYgf7Li6r9vTSLRdiBnRDxW0mRB0zmsxY1Pko"


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while 20> len(new_tweets) > 0:
        print("getting tweets before %s"%(oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print( "...%s tweets downloaded so far" % (len(alltweets)))

    #transform the tweepy tweets into a 2D array that will populate the csv    
    outtweets = [[tweet.id_str] for tweet in alltweets]

    #write the csv    
    with open('%s_tweets.json' % screen_name, 'w') as f:
        writer = csv.writer(f)        
        writer.writerows(outtweets)

get_all_tweets('@drake')
