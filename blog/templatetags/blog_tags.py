from django import template

from blog.models import Post

register = template.Library()


@register.simple_tag(name='total_no_of_posts')
def total_posts():
    return Post.published.count()