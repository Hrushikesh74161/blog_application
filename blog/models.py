from django.urls import reverse
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_querset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # default manager
    published = PublishedManager()  # our custom manager

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[str(self.pk)])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title