from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "first_name","last_name", "password1", "password2")
        model = get_user_model()
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':"Username"}),
            'first_name': forms.TextInput(attrs={'placeholder':"First Name"}),
            'last_name': forms.TextInput(attrs={'placeholder':"Last Name"}),
            # 'password1': forms.PasswordInput(attrs={'placeholder':"Password"}),
            # 'password2': forms.PasswordInput(attrs={'placeholder':"Confirm Password"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ""
        self.fields["first_name"].label = ""
        self.fields["last_name"].label = ""
        self.fields["password1"].placeholder = "Password"
        self.fields["password2"].placeholder = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""
        self.fields["username"].help_text = "please exclude @iitg.ernet.in or @iitg.ac.in"
