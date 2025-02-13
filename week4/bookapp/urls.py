from django.urls import path
from bookapp import views

urlpatterns = [
    path('', views.BookListView.as_view()),
    path('<int:id>/', views.BookDetailsView.as_view()),
    path('<int:id>/reviews/', views.BookReviewListView.as_view()),
]