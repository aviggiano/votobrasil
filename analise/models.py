from django.db import models
from TwitterAPI import TwitterAPI

class User(models.Model):

    screen_name = models.CharField(
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
            self.screen_name,
            self.id_str,
            self.geo,
        ])

class TweetManager(models.Manager):
    def create(self, user=None, id_str=None, text=None, lang=None):
        consumer_key = 'wHz23ocOw4SolyUBWHLqvw'
        consumer_secret = 'HgY1QGTAfcxHFdLichxWlqUqgmLgOFB8QUdSnnvuY0'
        access_token_key = '66269600-HvsEP0pnInp0IgmX23LkJJBjBVwwOxbqtd9FdsrTX'
        access_token_secret = '8qOKgkpF9MafSzxz2f7Fb7I207Fpj7hZ5XxE6rl2P6ykW'
        
        api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        r = api.request('search/tweets', {'q':'brasil'})
        
        tweet_list = []
        for i in r.get_iterator():
            tweet_list.append(i)
        tw = tweet_list[0]

        user_screen_name = tw['user']['screen_name']
        user_id_str = tw['user']['id_str']
        user_geo = tw['user']['location'] # TODO mudar

        self.user = User(screen_name = user_screen_name,
                    id_str = user_id_str,
                    geo = user_geo)
        self.id_str = tw['id_str']
        self.text = tw['text']
        self.lang = tw['lang']

        tweet = self.create(user = user,
                            id_str = id_str,
                            text = text,
                            lang = lang)
            
        return tweet

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

    objects = TweetManager()

    @classmethod
    def refresh(self):
        consumer_key = 'wHz23ocOw4SolyUBWHLqvw'
        consumer_secret = 'HgY1QGTAfcxHFdLichxWlqUqgmLgOFB8QUdSnnvuY0'
        access_token_key = '66269600-HvsEP0pnInp0IgmX23LkJJBjBVwwOxbqtd9FdsrTX'
        access_token_secret = '8qOKgkpF9MafSzxz2f7Fb7I207Fpj7hZ5XxE6rl2P6ykW'
        
        api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        r = api.request('search/tweets', {'q':'brasil'})
        
        tweet_list = []
        for i in r.get_iterator():
            tweet_list.append(i)
        tw = tweet_list[0]

        user_screen_name = tw['user']['screen_name']
        user_id_str = tw['user']['id_str']
        user_geo = tw['user']['location'] # TODO mudar

        self.user = User(screen_name = user_screen_name,
                    id_str = user_id_str,
                    geo = user_geo)
        self.id_str = tw['id_str']
        self.text = tw['text']
        self.lang = tw['lang']

    def __str__(self):

        return ';'.join([
            str(self.user),
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

