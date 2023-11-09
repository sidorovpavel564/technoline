from django.urls import path
from . import views

urlpatterns = [
    path('auth/signup/', views.SignUp.as_view(), name='signup'),
    path('auth/login/', views.Login.as_view(redirect_authenticated_user=True), name='login'),
    path('auth/password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('auth/password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('profile', views.my_profile_view, name='my_profile_view'),
    path('profile/change_user_profile_fields', views.change_user_profile_fields, name='change_user_profile_fields'),
    path('profile/change_user_fields', views.change_user_fileds, name='change_user_fields'),
    path('profile/cahnge_user_profile_picture', views.change_user_profile_picture, name='change_user_profile_picture'),
]
