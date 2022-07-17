from django.db import models

from .base_model import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=255)
