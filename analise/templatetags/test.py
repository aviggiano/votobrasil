from TwitterAPI import TwitterAPI
from django import template

register = template.Library()

class Oauthtest:
   'Oauth test'

   def __init__(self):
       api = TwitterAPI('wHz23ocOw4SolyUBWHLqvw', 'HgY1QGTAfcxHFdLichxWlqUqgmLgOFB8QUdSnnvuY0', '66269600-HvsEP0pnInp0IgmX23LkJJBjBVwwOxbqtd9FdsrTX', '8qOKgkpF9MafSzxz2f7Fb7I207Fpj7hZ5XxE6rl2P6ykW')
       r = api.request('search/tweets', {'q':'pizza'})
       for item in r.get_iterator():
           print item
