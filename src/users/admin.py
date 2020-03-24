from django.contrib import admin
from .models import Users
from ads.models import Category

# Register your models here.
admin.site.register(Users)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')
    admin.site.register(Category)
