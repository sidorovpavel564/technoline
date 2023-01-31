from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm, LoginForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('index'))
        return super().get(request,*args,**kwargs)

class Login(LoginView):
    form_class = LoginForm
