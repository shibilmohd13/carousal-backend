from django.urls import path, include  # Import include here

from django.contrib import admin
from video.views import upload_video, LoginView, delete_video, show_all_videos
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from video.views import TitleSubtitleModelViewSet

router = DefaultRouter()
router.register(r'titlesubtitlemodels', TitleSubtitleModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload/', upload_video, name='upload_video'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/videos/<int:video_id>/', delete_video, name='delete_video'),
    path('api/videos/', show_all_videos, name='show_all_videos'),
    path('', include(router.urls)), 
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
