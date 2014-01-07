from django.db import models

class User(models.Model):

    user = models.CharField(
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
            self.user,
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
