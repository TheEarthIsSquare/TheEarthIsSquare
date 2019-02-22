from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from s3direct.fields import S3DirectField
from tinymce.models import HTMLField
from django.utils import timezone

class StatsLog(models.Model):
    instagram_followers = models.CharField(max_length=255)
    instagram_likes = models.CharField(max_length=255)
    instagram_posts = models.CharField(max_length=255)
    facebook_likes = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
