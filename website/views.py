from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'index.html', {
    })

def redirect_home(request):
    response = redirect('home')
    return response
