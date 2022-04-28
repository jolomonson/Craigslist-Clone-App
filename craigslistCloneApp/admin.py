from django.contrib import admin
from .models import Search
# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    list_display = (
        'search',
        'min_price',
        'max_price'
    )
    list_filter = (
        'search',
        'min_price',
        'max_price'
    )
admin.site.register(Search)