from django.db import models

class User(models.Model):

    username = models.CharField(
        max_length=255,
    )

    email = models.EmailField()

    owner = models.ForeignKey(auth.models.User)

    def __str__(self):

        return ' '.join([
            self.first_name,
    def __str__(self):

        return ' '.join([
            self.username,
            self.email,
        ])

class Voto(models.Model):

    user = models.ForeignKey(User)

    partido = models.CharField(
        max_length=255,
    )

    num_votos = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'num_votos',)

    def __str__(self):

        return ','.join([
            self.partido,
            str(self.num_votos),
        ])
