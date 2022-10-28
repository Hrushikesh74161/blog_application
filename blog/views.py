from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from taggit.models import Tag

from .forms import CommentForm, EmailPostForm
from .models import Comment, Post


def post_list(request):
    obj_list = Post.published.all()
    paginator = Paginator(obj_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page no is not a integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page no is out of range deliver last page
        posts = paginator.page(paginator.num_pages)
    tag = 0  # all items not tagged, see posts_with_tag function and blog_list.html file
    return render(request, 'blog/post/blog_list.html', {'posts': posts, 'tag': tag, 'page': page})


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


def posts_with_tag(request, tag_id):
    tag_item = Tag.objects.get(id=tag_id)
    obj_list = Post.objects.filter(tags=tag_item)
    paginator = Paginator(obj_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page no is not a integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page no is out of range deliver last page
        posts = paginator.page(paginator.num_pages)
    tag = 1  # tagged items
    return render(request, 'blog/post/blog_list.html', {'posts': posts, 'tag_item': tag_item, 'tag': tag})