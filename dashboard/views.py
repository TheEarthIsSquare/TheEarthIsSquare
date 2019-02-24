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

        # Get All Likes Across All Posts
        allPostLikes = InstagramPost.objects.all().values_list('like_count', flat=True)
        instagramLikes = 0
        for mediaLikes in allPostLikes:
            instagramLikes = instagramLikes + mediaLikes

        # Get Facebook Follower Count
        try:
            facebookFollowers = Setting.objects.get(name="SocialsDashboard.FacebookFollowers")
        except Settings.DoesNotExist:
            facebookFollowers = Setting.objects.create(name="SocialsDashboard.FacebookFollowers",value=0)

        try:
            lastUpdate = Setting.objects.get(name="SocialsDashboard.LastUpdate")
        except Settings.DoesNotExist:
            lastUpdate = Setting.objects.create(name="SocialsDashboard.LastUpdate",value=datetime.now())

        instagramLikesGraph = GenerateInstagramLikesGraph()

        instagramFollowersGraph = GenerateInstagramFollowersGraph()

        return render(request, 'dashboard.html', {
        'instagramFollowers' : instagramFollowers.value,
        'instagramLikes' : instagramLikes,
        'instagramPosts' : InstagramPost.objects.all().order_by('-date_published'),
        'facebookFollowers' : facebookFollowers.value,
        'lastUpdate' : datetime.strptime(lastUpdate.value, '%Y-%m-%d %H:%M:%S.%f'),
        'instagramLikesGraph' : instagramLikesGraph,
        'instagramFollowersGraph' : instagramFollowersGraph
        })

def dashboard_data(request):
    count = StatsLog.objects.all().count()
    if count > 56:
        count = 56
    dataset = StatsLog.objects \
        .values('instagram_likes', 'date_created') \
        .order_by('-date_created') \
        [:count:8] \

    dataset.reverse()

    chart = {
        'chart': {
        'type': 'line',
        'backgroundColor': 'transparent'
        },
        'title': {'text': ''},
        'credits': {'enabled': False},
        'series': [{
            'name': 'Total Likes',
            'data': list(map(lambda row: {'name': row['date_created'].strftime("%B %d, %Y"), 'y': int(row['instagram_likes'])}, dataset))
        }]
    }

    return JsonResponse(chart)
