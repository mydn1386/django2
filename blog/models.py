from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', "Draft"),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique_for_date='published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    caption = models.TextField(max_length=10000)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    music_file = models.FileField(upload_to='music/', blank=True, null=True)
    image_file = models.FileField(upload_to='image/', blank=True, null=True)
    singer = models.CharField(max_length=10, blank=True, null=True)
    sub = models.TextField(max_length=1000000, blank=True, null=True)

    class Meta:
        ordering = ('-published',)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug, self.id])

    def __str__(self):
        return self.title


class Account(models.Model):
    GENDER_CHOICES = (
        ('آقا', "آقا"),
        ('خانم', 'خانم'),
    )
    phone = models.CharField(max_length=11, default='',)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, default='خانم')
    address = models.TextField(blank=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    birth = models.CharField(max_length=10,)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
