from django.test import TestCase
from django.utils import timezone
from .models import Video
# Create your tests here.

class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title='This is my title')
        Video.objects.create(title='This is my title', state=Video.VideoStateOptions.PUBLISH)

    def test_valid_title(self):
        title = 'This is my title'
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())
    
    def test_draft_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)
    
    def test_publish_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.PUBLISH)
        now = timezone.now()
        published_qs = Video.objects.filter(publish_timestamp__lte=now)
        self.assertTrue(published_qs.exists())