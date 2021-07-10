from rest_framework import serializers
from .models import Rower


class RowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rower
        fields = ("id", "nazwa", "data_dodania")