from django.contrib import admin
from .models import MovieGenre, Movie

# Register your models here.


admin.site.register(Movie)
admin.site.register(MovieGenre)
