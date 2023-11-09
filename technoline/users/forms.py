from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       PasswordResetForm, UserCreationForm)

from .models import Profile

User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


# form for change(update) user.profile fields
class ChangeProfileFieldsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChangeProfileFieldsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ('phone', 'address')


# form for change(update) user fields
class ChangeUserFieldsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChangeUserFieldsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


# custom widget for image upload
class ProfilePictureFileInput(forms.ClearableFileInput):
    template_name = 'users/form_widgets/image_file_input_form.html'


# form for cahnge(avatar) user.profile profile_picture
class ChangeUserProfilePicture(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture',)
        widgets = {
            'profile_picture': ProfilePictureFileInput,
        }
