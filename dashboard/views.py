from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from website.models import Profile, Project, Image, Service
from theearthissquare import settings
from website.forms import *
from dashboard.functions import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime
import requests, json, logging

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'dashboard.html', {
        'instagramFollowers' : getConfigValue('InstagramFollowers'),
        'instagramLikes' : getConfigValue('InstagramLikes'),
        'instagramPosts' : InstagramPost.objects.all().order_by('-date_published'),
        'facebookFollowers' : getConfigValue('FacebookFollowers'),
        'igLikesDifference': getDifference('instagram_likes'),
        'igFollowersDifference': getDifference('instagram_followers'),
        'fbFollowersDifference': getDifference('facebook_likes', getConfigValue('FacebookFollowers'))
        })

def dashboard_instagram(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'dashboard_instagram.html', {
        'instagramFollowers' : getConfigValue('InstagramFollowers'),
        'instagramLikes' : getConfigValue('InstagramLikes'),
        'instagramPosts' : InstagramPost.objects.all().order_by('-date_published'),
        'igLikesDifference': getDifference('instagram_likes'),
        'igFollowersDifference': getDifference('instagram_followers'),
        })

def dashboard_data(request,type,seriesName='Value'):
    chart = getChart(type,seriesName)
    return JsonResponse(chart)
