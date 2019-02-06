from django.shortcuts import render
from django.shortcuts import redirect
from website.models import Profile, Project, Image


# Create your views here.
def home(request):
    return render(request, 'index.html', {
    })

def redirect_home(request):
    response = redirect('home')
    return response

def team(request):
    profiles = Profile.objects.all().order_by('name')
    return render(request, 'team.html', {
    'profiles': profiles,
    })
