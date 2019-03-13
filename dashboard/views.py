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
        return render(request, 'dashboard/dashboard.html', {
        'instagramFollowers' : getConfigValue('InstagramFollowers'),
        'instagramLikes' : getConfigValue('InstagramLikes'),
        'instagramPosts' : InstagramPost.objects.all().order_by('-date_published'),
        'facebookFollowers' : getConfigValue('FacebookFollowers'),
        'igLikesDifference': getDifference('instagram_likes', getConfigValue('InstagramLikes')),
        'igFollowersDifference': getDifference('instagram_followers', getConfigValue('InstagramFollowers')),
        'fbFollowersDifference': getDifference('facebook_likes', getConfigValue('FacebookFollowers'))
        })

def dashboard_instagram(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'dashboard/dashboard_instagram.html', {
        'instagramFollowers' : getConfigValue('InstagramFollowers'),
        'instagramLikes' : getConfigValue('InstagramLikes'),
        'instagramPosts' : InstagramPost.objects.all().order_by('-date_published'),
        'igLikesDifference': getDifference('instagram_likes', getConfigValue('InstagramLikes')),
        'igFollowersDifference': getDifference('instagram_followers', getConfigValue('InstagramFollowers')),
        })

def dashboard_facebook(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'dashboard/dashboard_facebook.html', {
        'facebookFollowers' : getConfigValue('FacebookFollowers'),
        'fbFollowersDifference': getDifference('facebook_likes', getConfigValue('FacebookFollowers'))
        })

def dashboard_data(request,type,seriesName='Value'):
    chart = getChart(type,seriesName)
    return JsonResponse(chart)
