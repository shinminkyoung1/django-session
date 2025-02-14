from django.contrib import admin
from .models import Todo  # 추가한 라인

# Register your models here.
admin.site.register(Todo)