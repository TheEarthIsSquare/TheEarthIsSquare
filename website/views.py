from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from website.models import Profile, Project, Image, Service
from theearthissquare import settings
from website.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import send_mail


# Create your views here.
def home(request, reason=""):

    loading_screen = settings.USE_LOADING_SCREEN

    if loading_screen == False:
        timeout = 0
    else:
        timeout = 5500

    services = Service.objects.filter(parent=True)
    projects = Project.objects.all().order_by('client')
    profiles = Profile.objects.all().order_by('name')

    # If user accesses homepage and IS NOT logged in.
    if not request.user.is_authenticated:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'index.html')

    return render(request, 'index.html', {
    'services' : services,
    'projects' : projects,
    'profiles' : profiles,
    'timeout' : timeout,
    })

def services(request):
    services = Service.objects.filter(parent=True)

    return render(request, 'services.html', {
    'services' : services,
    })

def service(request, parsed_name):
    name = parsed_name.replace('_', ' ')
    service = Service.objects.get(name__iexact=name)

    return render(request, 'service.html', {
    'service' : service,
    })

def portfolio(request):
    services = Service.objects.filter(parent=True)
    portfolio = Project.objects.all().order_by('client')

    return render(request, 'portfolio.html', {
    'portfolio' : portfolio,
    })

def project(request, parsed_client):
    client = parsed_client.replace('_', ' ')
    project = Project.objects.get(client__iexact=client)

    return render(request, 'project.html', {
    'project' : project,
    })

def team(request):
    profiles = Profile.objects.all().order_by('name')
    return render(request, 'team.html', {
    'profiles' : profiles,
    })

def contact(request):
    form_class = ContactForm
    success = False

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            # email the profile with the contact info
            template = get_template('contact_template.txt')

            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }

            content = template.render(context)

            send_mail(
                'New Contact Form',
                content + ' REPLY TO: ' + contact_email,
                'hello@theearthissquare.com',
                ['hello@theearthissquare.com'],
                fail_silently=False,
            )
            success = True

    return render(request, 'contact.html', {
        'form': form_class,
        'emailSent': success,
    })
