# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from votos.models import Voto
from votos.models import User

import forms

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class ListVotosView(ListView):

    model = Voto
    template_name = 'votos.html'

class ListUsersView(LoggedInMixin, ListView):

    model = User
    template_name = 'users.html'

    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        # http://django-rest-framework.org/api-guide/filtering
        return queryset.filter(owner=request.user)

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

class EditUserVotoView(UpdateView):

    model = User
    template_name = 'edit-votos.html'
    form_class = forms.UserVotoFormSet

    def get_success_url(self):

        # redirect to the User view.
        return self.get_object().get_absolute_url()

