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
    context_object_name = "subcribedblogposts"
    ordering = "-created"

    def get_queryset(self):
        return BlogPost.objects.filter(author__user=self.request.user)
