from django.urls import path
from blogs.views import BlogPostListView, MyBlogListView, SubcribedBlogsListView


app_name = 'blogs'
urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogs'),
    path('<pk>/', MyBlogListView.as_view(), name='my-blog'),
    path('subscribed-blog-posts', SubcribedBlogsListView.as_view(), name='subscribed-blogs')
]
