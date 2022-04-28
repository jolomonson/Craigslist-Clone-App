from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Search(models.Model):
    search = models.CharField(_('Search'), max_length=500),
    min_price = models.CharField(_('Minimum Price'), max_length=100)
    max_price = models.CharField(_('Maximum Price'),max_length=100)
    created_at = models.DateTimeField(_('Created at '),auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at '),auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Search'
        verbose_name_plural = 'Searches'
