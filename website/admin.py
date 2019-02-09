from django.contrib import admin

from website.models import *

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'role')
    readonly_fields = ('image_tag',)

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'client', 'date_completed')

class ImageAdmin(admin.ModelAdmin):
    model = Image

class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('name',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Service, ServiceAdmin)
