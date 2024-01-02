from django import template
from ..models import Official, Assignment
from django.db import models

register = template.Library()

@register.simple_tag
def get_official_upcoming(official, org):
    return Assignment.objects.filter(official=official) # TODO: Also filter by date and organization

@register.simple_tag
def get_officials_sorted(org, sorting):
    officials = org.officials

    if sorting == "last_first":       
        officials = sorted(org.officials, key=lambda official: official.user.get_name_last_first())

    elif sorting == "first_last":
        officials = sorted(org.officials, key=lambda official: official.user.get_full_name())

    return officials
