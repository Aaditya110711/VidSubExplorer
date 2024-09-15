from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Subtitle(models.Model):
    video = models.ForeignKey(
        Video, related_name='subtitles', on_delete=models.CASCADE)
    language = models.CharField(max_length=10)
    content = models.TextField()

    def __str__(self):
        return f"{self.video.title} - {self.language}"
