from django.contrib import admin
from django.contrib.admin import AdminSite

from website.models import *

from dashboard.models import *

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
    list_display = ('name', 'type', 'tag', 'parent_service')
    readonly_fields = ["date_created", "date_modified"]

class InstagramPostAdmin(admin.ModelAdmin):
    model = InstagramPost
    list_display = ('date_published', 'like_count', 'comment_count')
    readonly_fields = ["date_created", "date_modified"]

class SettingAdmin(admin.ModelAdmin):
    model = Setting
    list_display = ('name', 'value')
    readonly_fields = ["date_created", "date_modified"]

class StatsLogAdmin(admin.ModelAdmin):
    model = StatsLog
    list_display = ('id', 'date_created')
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["instagram_posts", "instagram_likes", "instagram_followers", "facebook_likes", "date_created", "date_modified"]
        else:
            return []

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(InstagramPost, InstagramPostAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(StatsLog, StatsLogAdmin)


admin.site.site_header = "The Earth is Square"
admin.site.site_title = "The Earth is Square"
admin.site.index_title = "Admin Panel"
admin.site.index_template = "admin/admin_index.html"
