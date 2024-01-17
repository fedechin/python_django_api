from api.models import Joke
from rest_framework import serializers

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = '__all__'

    def get_url_with_id(self, obj):
        return f"{obj.url}/{obj.id}"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['url'] = self.get_url_with_id(instance)
        return representation