from rest_framework import serializers
from reviewapp.models import Review 
from bookapp.serializers import BookSerializer  # 추가한 라인

class BookReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"


