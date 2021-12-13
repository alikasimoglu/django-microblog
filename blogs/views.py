from itertools import chain
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
        return context
