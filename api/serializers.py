from rest_framework import serializers

class DepremSerializer(serializers.Serializer):
    tarih = serializers.CharField()
    saat = serializers.CharField()
    enlem = serializers.FloatField()
    boylam = serializers.FloatField()
    derinlik = serializers.FloatField()
    md = serializers.FloatField()
    ml = serializers.FloatField()
    mw = serializers.FloatField()
    yer = serializers.CharField()
    nitelik = serializers.CharField()