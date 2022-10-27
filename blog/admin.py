from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status',]
    list_filter = ['status', 'created', 'publish', 'author',]
    search_fields = ['title', 'body',]
    date_hierarchy = 'publish'
    ordering = ['status', 'publish',]
    raw_id_fields = ['author',]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active',]
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body',]