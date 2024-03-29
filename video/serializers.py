from rest_framework import serializers
from .models import Video
from . models import TitleSubtitleModel
from django.contrib.auth import authenticate

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'video_file', 'uploaded_at')

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Please provide both username and password.")
        
        return data
    

class TitleSubtitleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleSubtitleModel
        fields = '__all__'