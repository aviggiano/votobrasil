from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView
from analise.models import Tweet
import TwitterAPI

class ListTweetView(ListView):

    model = Tweet
    template_name = 'tweet-list.html'

class CreateTweetView(CreateView):
    
    model = Tweet
    template_name = 'tweet-create.html'

    def get_success_url(self):
        return reverse('tweet-list')
