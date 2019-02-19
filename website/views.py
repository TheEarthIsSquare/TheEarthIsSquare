from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from website.models import Profile, Project, Image, Service
from theearthissquare import settings
from website.forms import *
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

def findInstagramId():
    access_token = 'EAAXyjkCQvyIBAGUqaAdNB6j2Pl7rMo7NMuVm0VHPaAaZAvSQD2wowKFZBdhNEgoZAjFdMLdDAee4Jyrqj6fW61xVrjDcejsrzkBE100f6BhkQzgilRnuYVh5jUGsWjjVDKYILAetAPmivfXNANTZCeWeeg4bz0YLpBLtxBjSEbNmupP2w2kRQEzAcJPUYjxC1g9odM0ZCoAZDZD'

    url = 'https://graph.facebook.com/me?access_token=' + access_token
    response = requests.get(url).json()
    dump = json.dumps(response)
    loadJson = json.loads(dump)
    error = loadJson.get('error')
    if error != None:
        print('There has been an error with accessing the Facebook Page ID /me: ' + error['message'])
        return loadJson
    else:
        url = 'https://graph.facebook.com/' + loadJson['id'] + '?fields=connected_instagram_account&access_token=' + access_token
        response = requests.get(url).json()
        dump = json.dumps(response)
        loadJson = json.loads(dump)
        error = loadJson.get('error')
        if error != None:
            print('There has been an error when attempting to list connected Instagram: ' + error['message'])
            print(error)
            return loadJson
        else:
            print(loadJson)
            return loadJson['connected_instagram_account']['id']

def instagramFollowers():
    settings = graphAPI();
    id = findInstagramId()
    error = id.get('error')
    if error != None:
        print(id)
        return id
    else:
        print(id)
        url = 'https://graph.facebook.com/' + id + '?fields=followers_count&access_token=' + settings['access_token']
        response = requests.get(url).json()
        dump = json.dumps(response)
        loadJson = json.loads(dump)
        error = loadJson.get('error')
        if error != None:
            print('There has been an error trying to get the follower count: ' + error['message'])
            return loadJson['error']
        else:
            print(loadJson)
            return loadJson['followers_count']

def facebookFollowers():
    settings = graphAPI();
    url = 'https://graph.facebook.com/me?fields=fan_count&access_token=' + settings['access_token']
    response = requests.get(url).json()
    dump = json.dumps(response)
    loadJson = json.loads(dump)
    error = loadJson.get('error')
    if error != None:
        print('There has been an error when attempting to get the Facebook fan count ' + error['message'])
        return loadJson
    else:
        print(loadJson)
    return loadJson['fan_count']

def graphAPI():
    settings = {
        'access_token' : 'EAAXyjkCQvyIBAGUqaAdNB6j2Pl7rMo7NMuVm0VHPaAaZAvSQD2wowKFZBdhNEgoZAjFdMLdDAee4Jyrqj6fW61xVrjDcejsrzkBE100f6BhkQzgilRnuYVh5jUGsWjjVDKYILAetAPmivfXNANTZCeWeeg4bz0YLpBLtxBjSEbNmupP2w2kRQEzAcJPUYjxC1g9odM0ZCoAZDZD',
        }
    return settings

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        instagram_count = instagramFollowers()
        facebook_count = facebookFollowers()
        return render(request, 'dashboard.html', {
        'instagram_count' : instagram_count,
        'facebook_count' : facebook_count,
        })
