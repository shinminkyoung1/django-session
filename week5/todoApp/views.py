from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Todo, User
from .serializers import TodoSerializer

# Create your views here.
class Todos(APIView):

  def get_user(self, user_id):
    try:
      user = User.objects.get(id=user_id)
    except User.DoesNotExist:
      raise NotFound("유저를 찾을 수 없습니다.")
    return user

  def get(self, request, user_id):
    # month와 day 쿼리 파라미터로 받아서 필터링
    now = timezone.localtime(timezone.now())
    current_month = now.month
    current_day = now.day
    
		# 쿼리 파라미터에 "month"값이 없으면, 디폴트 값으로 current_month 가져옴
    month = request.query_params.get("month", current_month)
    month = int(month)

    day = request.query_params.get("day", current_day)
    day = int(day)

    user = self.get_user(user_id)
    todos = Todo.objects.filter(
      date__month=month,
      date__day=day,
      user=user
    )
    serializer = TodoSerializer(
      todos,
      many=True
    )
    return Response(serializer.data)
  
  def post(self, request, user_id):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
      user = self.get_user(user_id)
      serializer.save(
        user=user
      )
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
