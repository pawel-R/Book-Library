from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


from ..models import Book
from .serializers import BookSerializer


# Show list of books.
class ApiBookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields =  ("title", "authors", "language", "publishedDate")
    ordering_fields  =  ("id", "title", "authors", "language", "publishedDate")


# Show details of book.
@api_view(["GET", ])
def api_detail(request, pk):

    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)
    return Response(serializer.data)
    
# Update the book. Works only in Postman. 
@api_view(["PUT", ])
def api_update(request, pk):

    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {"success": "update successful"}
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete the book.
@api_view(["DELETE", ])
def api_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    operation = book.delete()
    if operation:
        data = {"success": "delete successful"}
    else:
        data = {"failure": "delete failed"}
    return Response(data=data)


# Add new book. Works only in Postman. Form is missing I guess.
@api_view(["POST", ])
def api_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

