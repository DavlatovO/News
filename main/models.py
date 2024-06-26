from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()
    banner_img = models.ImageField(upload_to='post-baner/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post-img/')


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to='post-vido/')
    video_url = models.URLField(blank=True, null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)