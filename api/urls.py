from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^login', login.as_view(), name='login'),
    url(r'^logout',logout.as_view(),name='logout'),
    url(r'^getAllSongs',getAllSongs.as_view(),name='getAllSongs'),
    url(r'^getAllPlaylist',getAllPlaylist.as_view(),name='getAllPlaylist'),
    url(r'^addToPlaylist',addToPlaylist.as_view(),name='addToPlaylist'),
    url(r'^getFromPlaylist/(?P<playlist_id>[0-9]+)',getFromPlaylist.as_view(),name='getFromPlaylist'),
    url(r'^deletePlaylist/(?P<playlist_id>[0-9]+)',deletePlaylist.as_view(),name='deletePlaylist'),
]+ static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)