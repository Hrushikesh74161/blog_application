from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/post/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 2


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post/blog_detail.html'
    context_object_name = 'post'