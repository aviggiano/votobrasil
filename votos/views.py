# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from votos.models import Voto
from votos.models import User

import forms

class ListVotosView(ListView):

    model = Voto
    template_name = 'votos.html'

class ListUsersView(ListView):

    model = User
    template_name = 'users.html'

class CreateUserView(CreateView):
    
    model = User
    template_name = 'edit-users.html'
    form_class = forms.UserForm

    def get_success_url(self):
        return reverse('users')

    def get_context_data(self, **kwargs):

        context = super(CreateUserView, self).get_context_data(**kwargs)
        context['action'] = reverse('users-new')

        return context

class UpdateUserView(UpdateView):

    model = User
    template_name = 'edit-users.html'
    form_class = forms.UserForm

    def get_success_url(self):
        return reverse('users')
    
    def get_context_data(self, **kwargs):

        context = super(UpdateUserView, self).get_context_data(**kwargs)
        context['action'] = reverse('users-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class DeleteUserView(DeleteView):

    model = User
    template_name = 'delete-user.html'

    def get_success_url(self):
        return reverse('users')

class UserView(DetailView):

    model = User
    template_name = 'user.html'
