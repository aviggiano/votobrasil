from django.views.generic import ListView
from analise.models import Tweet


class ListTweetView(ListView):

    model = Tweet
    template_name = 'tweet-list.html'
