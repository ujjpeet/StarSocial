from django.urls import path
from django.contrib.auth import views as auth_views #import Django buil-in authorization views for login/logout
from . import views #import the custom views set in accounts/views.py

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'), #logout redirects to home page
    path('signup/', views.SignupView.as_view(template_name='accounts/signup.html'), name='signup'),
]

