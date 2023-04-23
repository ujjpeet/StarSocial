from django.urls import path
from . import views

app_name = 'groups'

# urlpatterns = [
#     path(r"^$", views.ListGroups.as_view(), name="all"), #url is /groups
#     path(r"^new/$", views.CreateGroup.as_view(), name="create"),
#     path(r"^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"), #?P<slug> = slugifying the group name
#     path(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
#     path(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
# ]

urlpatterns = [
    path("", views.ListGroups.as_view(), name="all"), #url is /groups
    path("new/", views.CreateGroup.as_view(), name="create"),
    path("posts/in/<slug>/",views.SingleGroup.as_view(),name="single"), #?P<slug> = slugifying the group name
    path("join/<slug>/",views.JoinGroup.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveGroup.as_view(),name="leave"),
]