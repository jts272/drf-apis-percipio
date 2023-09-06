from rest_framework import serializers

from .models import Actor


class ActorSerializer(serializers.ModelSerializer):
    # Database store the path to the image, not the image itself
    # Serialize it like so
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Actor
        fields = "__all__"
