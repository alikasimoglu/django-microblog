from django.views.generic import ListView
from .models import Profile


class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/index.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)
