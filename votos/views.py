# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView

from votos.models import Voto
from votos.models import User


class ListVotosView(ListView):

    model = Voto
    template_name = 'votos.html'

class ListUsersView(ListView):

    model = User
    template_name = 'users.html'

class CreateUserView(CreateView):
    
    model = User
    template_name = 'edit-users.html'

    def get_success_url(self):
        return reverse('users')
