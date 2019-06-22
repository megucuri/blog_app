from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
from .models import Post


class BlogTests(TestCase):
    def setUp(self):  # From TestCase we can use the method setUp to create a new test database
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    # We expect the URL of our test to be at blog/1/detail since there’s only one post and the 1 is its primary key Django adds automatically for us.
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/blog/1/detail')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get('/blog/1/detail')
        no_response = self.client.get('/blog/100000/detail')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_create_view(self):  # Create a new post
        response = self.client.post(reverse('blog:post_new'), {
            'title': 'New title',
            'body': 'New text',
            'authoer': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('blog:post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    # Finally we test our delete view by confirming that if we delete a post the status code is 200 for success.
    def test_post_delete_view(self):
        response = self.client.get(reverse('blog:post_delete', args='1'))
        self.assertEqual(response.status_code, 200)
