from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', upload_video, name='video_upload'),
    path('list/', video_list, name='video_list'),
    path('search/', search_subtitles, name='video_search'),
    path('video_detail/<int:video_id>', video_detail, name='video_detail')
]
