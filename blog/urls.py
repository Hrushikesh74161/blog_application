from django.urls import path

from .views import BlogListView, post_detail, post_share

app_name = 'blog'


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<uuid:pk>', post_detail, name='blog_detail'),  # type: ignore
    path('<uuid:pk>/share/', post_share, name='post_share'),
]