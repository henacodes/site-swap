from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CreateUserForm(UserCreationForm):
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-700'})
    )

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'name', 'class': 'w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-700'}),
            'username': forms.TextInput(attrs={'placeholder':'username','class': 'w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-700'}),
            'email': forms.EmailInput(attrs={'placeholder':'email','class': 'w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-700'}),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'password', 'class': 'w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-700'})
        self.fields['password2'].widget.attrs.update({'placeholder':'confirm password', 'class': 'w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-700'})

    def clean_password2(self):
        password = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2