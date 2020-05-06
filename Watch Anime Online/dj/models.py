from django.db import models

# Create your models here.
class anime(models.Model):
    anime_name=models.CharField(max_length=50)
    anime_desc=models.CharField(max_length=300)
    episodes_no=models.IntegerField()
    image=models.ImageField(upload_to='dj/images',default='')
    video=models.FileField(upload_to='dj/videos',null=True,verbose_name='video')
    def __str__(self):
        return self.anime_name +":" + str(self.video)
        