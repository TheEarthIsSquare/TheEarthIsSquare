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
from pygal.style import Style
import requests, json, logging, pygal


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

def GenerateInstagramLikesGraph():
    custom_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground='white',
        foreground_strong='white',
        foreground_subtle='white',
        opacity='.9',
        transition='400ms ease-in',
        label_font_size=20,
        major_label_font_size=25,
        font_family='googlefont:Raleway',
        colors=('#DCF763',))
    Instagram_Likes = pygal.Line(style=custom_style, fill=True, min_scale=1, show_legend=False)
    IGLikesGraphCount = StatsLog.objects.all().count()
    if IGLikesGraphCount >= 1:
        IGLikesGraphFirst = StatsLog.objects.latest('date_created')
        if IGLikesGraphCount < 8:
            Instagram_Likes.x_labels = map(str, range(1, 2))
            Instagram_Likes.add('', [
            int(IGLikesGraphFirst.instagram_likes)
            ])
        elif IGLikesGraphCount < 16:
            IGLikesGraphObjects = StatsLog.objects.all()[:8:8]
            Instagram_Likes.x_labels = map(str, range(1, 3))
            Instagram_Likes.add('', [
            int(IGLikesGraphObjects[0].instagram_likes),
            int(IGLikesGraphFirst.instagram_likes)
            ])
        elif IGLikesGraphCount < 24:
            IGLikesGraphObjects = StatsLog.objects.all()[:16:8]
            Instagram_Likes.x_labels = map(str, range(1, 4))
            Instagram_Likes.add('', [
            int(IGLikesGraphObjects[0].instagram_likes),
            int(IGLikesGraphObjects[1].instagram_likes),
            int(IGLikesGraphFirst.instagram_likes)
            ])
        elif IGLikesGraphCount < 32:
            IGLikesGraphObjects = StatsLog.objects.all()[:24:8]
            Instagram_Likes.x_labels = map(str, range(1, 5))
            Instagram_Likes.add('', [
            int(IGLikesGraphObjects[0].instagram_likes),
            int(IGLikesGraphObjects[1].instagram_likes),
            int(IGLikesGraphObjects[2].instagram_likes),
            int(IGLikesGraphFirst.instagram_likes)
            ])
        elif IGLikesGraphCount < 40:
            IGLikesGraphObjects = StatsLog.objects.all()[:32:8]
            Instagram_Likes.x_labels = map(str, range(1, 6))
            Instagram_Likes.add('', [
            int(IGLikesGraphObjects[0].instagram_likes),
            int(IGLikesGraphObjects[1].instagram_likes),
            int(IGLikesGraphObjects[2].instagram_likes),
            int(IGLikesGraphObjects[3].instagram_likes),
            int(IGLikesGraphFirst.instagram_likes)
            ])
        elif IGLikesGraphCount < 48:
            IGLikesGraphObjects = StatsLog.objects.all()[:48:8]
            Instagram_Likes.x_labels = map(str, range(1, 7))
            Instagram_Likes.add('', [
            int(IGLikesGraphObjects[0].instagram_likes),
            int(IGLikesGraphObjects[1].instagram_likes),
            int(IGLikesGraphObjects[2].instagram_likes),
            int(IGLikesGraphObjects[3].instagram_likes),
            int(IGLikesGraphObjects[4].instagram_likes),
            int(IGLikesGraphFirst.instagram_likes)
            ])
        elif IGLikesGraphCount >= 48:
            AllStatLogs = StatsLog.objects.all()[:56:8]
            Instagram_Likes.x_labels = map(str, range(7, 0, -1))
            Instagram_Likes.add('', [
            int(AllStatLogs[0].instagram_likes),
            int(AllStatLogs[1].instagram_likes),
            int(AllStatLogs[2].instagram_likes),
            int(AllStatLogs[3].instagram_likes),
            int(AllStatLogs[4].instagram_likes),
            int(AllStatLogs[5].instagram_likes),
            int(IGLikesGraphFirst.instagram_likes)
            ])

    Instagram_Likes.render_django_response()
    return Instagram_Likes

def GenerateInstagramFollowersGraph():
    custom_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground='white',
        foreground_strong='white',
        foreground_subtle='white',
        opacity='.9',
        transition='400ms ease-in',
        label_font_size=20,
        major_label_font_size=25,
        font_family='googlefont:Raleway',
        colors=('#08BDBD',))
    Graph = pygal.Line(style=custom_style, fill=True, min_scale=1, show_legend=False)
    AllStatLogs = StatsLog.objects.all()
    LatestStatLog = StatsLog.objects.latest('date_created')
    if AllStatLogs.count() >= 1:
        if AllStatLogs.count() < 8:
            Graph.x_labels = map(str, range(1, 2))
            Graph.add('', [
            int(LatestStatLog.instagram_followers)
            ])
        elif AllStatLogs.count() < 16:
            AllStatLogs = StatsLog.objects.all()[:8:8]
            Graph.x_labels = map(str, range(1, 3))
            Graph.add('', [
            int(AllStatLogs[0].instagram_followers),
            int(LatestStatLog.instagram_followers)
            ])
        elif AllStatLogs.count() < 24:
            AllStatLogs = StatsLog.objects.all()[:16:8]
            Graph.x_labels = map(str, range(1, 4))
            Graph.add('', [
            int(AllStatLogs[0].instagram_followers),
            int(AllStatLogs[1].instagram_followers),
            int(LatestStatLog.instagram_followers)
            ])
        elif AllStatLogs.count() < 32:
            AllStatLogs = StatsLog.objects.all()[:24:8]
            Graph.x_labels = map(str, range(1, 5))
            Graph.add('', [
            int(AllStatLogs[0].instagram_followers),
            int(AllStatLogs[1].instagram_followers),
            int(AllStatLogs[2].instagram_followers),
            int(LatestStatLog.instagram_followers)
            ])
        elif AllStatLogs.count() < 40:
            AllStatLogs = StatsLog.objects.all()[:32:8]
            Graph.x_labels = map(str, range(1, 6))
            Graph.add('', [
            int(AllStatLogs[0].instagram_followers),
            int(AllStatLogs[1].instagram_followers),
            int(AllStatLogs[2].instagram_followers),
            int(AllStatLogs[3].instagram_followers),
            int(LatestStatLog.instagram_followers)
            ])
        elif AllStatLogs.count() < 48:
            AllStatLogs = StatsLog.objects.all()[:48:8]
            Graph.x_labels = map(str, range(1, 7))
            Graph.add('', [
            int(AllStatLogs[0].instagram_followers),
            int(AllStatLogs[1].instagram_followers),
            int(AllStatLogs[2].instagram_followers),
            int(AllStatLogs[3].instagram_followers),
            int(AllStatLogs[4].instagram_followers),
            int(LatestStatLog.instagram_followers)
            ])
        elif AllStatLogs.count() >= 48:
            AllStatLogs = StatsLog.objects.all()[:56:8]
            Graph.x_labels = map(str, range(7, 0, -1))
            Graph.add('', [
            int(AllStatLogs[0].instagram_followers),
            int(AllStatLogs[1].instagram_followers),
            int(AllStatLogs[2].instagram_followers),
            int(AllStatLogs[3].instagram_followers),
            int(AllStatLogs[4].instagram_followers),
            int(AllStatLogs[5].instagram_followers),
            int(LatestStatLog.instagram_followers)
            ])
    Graph.render_django_response()
    return Graph
