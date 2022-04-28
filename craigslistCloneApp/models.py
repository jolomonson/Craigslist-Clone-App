from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    min_price = models.CharField(max_length=100)
    max_price = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'
