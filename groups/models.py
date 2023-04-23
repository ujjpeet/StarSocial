from django.db import models
from django.utils.text import slugify #creates lowercase/removes space for URLs

#get the logged in user:
from django.contrib.auth import get_user_model 
User = get_user_model()

from django import template
register = template.Library()

from django.conf import settings
from django.urls import reverse

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True) #url
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = 'description'
        super().save(*args, **kwargs)

    #method to get the url for every group using slug:
    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="memberships") #group attribute is reated to Group class
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_groups') #user attribute is related to User

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")