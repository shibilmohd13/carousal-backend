from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class TitleSubtitleModel(models.Model):
    title = models.CharField(max_length=300)
    sub_title = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now_add=True)
