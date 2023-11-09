from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordResetView)
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import (ChangeProfileFieldsForm, ChangeUserFieldsForm,
                    ChangeUserProfilePicture, MyLoginForm,
                    MyPasswordChangeForm, MyPasswordResetForm,
                    MyUserCreationForm)
from .models import Profile, User


class SignUp(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    # If authenticated user requests 'login' url --> redirect to 'index'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('index'))
        return super().get(request, *args, **kwargs)


class Login(LoginView):
    form_class = MyLoginForm


class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm


class PasswordReset(PasswordResetView):
    form_class = MyPasswordResetForm


@login_required
def my_profile_view(request):
    user = request.user
    context = {'user': user}
    return render(request, 'users/my_profile_view.html', context)


@login_required
def change_user_profile_fields(request):
    profile = request.user.profile
    form = ChangeProfileFieldsForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('my_profile_view')
    context = {'form': form}
    return render(request, 'users/change_user_profile_fields.html', context)


@login_required
def change_user_fileds(request):
    user = request.user
    form = ChangeUserFieldsForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('my_profile_view')
    context = {'form': form}
    return render(request, 'users/change_user_fields.html', context)


@login_required
def change_user_profile_picture(request):
    profile = request.user.profile
    form = ChangeUserProfilePicture(request.POST or None, files=request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print(request.FILES)
            return redirect('my_profile_view')
    context = {'form': form}
    return render(request, 'users/change_user_profile_picture.html', context)
