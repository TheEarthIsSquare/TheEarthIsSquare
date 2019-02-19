from django.contrib import admin

from website.models import *

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'role')
    readonly_fields = ["date_created", "date_modified"]

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('client', 'type', 'date_completed')
    readonly_fields = ["date_created", "date_modified"]

class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('name', 'parent', 'package', 'parent_service', 'enabled',)
    readonly_fields = ["date_created", "date_modified"]

class InstagramPostAdmin(admin.ModelAdmin):
    model = InstagramPost
    list_display = ('date_published', 'like_count', 'comment_count')
    readonly_fields = ["date_created", "date_modified"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(InstagramPost, InstagramPostAdmin)

admin.site.site_header = "The Earth is Square"
admin.site.site_title = "The Earth is Square"
admin.site.index_title = "Admin Panel"
admin.site.index_template = "admin/admin_index.html"
