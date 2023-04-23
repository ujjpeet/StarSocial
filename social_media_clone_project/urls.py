from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path("admin/", admin.site.urls),
    #include the paths setup in accounts, groups and posts apps:
    path("accounts/", include('accounts.urls', namespace='accounts')),
    path("accounts/", include('django.contrib.auth.urls')),
    path("groups/", include('groups.urls', namespace='groups')),
    path("posts/", include('posts.urls', namespace='posts')),    
]

if settings.DEBUG:
    import debug_toolbar
    #redefine urlpatterns
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))
    ] + urlpatterns #adding the other urls defined above