from django.contrib import admin

from .models import UserProfile, DrawingTables, News

admin.site.register(UserProfile)
admin.site.register(DrawingTables)
admin.site.register(News)

# Register your models here.
