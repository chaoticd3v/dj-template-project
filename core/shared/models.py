from django.db import models
from django.db.models import fields


class BaseModel(models.Model):
    objects = models.Manager()

    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
