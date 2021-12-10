from django.contrib import admin

# Register your models here.

from .models import Boardgame
admin.site.register(Boardgame)

from .models import Info
admin.site.register(Info)