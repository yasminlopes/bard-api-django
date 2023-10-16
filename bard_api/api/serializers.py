from rest_framework import serializers

class RespostaSerializer(serializers.Serializer):
    resposta = serializers.CharField()