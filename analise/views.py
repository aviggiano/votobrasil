from django.views.generic import ListView
from analise.models import Tweet
import TwitterAPI

class ListTweetView(ListView):

    model = Tweet
    template_name = 'tweet-list.html'
