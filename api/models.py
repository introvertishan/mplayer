from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class allSongs(models.Model):

    title = models.CharField(max_length=255, blank=False)
    artists = models.CharField(max_length=255, blank=False)
    song_url = models.FileField(upload_to = 'songs',blank=False,validators=[FileExtensionValidator(allowed_extensions=['mp3'])])

    def __str__(self):
        return "{}".format(self.title)

class playlist(models.Model):

    user = models.ForeignKey(User)
    name = models.CharField(max_length=250)

    def __str__(self):

        return "{}".format(self.name)

class playListSongs(models.Model):

    song_id = models.ForeignKey(allSongs)
    playlist_id = models.ForeignKey(playlist)