# Create your views here.
from django.views.generic import ListView

from votos.models import Voto
from votos.models import User


class ListVotosView(ListView):

    model = Voto
    template_name = 'votos.html'

class ListUsersView(ListView):

    model = User
    template_name = 'users.html'
