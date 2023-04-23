from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignupView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('home') #if sign up is successfull take user back to the homepage
    template_name = 'index.html'

