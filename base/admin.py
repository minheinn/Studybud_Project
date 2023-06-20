from django.contrib import admin
from .models import *

# Register your models here.
class AdminRoom(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
admin.site.register(User)
admin.site.register(Room, AdminRoom)
admin.site.register(Topic)
admin.site.register(Message)