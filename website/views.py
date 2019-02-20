from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from website.models import Profile, Project, Image, Service
from theearthissquare import settings
from website.forms import *
from website.functions import *
from django.template.loader import get_template
from django.core.mail import send_mail
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
import requests, json, logging



# Create your views here.
def home(request, reason=""):
    loading_screen = settings.USE_LOADING_SCREEN

    if loading_screen == False:
        timeout = 0
    else:
        timeout = 5500

    services = Service.objects.filter(parent=True)
    projects = Project.objects.all().order_by('-ongoing', '-date_completed')
    profiles = Profile.objects.all().order_by('name')

    # If user accesses homepage and IS NOT logged in.
    # if not request.user.is_authenticated:
    #    username = request.POST.get('username')
    #    password = request.POST.get('password')
    #    user = authenticate(request, username=username, password=password)
    #    if user is not None:
    #        login(request, user)
    #    else:
    #        return render(request, 'index.html')

    connection.close()
    return render(request, 'index.html', {
    'services' : services,
    'projects' : projects,
    'profiles' : profiles,
    'timeout' : timeout,
    })

def services(request):

    services = Service.objects.filter(parent=True, enabled=True)
    sub_services = Service.objects.filter(parent=False, enabled=True, package=False)

    connection.close()
    return render(request, 'services.html', {
    'services' : services,
    'sub_services' : sub_services,
    })

def service(request, parsed_name):
    name = parsed_name.replace('_', ' ')
    service = Service.objects.get(name__iexact=name)

    connection.close()
    return render(request, 'service.html', {
    'service' : service,
    })

def portfolio(request):
    services = Service.objects.filter(parent=True)
    portfolio = Project.objects.all().order_by('-ongoing', '-date_completed')

    connection.close()
    return render(request, 'portfolio.html', {
    'portfolio' : portfolio,
    })

def project(request, parsed_client):
    client = parsed_client.replace('_', ' ')
    project = Project.objects.get(client__iexact=client)

    connection.close()
    return render(request, 'project.html', {
    'project' : project,
    })

def team(request):
    profiles = Profile.objects.all().order_by('name')

    connection.close()
    return render(request, 'team.html', {
    'profiles' : profiles,
    })

def contact(request):
    coffee_form = ContactForm_Coffee
    work_form = ContactForm_Work
    other_form = ContactForm_Other
    success = False

    if request.method == 'POST':
        if request.POST['action'] == 'Coffee':
            form = ContactForm_Coffee(data=request.POST)

        elif request.POST['action'] == 'Work':
            form = ContactForm_Work(data=request.POST)

        else:
            form = ContactForm_Other(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            if request.POST['action'] == 'Coffee':
                city = form.cleaned_data['city']

                # email the profile with the contact info
                template = get_template('contact_coffee.txt')

                context = {
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': form_content,
                    'city': city,
                }

            elif request.POST['action'] == 'Work':
                type = form.cleaned_data['type']

                # email the profile with the contact info
                template = get_template('contact_work.txt')

                context = {
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': form_content,
                    'type': type,
                }

            else:

                # email the profile with the contact info
                template = get_template('contact_other.txt')

                context = {
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': form_content,
                }

            content = template.render(context)

            send_mail(
                'Contact Form: ' + contact_name + ' (' + contact_email + ')',
                content + ' REPLY TO: ' + contact_email,
                'hello@theearthissquare.com',
                ['hello@theearthissquare.com'],
                fail_silently=False,
            )
            success = True

    return render(request, 'contact.html', {
        'coffee_form': coffee_form,
        'work_form': work_form,
        'other_form': other_form,
        'emailSent': success,
    })

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
        instagram_likes = 0
        for mediaLikes in allPostLikes:
            instagram_likes = instagram_likes + mediaLikes

        # Get Facebook Follower Count
        try:
            facebookFollowers = Settings.objects.get(name="SocialsDashboard.FacebookFollowers")
        except Settings.DoesNotExist:
            facebookFollowers = Settings.objects.create(name="SocialsDashboard.FacebookFollowers",value=0)

        try:
            lastUpdate = Settings.objects.get(name="SocialsDashboard.LastUpdate")
        except Settings.DoesNotExist:
            lastUpdate = Settings.objects.create(name="SocialsDashboard.LastUpdate",value=Null)


        return render(request, 'dashboard.html', {
        'instagramFollowers' : instagramFollowers.value,
        'facebookFollowers' : facebookFollowers.value,
        'instagram_likes' : instagram_likes,
        'lastUpdate' : datetime.strptime(lastUpdate.value, '%Y-%m-%d %H:%M:%S.%f'),
        })
