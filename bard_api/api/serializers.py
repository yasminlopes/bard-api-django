from rest_framework import serializers

class BardApiSerializer(serializers.Serializer):
    response = serializers.CharField()