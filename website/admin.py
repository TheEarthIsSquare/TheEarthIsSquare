from django.contrib import admin

from website.models import *

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'role')

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'client', 'date_completed')

class ImageAdmin(admin.ModelAdmin):
    model = Image

class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('name', 'parent', 'parent_service', 'enabled',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Service, ServiceAdmin)

admin.site.site_header = "The Earth is Square"
admin.site.site_title = "The Earth is Square"
admin.site.index_title = "Admin Panel"
admin.site.index_template = "admin/admin_index.html"
