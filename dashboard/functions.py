from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from website.models import Profile, Project, Image, Service, InstagramPost, Setting
from dashboard.models import StatsLog
from theearthissquare import settings
from website.forms import *
from django.db import connection
from datetime import datetime
from django.templatetags.static import static
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests, json, logging

def updateSocialsDashboard(success=False):
    graphSettings = graphAPI();
    instagram = getFBPageInfo().get('connected_instagram_account')
    response = requests.get('https://graph.facebook.com/' + instagram['id'] + '?fields=media{media_url,comments_count,id,like_count,timestamp,caption},followers_count&access_token=' + graphSettings['access_token'])
    jsonData = response.json()

    mediaList = []
    for media in jsonData['media']['data']:
        mediaList.append(media)
    allInstagramPosts = InstagramPost.objects.all()
    totalLikes = 0
    for post in allInstagramPosts:
        totalLikes += post.like_count
    databasePostList = [media for media in allInstagramPosts]
    databasePostIdList = InstagramPost.objects.all().values_list('instagram_id', flat=True)
    for media in mediaList:
        if media['id'] not in databasePostIdList:
            instagram_id = media['id']
            image_url = media['media_url']
            like_count = media['like_count']
            comment_count = media['comments_count']
            caption = media['caption']
            date_published = media['timestamp']
            addNewPost = InstagramPost(instagram_id=instagram_id,image_url=image_url,like_count=like_count,comment_count = comment_count,caption=caption,date_published=date_published)
            addNewPost.save()
        else:
            for post in databasePostList:
                if post.instagram_id == media['id']:
                    post.like_count = media['like_count']
                    post.comment_count = media['comments_count']
                    post.caption = media['caption']
                    post.save()

    instagramFollowers = getConfigValue('InstagramFollowers',False)
    instagramFollowers.value = jsonData['followers_count']
    instagramFollowers.save()

    facebookFollowers = getConfigValue('FacebookFollowers',False)
    facebookFollowers.value = getFBPageInfo().get('fan_count')
    facebookFollowers.save()

    lastUpdate = getConfigValue('LastUpdate',False)
    lastUpdate.value = datetime.now()
    lastUpdate.save()

    instagramLikes = getConfigValue('InstagramLikes',False)
    instagramLikes.value = totalLikes
    instagramLikes.save()

    return True

def createStatsLog():
    facebookFollowers = getConfigValue('FacebookFollowers')
    instagramFollowers = getConfigValue('InstagramFollowers')
    instagramLikes = getConfigValue('InstagramLikes')

    newLog = StatsLog.objects.create(instagram_likes=instagramLikes,instagram_followers=instagramFollowers.value,instagram_posts=InstagramPost.objects.all().count(),facebook_likes=facebookFollowers.value)

    return None

def getChart(type,seriesName):
    count = StatsLog.objects.all().order_by('-date_created')[:56].count()

    print(type)

    dataset = StatsLog.objects \
        .values(type, 'date_created') \
        .order_by('-date_created') \
        [:count:8]

    dataset.reverse()

    chart = {
        'chart': {
            'type': 'line',
            'backgroundColor': 'transparent',
        },
        'title': {
            'text': ''
        },
        'colors': ['#2B59C3'],
        'credits': {
            'enabled': False
        },
        'xAxis': {
            'title': {
                'enabled': True,
                'text': 'Days Ago',
                'style': {
                    'color': '#2B59C3'
                }
            },
            'categories': [7, 6, 5, 4, 3, 2, 1],
            'labels': {
                'style': {
                    'color': '#2B59C3'
                }
            }
        },
        'yAxis': {
            'title': {
                'enabled': False,
            },
            'labels': {
                'style': {
                    'color': '#2B59C3'
                }
            }
        },
        'legend': {
            'enabled': False
        },
        'series': [{
            'name': seriesName,
            'data': list(map(lambda row: {'name': row['date_created'].strftime("%B %d, %Y"), 'y': int(row[type])}, dataset))
        }]
    }
    return chart

def getConfigValue(option,value=True):
    try:
        config = Setting.objects.get(name="SocialsDashboard." + option)
    except Setting.DoesNotExist:
        config = Setting.objects.create(name="SocialsDashboard." + option,value='')

    if value == True:
        return config.value
    else:
        return config

def getDifference(type,extra=''):
    objects = StatsLog.objects.values_list(type, flat=True).order_by('-date_created')
    if extra == '':
        difference = (int(objects[0]) - int(objects[7]))
    else:
        difference = (int(extra) - int(objects[7]))

    return difference

def getFBPageInfo():
    graphSettings = graphAPI();
    response = requests.get('https://graph.facebook.com/' + graphSettings['teis_facebook_id'] + '?fields=connected_instagram_account,fan_count&access_token=' + graphSettings['access_token'])
    data = response.json()
    return data

def graphAPI():
    values = {
        'access_token' : settings.FACEBOOK_GRAPH_API_ACCESS_KEY,
        'teis_facebook_id' : '380002269441497',
        }
    return values
