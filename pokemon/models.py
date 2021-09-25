from django.db import models
from fwbasemodel.models import BaseModel
# Create your models here.


class Pokemon(BaseModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Name', blank=False, unique=True)
    base_stats = models.JSONField(null=False)
    height = models.IntegerField(blank=False)
    weight = models.IntegerField(blank=False)
    evolutions = models.JSONField(null=False)
    created_at = models.DateTimeField(null=True, blank=True, verbose_name=u'Fecha de creación')
