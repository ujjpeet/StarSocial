from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from groups.models import Group,GroupMember
from . import models

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description") #when someone creates a group only the name and description fields are editable
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            #create membership:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, you are already a member of {} group".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:
            #check whether user is a membor of the group:
            membership = models.GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get("slug")).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, "You can't leave this group because you are not a member.")

        else:
            membership.delete()
            messages.success(self.request, "You have successfully left this group.")

        return super().get(request, *args, **kwargs)