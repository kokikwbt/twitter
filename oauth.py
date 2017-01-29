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

def get_api(database, userid):
  token = database[userid]['token']
  secret = database[userid]['secret']
  auth.set_access_token(token, secret)
  api = tweepy.API(auth)
  return api
