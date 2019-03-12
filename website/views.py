from django.shortcuts import render, redirect
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

    timeout = 4500 if loading_screen else 0

    projects = Project.objects.all().order_by('-ongoing', '-date_completed')[:4]
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

    if request.method == 'POST':
        if request.POST['action'] == 'Dev_Off':
            request.user.profile.dev_mode = False
            request.user.profile.save()
        elif request.POST['action'] == 'Dev_On':
           request.user.profile.dev_mode = True
           request.user.profile.save()

    developer_mode = request.user.profile.dev_mode if request.user.is_authenticated else False

    template = 'dev/index.html' if developer_mode else 'index.html'

    connection.close()
    return render(request, template, {
    'projects' : projects,
    'profiles' : profiles,
    'timeout' : timeout,
    'developer_mode' : developer_mode,
    })

def services(request):

    services = Service.objects.order_by('name').filter(type='a')
    included_services = Service.objects.filter(type='b')
    addon_services = Service.objects.filter(type='c')

    if request.method == 'POST':
        if request.POST['action'] == 'Dev_Off':
            request.user.profile.dev_mode = False
            request.user.profile.save()
        elif request.POST['action'] == 'Dev_On':
           request.user.profile.dev_mode = True
           request.user.profile.save()

    if request.user.is_authenticated:
        developer_mode = request.user.profile.dev_mode
    else:
        developer_mode = False

    template = 'services.html'
    if developer_mode == True:
        template = 'dev/services.html'

    connection.close()
    return render(request, template, {
    'services' : services,
    'included_services' : included_services,
    'addon_services' : addon_services,
    })

def portfolio(request):
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

def about(request):
    profiles = Profile.objects.all().order_by('name')

    connection.close()
    return render(request, 'about.html', {
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

def examples(request):

    return render(request, 'examples.html', {
    })

def cafe_example(request):

    return render(request, 'cafe_example/index.html', {
    })
