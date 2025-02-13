from django.contrib import admin
from reviewapp.models import Review  # 추가한 라인

# Register your models here.
admin.site.register(Review)