from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class User(models.Model):

    username = models.CharField(
        max_length=255,
    )

    email = models.EmailField()

    def __str__(self):

        return ','.join([
            self.username,
            self.email,
        ])

    def get_absolute_url(self):

        return reverse('users-view', kwargs={'pk': self.id})

class Voto(models.Model):

    partido = models.CharField(
        max_length=255,
    )

    num_votos = models.PositiveIntegerField(default=0)

    def __str__(self):

        return ','.join([
            self.partido,
            self.num_votos,
        ])
