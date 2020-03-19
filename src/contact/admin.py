from django.contrib import admin
from .models import Messages, Thread, Ratings

# Register your models here.
admin.site.register(Messages)
admin.site.register(Thread)
admin.site.register(Ratings)
