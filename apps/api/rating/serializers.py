from rest_framework import serializers
from apps.rating.models import Rating



class RatingListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", 'content', "rating", "recipient", "date_created"]
