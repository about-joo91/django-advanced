from typing import Tuple

from django.http import HttpRequest
from ninja import Router

from tabom.apis.v1.schemas.like_request import LikeRequest
from tabom.apis.v1.schemas.like_response import LikeResponse
from tabom.models.like import Like
from tabom.services.like_service import do_like, undo_like

router = Router()


@router.post("/", response=LikeResponse)
def post_like(request: HttpRequest, like_request: LikeRequest) -> Tuple[int, Like]:
    like = do_like(article_id=like_request.article_id, user_id=like_request.user_id)
    return 201, like


@router.delete("/", response=LikeResponse)
def delete_like(user_id: int, article_id: int) -> Tuple[int, None]:
    undo_like(user_id=user_id, article_id=article_id)
    return 204, None