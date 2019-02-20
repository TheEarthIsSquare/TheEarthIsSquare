from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from website.models import Profile, Project, Image, Service, InstagramPost, Settings
from theearthissquare import settings
from website.forms import *
from website.functions import *
from django.db import connection
import requests, json, logging
from datetime import datetime


def getFBPageInfo():
    graphSettings = graphAPI();
    url = 'https://graph.facebook.com/' + graphSettings['teis_facebook_id'] + '?fields=connected_instagram_account,fan_count&access_token=' + graphSettings['access_token']
    response = requests.get(url).json()
    dump = json.dumps(response)
    loadJson = json.loads(dump)
    error = loadJson.get('error')
    if error != None:
        print('There has been an error when attempting to get Facebook Page Info ' + error['message'])
        print(error)
        return loadJson
    else:
        print(loadJson)
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
        instagramFollowers = Settings.objects.get(name="SocialsDashboard.InstagramFollowers")
    except Settings.DoesNotExist:
        instagramFollowers = None

    if instagramFollowers == None:
        instagramFollowers = Settings.objects.create(name="SocialsDashboard.InstagramFollowers",value=loadJson['followers_count'])
    else:
        instagramFollowers.value = loadJson['followers_count']
        instagramFollowers.save()

    try:
        facebookFollowers = Settings.objects.get(name="SocialsDashboard.FacebookFollowers")
    except Settings.DoesNotExist:
        facebookFollowers = None

    if facebookFollowers == None:
        facebookFollowers = Settings.objects.create(name="SocialsDashboard.FacebookFollowers",value=getFBPageInfo().get('fan_count'))
    else:
        facebookFollowers.value = getFBPageInfo().get('fan_count')
        facebookFollowers.save()

    try:
        lastUpdate = Settings.objects.get(name="SocialsDashboard.LastUpdate")
    except Settings.DoesNotExist:
        lastUpdate = None

    if lastUpdate == None:
        lastUpdate = Settings.objects.create(name="SocialsDashboard.LastUpdate",value=datetime.now())
    else:
        lastUpdate.value = datetime.now()
        lastUpdate.save()

    Success = True
    return Success
