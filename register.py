# -*- coding: utf-8 -*-
import os
import json
from getpass import getpass
import tweepy
import settings

def main():
  account_id = input('Account id: ')
  password = getpass('Password: ')
  #if
  with open('./account.db', 'r') as f:
    database = json.load(f)
    if account_id in database.keys():
      exit('This account has already registered.')

  # oauth
  auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,
                             settings.CONSUMER_SECRET)
  try:
    redirect_url = auth.get_authorization_url()
    print('Please authorize: ' + redirect_url)
    verifier = input('PIN: ')
    access_token = auth.get_access_token(verifier)
  except tp.TweepError:
    print('Error! Failed to get request token.')

  # save access token
  info = {'password': password,
          'token': auth.access_token,
          'secret': auth.access_token_secret}
  database.update({account_id: info})
  with open('./account.db', 'w') as f:
    json.dump(database, f, indent=2)


if __name__ == '__main__':
  main()