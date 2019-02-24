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


def getFBPageInfo():
    graphSettings = graphAPI();
    url = 'https://graph.facebook.com/' + graphSettings['teis_facebook_id'] + '?fields=connected_instagram_account,fan_count&access_token=' + graphSettings['access_token']
    response = requests.get(url).json()
    dump = json.dumps(response)
    loadJson = json.loads(dump)
    error = loadJson.get('error')
    if error != None:
        print('There has been an error when attempting to get Facebook Page Info ' + error['message'])
        return loadJson
    else:
        return loadJson

def graphAPI():
    values = {
        'access_token' : settings.FACEBOOK_GRAPH_API_ACCESS_KEY,
        'teis_facebook_id' : '380002269441497',
        }
    return values

def updateSocialsDashboard(success=False):
    graphSettings = graphAPI();
    instagram = getFBPageInfo().get('connected_instagram_account')
    url = 'https://graph.facebook.com/' + instagram['id'] + '?fields=media{media_url,comments_count,id,like_count,timestamp,caption},followers_count&access_token=' + graphSettings['access_token']
    response = requests.get(url).json()
    dump = json.dumps(response)
    loadJson = json.loads(dump)
    error = loadJson.get('error')
    if error != None:
        print('Error - updateInstagramDatabase: ' + error['message'])
        return loadJson
    else:
        mediaList = []
        for media in loadJson['media']['data']:
            mediaList.append(media)
        databaseQueryList = InstagramPost.objects.all()
        databasePostList = [media for media in databaseQueryList]
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

    try:
        instagramFollowers = Setting.objects.get(name="SocialsDashboard.InstagramFollowers")
    except Settings.DoesNotExist:
        instagramFollowers = None

    if instagramFollowers == None:
        instagramFollowers = Setting.objects.create(name="SocialsDashboard.InstagramFollowers",value=loadJson['followers_count'])
    else:
        instagramFollowers.value = loadJson['followers_count']
        instagramFollowers.save()

    try:
        facebookFollowers = Setting.objects.get(name="SocialsDashboard.FacebookFollowers")
    except Settings.DoesNotExist:
        facebookFollowers = None

    if facebookFollowers == None:
        facebookFollowers = Settings.objects.create(name="SocialsDashboard.FacebookFollowers",value=getFBPageInfo().get('fan_count'))
    else:
        facebookFollowers.value = getFBPageInfo().get('fan_count')
        facebookFollowers.save()

    try:
        lastUpdate = Setting.objects.get(name="SocialsDashboard.LastUpdate")
    except Settings.DoesNotExist:
        lastUpdate = None

    if lastUpdate == None:
        lastUpdate = Setting.objects.create(name="SocialsDashboard.LastUpdate",value=datetime.now())
    else:
        lastUpdate.value = datetime.now()
        lastUpdate.save()

    Success = True
    return Success

def createStatsLog():
    try:
        facebookFollowers = Setting.objects.get(name="SocialsDashboard.FacebookFollowers")
    except Settings.DoesNotExist:
        return None

    try:
        instagramFollowers = Setting.objects.get(name="SocialsDashboard.InstagramFollowers")
    except Settings.DoesNotExist:
        return None

    allPostLikes = InstagramPost.objects.all().values_list('like_count', flat=True)
    instagramLikes = 0
    for mediaLikes in allPostLikes:
        instagramLikes = instagramLikes + mediaLikes

    newLog = StatsLog.objects.create(instagram_likes=instagramLikes,instagram_followers=instagramFollowers.value,instagram_posts=InstagramPost.objects.all().count(),facebook_likes=facebookFollowers.value)

    return None

def instagramLikesChart():
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
                'text': '# of Total Likes',
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
            'name': 'Total Likes',
            'data': list(map(lambda row: {'name': row['date_created'].strftime("%B %d, %Y"), 'y': int(row['instagram_likes'])}, dataset))
        }]
    }
    return chart

def instagramFollowersChart():
    count = StatsLog.objects.all().count()
    if count > 56:
        count = 56
    dataset = StatsLog.objects \
        .values('instagram_followers', 'date_created') \
        .order_by('-date_created') \
        [:count:8] \

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
                'text': '# of Total Followers',
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
            'name': 'Total Followers',
            'data': list(map(lambda row: {'name': row['date_created'].strftime("%B %d, %Y"), 'y': int(row['instagram_followers'])}, dataset))
        }]
    }
    return chart
