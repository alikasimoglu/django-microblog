from django.urls import path
from profiles.views import ProfileListView, ProfileDetailView, profile_subscribe_button


app_name = 'profiles'
urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles'),
    path('change_subscribe', profile_subscribe_button, name='profile_subscribe'),
    path('<pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
