from django.contrib.admin.sites import *
from django import template

register = template.Library()
@register.simple_tag
def all_apps ():
    return self.get_app_list(request)
