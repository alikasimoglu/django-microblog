from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from blogs.models import BlogPost
from .models import Profile


class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/index.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"
    context_object_name = "profile"

    def get_object(self, **kwargs):
        pk = self.kwargs.get("pk")
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)
        if view_profile.user in my_profile.subscribed.all():
            subscribe = True
        else:
            subscribe = False
        context["subscribe"] = subscribe
        context["profile_posts"] = BlogPost.objects.filter(author__user=view_profile.user)
        return context


def profile_subscribe_button(request):
    if request.method == "POST":
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get("profile_pk")
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.subscribed.all():
            my_profile.subscribed.remove(obj.user)
        else:
            my_profile.subscribed.add(obj.user)
        return redirect(request.META.get("HTTP_REFERER"))
    return redirect("profiles:profile-detail")
