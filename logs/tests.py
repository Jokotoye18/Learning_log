from django.test import TestCase
from django.urls import reverse
from logs.models import Topic, Entry
from django.contrib.auth import get_user_model


class TestTopicModel(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testname',
            email = 'test@gmail.com',
            password = '12345'
        )
        self.topic = Topic.objects.create(
            author = self.user,
            topic = 'New topic for test',
            slug = 'new-topic-for-test',
        )

    def test_topic_text_representation(self):
        self.assertEqual(f'{self.topic}', 'New topic for test')

    def test_topic_get_absolute_url(self):
        self.assertEqual(self.topic.get_absolute_url(), '/logs/new-topic-for-test-1/')

    def test_topic_content(self):
        self.assertEqual(f'{self.topic.author}', 'testname')
        self.assertEqual(f'{self.topic.topic}', 'New topic for test')
        self.assertEqual(f'{self.topic.slug}', 'new-topic-for-test')
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(Topic.objects.count(), 1)

