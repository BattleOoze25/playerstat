from rest_framework import serializers
from . models import (Player, Score)
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields ='__all__'
