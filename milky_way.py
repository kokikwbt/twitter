# -*- coding: utf-8 -*-
import tweepy
import oauth
import settings

database = oauth.load_database()
user_id = input('Your id: ')
api = oauth.get_api(database, user_id)
target_id = input('Target id: ')
count = int(input('# of favs: '))
timeline = tweepy.user_timeline(target_id, count=count)

# Milky way
for i in range(count):
  status = timeline[0]
  if status.text[0] == '@':
    continue
  if not status.favorited:
      api.create_favorite(status.id)
