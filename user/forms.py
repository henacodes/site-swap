from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

INPUT_CLASS = "w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-700"

class CreateUserForm(UserCreationForm):
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': INPUT_CLASS})
    )

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'name', 'class': INPUT_CLASS}),
            'username': forms.TextInput(attrs={'placeholder':'username','class': INPUT_CLASS}),
            'email': forms.EmailInput(attrs={'placeholder':'email','class': INPUT_CLASS}),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'password', 'class': INPUT_CLASS})
        self.fields['password2'].widget.attrs.update({'placeholder':'confirm password', 'class': INPUT_CLASS})

    def clean_password2(self):
        password = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2
    





class UserAuthenticateForm(AuthenticationForm):
    class Meta:
        model = User  # Replace "User" with the name of your custom user model
        ##fields = ['username', 'password']  # Fields to include in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize form fields if needed
        #self.fields['email'].widget.attrs.update({'class':INPUT_CLASS,'placeholder': 'Email'})
        #self.fields['password'].widget.attrs.update({'class':INPUT_CLASS,'placeholder': 'Password'})

        ##for  field in self.fields:
        ##    field.widget.attrs.update({'class':INPUT_CLASS,'placeholder': 'Email'})
        
