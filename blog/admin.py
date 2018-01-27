from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_created', 'time_last_modified', 'category', 'author']

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)