from django.views import View
from django.http import JsonResponse
from .models import Video,Subtitle
from .tasks import process_video
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
class VideoUploadView(View):
    def post(self, request):
        video_file = request.FILES.get('video')
        if not video_file:
            return JsonResponse({'error': 'No video file provided'}, status=400)
        
        video = Video.objects.create(
            title=video_file.name,
            file=video_file
        )
        
        # Trigger background processing
        process_video.delay(video.id)
        
        return JsonResponse({'message': 'Video uploaded successfully', 'video_id': video.id})
    
class VideoListView(View):
    def get(self, request):
        videos = Video.objects.filter(processed=True).values('id', 'title', 'uploaded_at')
        return JsonResponse({'videos': list(videos)})
    

class VideoSearchView(View):
    def get(self, request):
        query = request.GET.get('q', '').lower()
        video_id = request.GET.get('video_id')
        
        if not query or not video_id:
            return JsonResponse({'error': 'Missing query or video_id'}, status=400)
        
        subtitles = Subtitle.objects.filter(
            Q(video_id=video_id) & Q(content__icontains=query)
        ).values('content', 'start_time', 'end_time')
        
        results = [
            {
                'content': sub['content'],
                'start_time': sub['start_time'],
                'end_time': sub['end_time']
            }
            for sub in subtitles
        ]
        
        return JsonResponse({'results': results})
    
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    subtitles = video.subtitles.all()
    return render(request, 'video_detail.html', {'video': video, 'subtitles': subtitles})

def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        video_file = request.FILES.get('video')
        
        if title and video_file:
            video = Video.objects.create(title=title, file=video_file)
            process_video.delay(video.id)
            return JsonResponse({'status': 'success', 'video_id': video.id})
    
    return JsonResponse({'status': 'error'})

def search_subtitles(request, video_id):
    query = request.GET.get('q', '').lower()
    video = get_object_or_404(Video, id=video_id)
    subtitles = video.subtitles.all()
    
    results = []
    for subtitle in subtitles:
        content = subtitle.content.lower()
        if query in content:
            timestamp = content.index(query)  # This is a simplification, you'll need to implement proper timestamp extraction
            results.append({'timestamp': timestamp, 'text': subtitle.content})
    
    return JsonResponse({'results': results})