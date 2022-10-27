from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .forms import CommentForm, EmailPostForm
from .models import Comment, Post


class BlogListView(ListView):
    queryset = Post.published.all()
    template_name = 'blog/post/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 2


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        comment_data = CommentForm(request.POST)
        if comment_data.is_valid():
            cd = comment_data.cleaned_data
            comment = Comment.objects.create(
                post = post,
                **cd)
            comment.save()

    form = CommentForm()

    return render(request, 'blog/post/blog_detail.html', {'post': post, 'form': form})


def post_share(request, pk):
    # retrive post by id
    post = get_object_or_404(Post, id=pk, status='published')
    sent = False
    if request.method == 'POST':
        # form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}"
            send_mail(subject, message, 'admin@email.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
        
    return render(request, 'blog/post/post_share.html', {'post': post, 'form': form, 'sent': sent})