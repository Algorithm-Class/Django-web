from django import forms

from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
  user = forms.CharField(label='Your name',max_length = 100)
  password = forms.CharField(widget = forms.PasswordInput())

  def clean_password(self):
        passwd = self.cleaned_data['password']
        if( passwd != 'welcome'):
            raise ValidationError('Invalid password')

        # Remember to always return the cleaned data.
        return passwd

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    def clean_your_name(self):
        user = self.cleaned_data['your_name']
        if( user != 'sboda'):
            raise ValidationError('Invalid user name')

        # Remember to always return the cleaned data.
        return user
