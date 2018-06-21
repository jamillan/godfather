#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
 
CONSUMER_KEY = "HGsCa24B9jlGFiDpRaBemTyjj"
CONSUMER_SECRET = "BA87yf8QyolGnTUmHEc07A1ZfnKbmHa6GfMRj3tBEJ8lWMFGPH"
ACCESS_TOKEN = "1006801061754097664-I7ziYNHGJ3ydUPgtEP0wYEvTBYuWJz"
ACCESS_TOKEN_SECRET = "Xz3kwLMXd7UYDpkyjNMfXn5ATnW3njLNVuybST3ci5v3k"
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
#list of specific strings we want to check for in Tweets
t = ['Hello',
    'hello']
 
public_tweets = api.home_timeline()
idx= 0 ;
for tweet in public_tweets:
    buffer_str =str(tweet.text).split()
    if idx == 0: 
            m = buffer_str[0] + " podcast"
            print(tweet.id) 
            user = api.get_user(buffer_str[0]) 
            print(user.) 
            #s = api.update_status(m, s.id) 

    idx= idx + 1 
quit()



for s in twts:
    print(s.text)
    for i in t:
        if i == s.text:
            print("found match")
            sn = s.user.screen_name
            m = "@%s Hello!" % (sn)
            s = api.update_status(m, s.id)
