from django.urls import path
from bookapp import views

urlpatterns = [
    path('', views.book_list),
    path('<int:id>/', views.book_details),
]