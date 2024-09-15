import subprocess
from celery import shared_task

from .models import Video, Subtitle

@shared_task
def process_video(video_id):
    video = Video.objects.get(id=video_id)
    video_path = video.file.path
    subtitle_path = f"{video_path}.srt"

    try:
        result = subprocess.run(
            ['ccextractor', video_path, '-o', subtitle_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"ccextractor output: {result.stdout.decode()}")
        print(f"ccextractor error: {result.stderr.decode()}")

        # Read the subtitle file and save it to the database
        with open(subtitle_path, 'r') as f:
            subtitle_content = f.read()

        Subtitle.objects.create(video=video, language='en', content=subtitle_content)
        print(f"Successfully processed video {video_id}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing video {video_id}: {e}")
        print(f"Command output: {e.output.decode()}")
        print(f"Command error output: {e.stderr.decode()}")
        raise