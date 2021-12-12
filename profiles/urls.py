from django.urls import path
from profiles.views import ProfileListView

app_name = 'profiles'
urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles'),
]
