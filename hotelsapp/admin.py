from django.contrib import admin
from .models import *


@admin.register(Hotel)
class HotyelModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'rate', 'created')


admin.site.register(PictureModel)
