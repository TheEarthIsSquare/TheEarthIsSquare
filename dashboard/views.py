from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from website.models import Profile, Project, Image, Service
from theearthissquare import settings
from website.forms import *
from dashboard.functions import *
from django.template.loader import get_template
from django.core.mail import send_mail
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
import requests, json, logging

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            dashboardUpdated = updateSocialsDashboard()

        # Get Instagram Follower Count
        try:
            instagramFollowers = Settings.objects.get(name="SocialsDashboard.InstagramFollowers")
        except Settings.DoesNotExist:
            instagramFollowers = Settings.objects.create(name="SocialsDashboard.InstagramFollowers",value=0)

        # Get All Likes Across All Posts
        allPostLikes = InstagramPost.objects.all().values_list('like_count', flat=True)
        instagramLikes = 0
        for mediaLikes in allPostLikes:
            instagramLikes = instagramLikes + mediaLikes

        # Get Facebook Follower Count
        try:
            facebookFollowers = Settings.objects.get(name="SocialsDashboard.FacebookFollowers")
        except Settings.DoesNotExist:
            facebookFollowers = Settings.objects.create(name="SocialsDashboard.FacebookFollowers",value=0)

        try:
            lastUpdate = Settings.objects.get(name="SocialsDashboard.LastUpdate")
        except Settings.DoesNotExist:
            lastUpdate = Settings.objects.create(name="SocialsDashboard.LastUpdate",value=datetime.now())


        return render(request, 'dashboard.html', {
        'instagramFollowers' : instagramFollowers.value,
        'instagramLikes' : instagramLikes,
        'instagramPosts' : InstagramPost.objects.all().order_by('-date_published'),
        'facebookFollowers' : facebookFollowers.value,
        'lastUpdate' : datetime.strptime(lastUpdate.value, '%Y-%m-%d %H:%M:%S.%f'),
        })
