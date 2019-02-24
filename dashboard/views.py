from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from website.models import Profile, Project, Image, Service
from theearthissquare import settings
from website.forms import *
from dashboard.functions import *
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core import serializers
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime
from django.forms.models import model_to_dict
import requests, json, logging, pygal

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            dashboardUpdated = updateSocialsDashboard()

        # Get Instagram Follower Count
        try:
            instagramFollowers = Setting.objects.get(name="SocialsDashboard.InstagramFollowers")
        except Settings.DoesNotExist:
            instagramFollowers = Setting.objects.create(name="SocialsDashboard.InstagramFollowers",value=0)

        totalInstagramLikes = StatsLog.objects.values_list('instagram_likes', flat=True).order_by('-date_created')
        igLikesDifference = (int(totalInstagramLikes[0]) - int(totalInstagramLikes[7]))

        totalInstagramFollowers = StatsLog.objects.values_list('instagram_followers', flat=True).order_by('-date_created')
        igFollowersDifference = (int(totalInstagramFollowers[0]) - int(totalInstagramFollowers[7]))

        totalFacebookFollowers = StatsLog.objects.values_list('facebook_likes', flat=True).order_by('-date_created')
        fbFollowersDifference = (int(totalFacebookFollowers[0]) - int(totalFacebookFollowers[7]))

        # Get Facebook Follower Count
        try:
            facebookFollowers = Setting.objects.get(name="SocialsDashboard.FacebookFollowers")
        except Settings.DoesNotExist:
            facebookFollowers = Setting.objects.create(name="SocialsDashboard.FacebookFollowers",value=0)

        try:
            lastUpdate = Setting.objects.get(name="SocialsDashboard.LastUpdate")
        except Settings.DoesNotExist:
            lastUpdate = Setting.objects.create(name="SocialsDashboard.LastUpdate",value=datetime.now())

        return render(request, 'dashboard.html', {
        'instagramFollowers' : instagramFollowers.value,
        'instagramLikes' : totalInstagramLikes[0],
        'instagramPosts' : InstagramPost.objects.all().order_by('-date_published'),
        'facebookFollowers' : facebookFollowers.value,
        'lastUpdate' : datetime.strptime(lastUpdate.value, '%Y-%m-%d %H:%M:%S.%f'),
        'igLikesDifference': igLikesDifference,
        'igFollowersDifference': igFollowersDifference,
        'fbFollowersDifference': fbFollowersDifference
        })

def dashboard_data(request,type):
    if type == 'instagramLikes':
        chart = instagramLikesChart()
    elif type == 'instagramFollowers':
        chart = instagramFollowersChart()

    return JsonResponse(chart)
