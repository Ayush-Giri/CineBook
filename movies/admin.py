from django.contrib import admin
from movies.models import Genre, Language, Movies

# Register your models here.

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Movies)
