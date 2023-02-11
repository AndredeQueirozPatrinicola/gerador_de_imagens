from rest_framework import serializers



class ImageSerializer(serializers.Serializer):
    url = serializers.CharField()


class ErroSerializer(serializers.Serializer):
    status_code = serializers.IntegerField()
    detail = serializers.CharField()