from django.contrib import admin
from .models import Search
# Register your models here.

@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = (
        'search',
        'min_price',
        'max_price'
    )
    list_filter = (
        'min_price',
        'max_price'
    )
