from django import forms
from users.models import User
from django.contrib.auth.forms import  UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from crispy_forms.bootstrap import AppendedText, PrependedText


class UserSignUpForm(UserCreationForm):

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        for field_name in self.fields:
            field = self.fields.get(field_name)
            # field.widget.attrs['placeholder'] += field.label
            field.label = ''

        self.helper.layout = Layout(

             Div(
                PrependedText('username', '<i class="ni ni-hat-3"></i>', placeholder="username"),
                css_class='form-group',
                ),
            Div(
                PrependedText('email', '<i class="ni ni-email-83"></i>', placeholder="email"),
                css_class='form-group',
               ),
            Div(
                PrependedText('password1', '<i class="ni ni-lock-circle-open"></i>', placeholder="password"),
                css_class='form-group',
               ),
            Div(
                PrependedText('password2', '<i class="ni ni-lock-circle-open"></i>', placeholder="confirm password"),
                css_class='form-group',
               ),
            Div(
                Submit('submit', 'Create account', css_class='btn btn-primary mt-4'),
                css_class='text-center'
            )
        )

    class Meta:

        model = User
        fields = ('username', 'email', 'password1', 'password2')
