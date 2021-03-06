from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from videos.models import Video
from djangoflix.db.models import PublishStateOptions
from djangoflix.db.receivers import publish_state_pre_save, slugify_pre_save


class PublishStateOptions(models.TextChoices):
        PUBLISH = 'PU','Published'
        DRAFT = 'DR','Draft'
        UNLISTED = 'UN','Unlisted'
        PRIVATE = 'PR','Private'

class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte= now 
        )

class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

class Playlist(models.Model):
    PlaylistStateOptions = PublishStateOptions
    video = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    state = models.CharField(max_length=4, choices=PlaylistStateOptions.choices, default=PlaylistStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PlaylistManager()

    @property
    def is_published(self):
        return self.active
    




pre_save.connect(publish_state_pre_save, sender=Playlist)
pre_save.connect(slugify_pre_save, sender=Playlist)