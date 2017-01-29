# -*- coding: utf-8 -*-
import tweepy
import settings
import oauth

class MyStreamListener(tweepy.MyStreamListener):
  def on_status(self, status):
    if status.text[0] == '@': return
    if not status.favorited:
      api.create_favorite(status.id)

  def on_error(self, status_code):
    if status_code == 420:
      return False

if __name__ == '__main__':
  db = oauth.load_database()
  main_id = input('Your user id: ')
  api = oauth.get_api(db, main_id)
  myStream = tweepy.Stream(api.auth, MyStreamListener())
  myStream.userstream()