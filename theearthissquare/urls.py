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

    path('', include('registration.backends.simple.urls')),

    path('admin/', admin.site.urls),

    path('team/', views.team, name='team'),

    path('services/', TemplateView.as_view(template_name = 'services.html'), name='services'),

    path('portfolio/', TemplateView.as_view(template_name = 'portfolio.html'), name='portfolio'),

    path('contact/', TemplateView.as_view(template_name = 'contact.html'), name='contact'),

    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),

    url(r'^s3direct/', include('s3direct.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
