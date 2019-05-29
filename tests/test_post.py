import unittest
from app.models import Post, User
from app import db

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username='James', password='potato', email='james@ms.com')
        self.new_post = Post(post_id=12345, text='Inspirational', user=self.user_James)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.post_id, 12345)
        self.assertEquals(self.new_post.text, 'Inspirational')
        self.assertEquals(self.new_post.user, self.user_James)

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_post_by_id(self):
        self.new_post.save_post()
        got_posts = Post.get_posts(12345)
        self.assertTrue(len(got_posts) == 1)