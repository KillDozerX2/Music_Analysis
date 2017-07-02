from django.contrib import admin

from .models import Artist, Genre, Song, Request


# Register your models here.


admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Request)