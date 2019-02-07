from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from s3direct.fields import S3DirectField


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    avatar = S3DirectField(dest='profiles')
    twitter_username = models.CharField(max_length=255, null=True, blank=True)
    instagram_username = models.CharField(max_length=255, null=True, blank=True)

class Project(models.Model):
    TYPE_CHOICES = (
        (1, 'Website'),
        (2, 'Design'),
        (3, 'Marketing'),
        (4, 'Social Media Campagin'),
    )

    name = models.CharField(max_length=255)
    type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
    )
    client = models.CharField(max_length=255)
    date_completed = models.DateField(default=datetime.now)
    description = models.TextField(null=True, blank=True)
    tesimonial = models.TextField(null=True, blank=True)
    main_image = S3DirectField(dest='projects', null=True)

class Image(models.Model):
    image = S3DirectField(dest='projects', null=True)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
