from rest_framework import serializers
from rest_framework.serializers import CharField, IntegerField
from django.contrib.auth.models import User
from .models import *
from django.db.models import Q
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token

class loginSerializer(serializers.ModelSerializer):

    username = CharField()
    use_id = IntegerField(allow_null=True,required=False)
    token= CharField(allow_null=True, required=False)

    class Meta:

        model = User
        fields = [
            'username',
            'password',
            'use_id',
            'token'
        ]

    def validate(self,data):

        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(Q(username=username)).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("User Doesn't Exist")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Wrong Password")
        token, _ = Token.objects.get_or_create(user=user_obj)
        data["use_id"] = user_obj.pk
        data["token"] = token.key
        return data

class allSongsSerializer(serializers.ModelSerializer):

    class Meta:

        model = allSongs
        fields = '__all__'

class playlistSerializer(serializers.ModelSerializer):

    class Meta:

        model = playlist
        fields = '__all__'

class addToPlaylistSerializer(serializers.ModelSerializer):

    class Meta:

        model = playListSongs
        fields = '__all__'

class getFromPlaylistSerializer(serializers.ModelSerializer):

    class Meta:

        model = playListSongs
        fields = '__all__'
        depth = 1

