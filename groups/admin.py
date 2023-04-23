from django.contrib import admin
from . import models

# Register your models here.

#Group model:
admin.site.register(models.Group) #basic registration of a model in admin

#GroupMember model:
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember
#Group behaves as kind of a parent for GroupMember, 
#but with the TabularInLine class we can see the members of a group in admin if we clik on the group
#no need for further registering here the GroupMember model


