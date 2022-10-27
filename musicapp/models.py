from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    date_released = models.DateTimeField('date published')

class Lyrics(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
