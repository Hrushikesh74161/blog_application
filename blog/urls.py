from django.urls import path

from .feeds import LatestPostsFeed
from .views import post_detail, post_list, post_share, posts_with_tag

app_name = 'blog'


urlpatterns = [
    path('', post_list, name='blog_list'),
    path('<uuid:pk>', post_detail, name='blog_detail'),  # type: ignore
    path('<uuid:pk>/share/', post_share, name='post_share'),
    path('tag/<int:tag_id>', posts_with_tag, name='tagged_posts'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]