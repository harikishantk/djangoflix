from django.contrib import admin

# Register your models here.
from .models import Video, VideoPublishedProxy, VideoAllProxy

class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['id','title','state','video_id','is_published','get_playlist_ids']
    search_fields = ['title']
    list_filter = ['active', 'state']
    readonly_fields = ['id','is_published', 'publish_timestamp','get_playlist_ids']
    class Meta:
        model = VideoAllProxy
    
    # def published(self, obj, *args, **kwargs):
    #     return obj.active

admin.site.register(VideoAllProxy, VideoAllAdmin)

class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title','video_id']
    search_fields = ['title']
    class Meta:
        model = VideoPublishedProxy
    
    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)

admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)