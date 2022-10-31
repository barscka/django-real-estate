from importlib.metadata import files
from rest_framework import serializers

from .models import Enquirty


class EnquirtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquirty
        fields = "__all__"
