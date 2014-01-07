from TwitterAPI import TwitterAPI
from django import template

register = template.Library()

def f(value):
   api = TwitterAPI('wHz23ocOw4SolyUBWHLqvw', 'HgY1QGTAfcxHFdLichxWlqUqgmLgOFB8QUdSnnvuY0', '66269600-HvsEP0pnInp0IgmX23LkJJBjBVwwOxbqtd9FdsrTX', '8qOKgkpF9MafSzxz2f7Fb7I207Fpj7hZ5XxE6rl2P6ykW')
   r = api.request('search/tweets', {'q':'brasil'})
   for item in r.get_iterator():
      print item
      
