from django.contrib import admin
from .models import Home
from .models import About

# Register your models here.
admin.site.register(Home)
admin.site.register(About)