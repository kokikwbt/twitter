# -*- coding: utf-8 -*-
import json
import tweepy
import settings
import oauth

auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,
                           settings.CONSUMER_SECRET)

def multi_fav(tokenlist, status):
  for i in range(len(tokenlist)):
    auth.set_access_token(tokenlist[i][0], tokenlist[i][1])
    api = tweepy.API(auth)
    try:
      api.create_favorite(status.id)
    except tweepy.TweepError as e:
      exit('Cannot favorite')
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
  db = oauth.load_database()
  tokenlist = oauth.get_tokens(db)
  main_id = input('Your user id: ')
  api = oauth.get_api(db, main_id)
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