from django.contrib import admin
from django.contrib.admin import TabularInline
from taggit.models import Tag

from .models import Comment, Post


class CommentInline(TabularInline):
    model = Comment
    fields = ['name', 'body', 'active']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status',]
    list_filter = ['status', 'created', 'publish', 'author',]
    search_fields = ['title', 'body',]
    date_hierarchy = 'publish'
    ordering = ['status', 'publish',]
    raw_id_fields = ['author',]
    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active',]
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body',]