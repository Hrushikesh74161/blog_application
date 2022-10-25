from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = 'blog'


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<uuid:pk>', BlogDetailView.as_view(), name='blog_detail'),
]