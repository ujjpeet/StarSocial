from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin #restrict actions to logged in users
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin #braces needs to be installed from command line with the command: pip install django-braces
from . import forms
from . import models

#user object, needed to knwo the currently logged in user:
from django.contrib.auth import get_user_model
User = get_user_model()

#all posts
class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user", "group") #foreign keys for the posts

#posts for the logged in user
class UserPosts(generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"

    #method to fetch all posts of a user:
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

#post details
class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "group") #foreign keys for a post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

#create new post
class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('message','group')
    model = models.Post

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False) #do not commit the form to DB
        self.object.user = self.request.user #modify user, connecting post to user
        self.object.save() #save data into DB now
        return super().form_valid(form)

#delete post
class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post deleted")
        return super().delete(*args, **kwargs)