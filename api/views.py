from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User

# Create your views here.
class login(APIView):

    serializer_class = loginSerializer
    permission_classes = [AllowAny]

    def post(self,request, *args, **kwargs):
        data = request.data
        serializer = loginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            context = {'user_id':new_data['use_id'],'token':new_data['token']}
            return Response(context, status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class logout(APIView):

    queryset = User.objects.all()

    def get(self, request, format=None):
        request.user.auth_token.delete()
        context = {'deleted':"yes"}
        return Response(context,status=HTTP_200_OK)

class getAllSongs(generics.ListAPIView):

    queryset = allSongs.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = allSongsSerializer
    authentication_classes = (TokenAuthentication,)

class getAllPlaylist(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = playlistSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return playlist.objects.filter(user=user.pk)

class addToPlaylist(generics.CreateAPIView):
    queryset = playListSongs.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = addToPlaylistSerializer
    authentication_classes = (TokenAuthentication,)

class getFromPlaylist(generics.ListAPIView):

    lookup_url_kwarg = "playlist_id"
    permission_classes = [IsAuthenticated]
    serializer_class = getFromPlaylistSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):

        playlist_id = self.kwargs.get(self.lookup_url_kwarg)
        data = playListSongs.objects.filter(playlist_id=playlist_id)
        return data

class deletePlaylist(generics.RetrieveUpdateDestroyAPIView):

    queryset = playlist.objects.all()
    lookup_url_kwarg = "playlist_id"
    permission_classes = [IsAuthenticated]
    serializer_class = getFromPlaylistSerializer
    authentication_classes = (TokenAuthentication,)

    def delete(self, request, *args, **kwargs):
        playlist_id = self.kwargs.get(self.lookup_url_kwarg)
        toDelete = playlist.objects.get(pk=playlist_id).delete()
        context = {'deleted': "yes"}
        return Response(context, status=HTTP_200_OK)