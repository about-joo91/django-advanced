from django.db import models

from tabom.models.article import Article
from tabom.models.user import User

from .base_model import BaseModel


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "article"], name="unique_user_article")]
