"""
    Registers the models Messages, Thread and Ratings for use in the Django admin site
"""

from django.contrib import admin
from .models import Messages, Thread, Ratings

# Register your models here.
admin.site.register(Messages)
admin.site.register(Thread)
admin.site.register(Ratings)
