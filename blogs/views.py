from itertools import chain

from django.shortcuts import redirect
from django.views.generic import ListView
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
