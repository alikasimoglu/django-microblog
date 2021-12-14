from django.urls import path
from blogs.views import BlogPostListView, MyBlogListView, SubcribedBlogsListView, mark_as_read_button, \
    BlogPostCreateView

app_name = 'blogs'
urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogs'),
    path('<pk>/', MyBlogListView.as_view(), name='my-blog'),
    path('subscribed-blog-posts', SubcribedBlogsListView.as_view(), name='subscribed-blogs'),
    path('change_readed', mark_as_read_button, name='mark_as_read'),
    path('post-create', BlogPostCreateView.as_view(), name='post-create'),
]
