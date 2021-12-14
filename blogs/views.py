from itertools import chain

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from blogs.models import BlogPost
from profiles.models import Profile


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogs/index.html'
    context_object_name = "blogs"
    ordering = "-created"


class MyBlogListView(ListView):
    model = BlogPost
    template_name = 'blogs/my_blog.html'
    context_object_name = "myblog"
    ordering = "-created"

    def get_queryset(self):
        return BlogPost.objects.filter(author__user=self.request.user)


class SubcribedBlogsListView(ListView):
    model = BlogPost
    template_name = 'blogs/subcribed_blogs.html'
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        users = [user for user in profile.subscribed.all()]
        posts = []
        for u in users:
            p = Profile.objects.get(user=u)
            p_posts = p.blogpost_set.all()
            posts.append(p_posts)
            unpack = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
            context["posts"] = unpack
        readed = profile.readed.all()
        context["readed"] = readed
        return context


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogs/post_create.html'
    fields = ["author", "post_title", "post_content"]
    error_message = 'Error saving the post, check fields below.'

    def get_success_url(self):
        return reverse("blogs:post-create")

    def form_valid(self, form):
        post_form = form.save(commit=False)
        post_form.user = self.request.user
        post_form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


def mark_as_read_button(request):
    if request.method == "POST":
        my_profile = Profile.objects.get(user=request.user)
        post = request.POST.get("post_pk")
        obj = BlogPost.objects.get(pk=post)

        if obj in my_profile.readed.all():
            my_profile.readed.remove(obj)
        else:
            my_profile.readed.add(obj)
        return redirect(request.META.get("HTTP_REFERER"))
    return redirect("blogs:subscribed-blogs")
