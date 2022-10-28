from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class Testing_tagged_items(TestCase):
    def test_tagged_posts(self):
        print(reverse('blog:blog_list'))