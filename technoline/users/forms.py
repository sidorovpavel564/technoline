from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms

User = get_user_model()

class CreationForm(UserCreationForm):
    """
    password1 and password2 are "custom" fields on the UserCreationForm since 
    they do not exist as model fields on the User model. Meta.widgets will not 
    work for these custom fields, you will need to redefine these fields and
    their widgets in your form
    """
    error_messages = {
        "password_mismatch": ("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password"}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', "autofocus": True}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "current-password"}),
    )
