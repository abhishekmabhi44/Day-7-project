from rest_framework import serializers


class JobSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    company = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)