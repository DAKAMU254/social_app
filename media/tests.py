from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment, Follow

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(user=self.user, content='Test content')

    def test_post_creation(self):
        self.assertEqual(self.post.content, 'Test content')
        self.assertEqual(self.post.user.username, 'testuser')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(user=self.user, content='Test content')
        self.comment = Comment.objects.create(user=self.user, post=self.post, content='Test comment')

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, 'Test comment')
        self.assertEqual(self.comment.post.content, 'Test content')
        self.assertEqual(self.comment.user.username, 'testuser')

class FollowModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.follow = Follow.objects.create(follower=self.user1, followed=self.user2)

    def test_follow_creation(self):
        self.assertEqual(self.follow.follower.username, 'testuser1')
        self.assertEqual(self.follow.followed.username, 'testuser2')
