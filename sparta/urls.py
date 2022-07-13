from typing import Dict

from django.contrib import admin
from django.http import HttpRequest
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/add")
def add(request: HttpRequest, a: int, b: int) -> Dict[str, int]:
    return {"result": a + b}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
