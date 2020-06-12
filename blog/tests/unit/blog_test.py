from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Blog')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Blog', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        pass

    def test_creat_posts(self):
        pass

    def test_json(self):
        pass
