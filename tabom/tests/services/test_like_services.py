from django.db.utils import IntegrityError
from django.test import TestCase

from tabom.models.article import Article
from tabom.models.like import Like
from tabom.models.user import User
from tabom.services.like_service import do_like, undo_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        like = do_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect
        do_like(user.id, article.id)
        with self.assertRaises(IntegrityError):
            do_like(user.id, article.id)

    def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:
        # Given
        invalid_user_id = 9988
        article = Article.objects.create(title="test_title")

        # Expect
        with self.assertRaises(User.DoesNotExist):
            do_like(invalid_user_id, article.id)

    def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:
        # Given
        user = User.objects.create(name="test")
        invalid_article_id = 9988

        # Expect
        with self.assertRaises(Article.DoesNotExist):
            do_like(user.id, invalid_article_id)

    def test_a_user_can_undo_like(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_article")
        like = do_like(user.id, article.id)

        # When
        undo_like(user.id, article.id)

        # Then
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.filter(id=like.id).get()
