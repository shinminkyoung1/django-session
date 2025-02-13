from rest_framework.response import Response  
from rest_framework.decorators import api_view  # 추가된 라인
from bookapp.models import Book
from bookapp.serializers import BookSerializer 

@api_view()  # 어떤 HTTP Method 받을지 명시. default: GET
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view()
def book_details(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)