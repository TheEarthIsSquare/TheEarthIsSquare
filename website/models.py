from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from s3direct.fields import S3DirectField
from tinymce.models import HTMLField

class Profile(models.Model):
    # def image_tag(self):
    #    return u'<img src="%s" />' % {{ self.avatar.url }}
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True

    avatar = S3DirectField(dest='profiles')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    twitter_username = models.CharField(max_length=255, null=True, blank=True)
    instagram_username = models.CharField(max_length=255, null=True, blank=True)
    linkedin_username = models.CharField(max_length=255, null=True, blank=True)

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = HTMLField(null=True, blank=True)
    image = S3DirectField(dest='services', null=True, blank=True)
    enabled = models.BooleanField(default=False)
    parent = models.BooleanField(default=False)
    package = models.BooleanField(default=False)
    parent_service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'parent': True})
    fa_icon = models.CharField(max_length=20, null=True, blank=True, default='fas')

    def __str__(self):
        return self.name

    def parsed_name(self):
        name = self.name.lower().replace('&amp;', '_')
        name = self.name.lower().replace('&', '_')
        return name.replace(' ', '_')

class Project(models.Model):

    type = models.ForeignKey(Service, on_delete=models.DO_NOTHING, null=True, blank=True, limit_choices_to={'parent': False})
    client = models.CharField(max_length=255)
    ongoing = models.BooleanField(default=False)
    date_completed = models.DateField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    tesimonial = HTMLField(null=True, blank=True)
    client_website = models.CharField(max_length=255, null=True, blank=True)
    avatar = S3DirectField(dest='projects', null=True, blank=True)
    banner = S3DirectField(dest='projects', null=True, blank=True)

    def parsed_client(self):
        return self.client.lower().replace(' ', '_')

    def date(self):
        if self.ongoing == True:
            return 'Ongoing'
        else:
            return self.date_completed

class Image(models.Model):
    image = S3DirectField(dest='projects', null=True)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
