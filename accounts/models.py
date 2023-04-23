from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    pass #if class is empty yet, pass keyword is needed to avoid syntax error