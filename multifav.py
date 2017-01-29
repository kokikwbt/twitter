# -*- coding: utf-8 -*-
import json
import tweepy
import settings

auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,
                           settings.CONSUMER_SECRET)

def load_database():
  with open('./account.db', 'r') as f:
    database = json.load(f)
  return database

def get_tokens(database):
  tokenlist = []
  for id in database.keys():
    token = database[id]['token']
    secret = database[id]['secret']
    tokenlist.append((token, secret))
  return tokenlist

def main_token(database, userid):
  token = database[userid]['token']
  secret = database[userid]['secret']
  auth.set_access_token(token, secret)
  api = tweepy.API(auth)
  return api

def multi_fav(tokenlist, status):
  for i in range(len(tokenlist)):
    auth.set_access_token(tokenlist[i][0], tokenlist[i][1])
    api = tweepy.API(auth)
    api.create_favorite(status.id)
  return

def multi_retweet(tweetid):
  return

def disp_tweet(api, userid, num=10):
  tweet = []
  timeline = api.user_timeline(userid, count=num)
  print('Tweets @', userid)
  print('----------------------------------------')
  for i in range(num):
    print('[', i, ']', timeline[i].text)
    print('----------------------------------------')
  return timeline

def main():
  db = load_database()
  tokenlist = get_tokens(db)
  main_id = input('Your user id: ')
  api = main_token(db, main_id)
  while(1):
    target_id = input('Target user id: ')
    tweets = disp_tweet(api, target_id)
    status_id = int(input('target status id: '))
    if status_id >= 0 and status_id < 10:
      multi_fav(tokenlist, tweets[status_id])
    end = input('End? (yes: 1,no: 0) ')
    if end: break
  return

if __name__ == '__main__':
  main()