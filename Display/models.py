from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Genre(models.Model):
    Name = models.CharField(max_length=50)
    Details = models.TextField()
    Logo = models.FileField(null=True , blank=True)
    def __str__(self):
        return self.Name

class Artist(models.Model):
    ArtistName = models.CharField(max_length=200)
    Bio = models.TextField()
    Picture = models.FileField()
    def __str__(self):
        return self.ArtistName

class Song(models.Model):
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Genre  = models.ForeignKey(Genre, on_delete=models.CASCADE)
    Album = models.CharField(max_length=200 ,null=False)
    Title = models.CharField(max_length=50, null=False)
    IntroDetails = models.TextField(null=True)
    Verse1Details = models.TextField(null=True)
    Verse2Details = models.TextField(null=True)
    OutroDetails = models.TextField(null=True)
    Image_src = models.FileField()
    def __str__(self):
        return self.Title

class Request(models.Model):
    Song_name = models.CharField(max_length=200)
    Artist = models.CharField(max_length=100 ,null=True , blank=True)
    Message = models.TextField(null=True , blank=True)
    def __str__(self):
        return self.Song_name
class Author_request(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Verification = models.BooleanField()
