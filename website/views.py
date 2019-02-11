from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from website.models import Profile, Project, Image, Service
from theearthissquare import settings

# Create your views here.
def home(request, reason=""):

    loading_screen = settings.USE_LOADING_SCREEN
    if loading_screen == True:
        timeout = 5500
    else:
        timeout = 0

    services = Service.objects.filter(parent=True)
    projects = Project.objects.all().order_by('name')
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

# def redirect_home(request):
#    return redirect('home', {
#    })

def team(request):
    profiles = Profile.objects.all().order_by('name')
    return render(request, 'team.html', {
    'profiles' : profiles,
    })
