from django.contrib import admin

from website.models import Profile, Project, Image

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'role')
    readonly_fields = ('image_tag',)

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'client', 'date_completed')

class ImageAdmin(admin.ModelAdmin):
    model = Image

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
