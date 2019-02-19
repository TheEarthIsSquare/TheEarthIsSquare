from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views
from website import views
from django.contrib.auth import logout
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

urlpatterns = [

    path('', views.home, name='home'),

    path('', include('registration.backends.simple.urls')), # Figure out why this is needed to use the auth_logout link.

    path('admin/', admin.site.urls),

    path('team/', views.team, name='team'),

    path('services/', views.services, name='services'),

    path('services/<parsed_name>/', views.service, name='service'),

    path('portfolio/', views.portfolio, name='portfolio'),

    path('portfolio/<parsed_client>/', views.project, name='project'),

    path('contact/', views.contact, name='contact'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),

    url(r'^s3direct/', include('s3direct.urls')),

    url(r'^tinymce/', include('tinymce.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
