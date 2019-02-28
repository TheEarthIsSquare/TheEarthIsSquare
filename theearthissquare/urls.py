from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views
from website import views as website
from dashboard import views as dashboard
from django.contrib.auth import logout
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

urlpatterns = [

    path('', website.home, name='home'),

    path('', include('registration.backends.simple.urls')), # Figure out why this is needed to use the auth_logout link.

    path('admin/', admin.site.urls),

    path('team/', website.team, name='team'),

    path('services/', website.services, name='services'),

    path('services/<parsed_name>/', website.service, name='service'),

    path('examples/', website.examples, name='examples'),

    path('examples/cafe/', website.cafe_example, name='cafe_example'),

    path('portfolio/', website.portfolio, name='portfolio'),

    path('portfolio/<parsed_client>/', website.project, name='project'),

    path('contact/', website.contact, name='contact'),

    path('dashboard/', dashboard.dashboard, name='dashboard'),

    path('dashboard/instagram/', dashboard.dashboard_instagram, name='dashboard_instagram'),

    path('dashboard/facebook/', dashboard.dashboard_facebook, name='dashboard_facebook'),

    path('dashboard/data<type>,<seriesName>', dashboard.dashboard_data, name='dashboard_data'),

    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),

    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml'), name='sitemap'),

    url(r'^s3direct/', include('s3direct.urls')),

    url(r'^tinymce/', include('tinymce.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
