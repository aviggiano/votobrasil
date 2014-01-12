from django.db import models
from TwitterAPI import TwitterAPI

class User(models.Model):

    username = models.CharField(
        max_length=255,
    )

    id_str = models.CharField(
        max_length=255,
    )
    
    geo = models.CharField(
        max_length=255,
    )
    
    def __str__(self):

        return ';'.join([
            self.username,
            self.id_str,
            self.geo,
        ])

class Tweet(models.Model):

    user = models.ForeignKey(User)    

    id_str = models.CharField(
        max_length=255,
    )

    text = models.CharField(
        max_length=255,
    )

    lang = models.CharField(
        max_length=255,
    )

    def __init__(self, user=None):
        user = user

        consumer_key = 'wHz23ocOw4SolyUBWHLqvw'
        consumer_secret = 'HgY1QGTAfcxHFdLichxWlqUqgmLgOFB8QUdSnnvuY0'
        access_token_key = '66269600-HvsEP0pnInp0IgmX23LkJJBjBVwwOxbqtd9FdsrTX'
        access_token_secret = '8qOKgkpF9MafSzxz2f7Fb7I207Fpj7hZ5XxE6rl2P6ykW'
        
        api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        r = api.request('search/tweets', {'q':'pizza'})
        print r.status_code
#        for item in r.get_iterator():
#            print item

    def __str__(self):

        return ';'.join([
            self.user,
            self.id_str,
            self.text,
            self.lang,
        ])

class Voto(models.Model):

    user = models.ForeignKey(User)

    partido = models.CharField(
        max_length=255,
    )

    confianca = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):

        return ','.join([
            self.user,
            self.partido,
            str(self.confianca),
        ])
