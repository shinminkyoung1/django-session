from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

  user = serializers.StringRelatedField(read_only=True)  # 아래 부연 설명 참고
  todo_id = serializers.IntegerField(source='id', read_only=True)  # 아래 부연 설명 참고

  class Meta:
    model = Todo
    fields = [
      'todo_id',
      'user',
      'date',
      'content',
      'is_checked',
      'emoji',
    ]