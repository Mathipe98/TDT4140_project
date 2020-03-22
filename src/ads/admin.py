"""
    Registers the advertisement model so that it is available in the django admin page
"""

from django.contrib import admin
from .models import Advertisement

# Register your models here.
admin.site.register(Advertisement)
