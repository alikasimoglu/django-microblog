from itertools import chain
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
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


@receiver(post_save, sender=BlogPost)
def send_mail_to_subs(sender, instance, created, **kwargs):
    if created:
        send_mail(
            f'New Post',
            'Hi .... ',
            'testcod77@gmail.com',
            ["alikasimoglu@gmail.com"],
        )


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogs/post_create.html'
    fields = ["post_title", "post_content"]
    error_message = 'Error saving the post, check fields.'

    def get_success_url(self):
        return reverse("blogs:post-create")

    def form_valid(self, form):
        post_form = form.save(commit=False)
        user = Profile.objects.get(user=self.request.user)
        form.instance.author = user
        post_form.save()
        return super(BlogPostCreateView, self).form_valid(form)

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
