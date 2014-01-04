from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory
from votos.models import User, Voto

class UserForm(forms.ModelForm):
    confirm_email = forms.EmailField(
        "Confirm email",
        required=True,
    )

    class Meta:
        model= User

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email
        return super(UserForm, self).__init__(*args, **kwargs)

    def clean(self):

        if (self.cleaned_data.get('email') != 
            self.cleaned_data.get('confirm_email')):
            raise ValidationError(
                "Email addresses must match."
            )

        return self.cleaned_data

# inlineformset_factory creates a Class from a parent model (User) to a child model (Voto)
UserVotoFormSet = inlineformset_factory(
    User,
    Voto,
)
