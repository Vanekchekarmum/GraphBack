from rest_framework import serializers
from .models import Graph
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph
        fields = ["task", "completed", "timestamp", "updated", "user"]