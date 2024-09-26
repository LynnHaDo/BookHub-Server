from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from scripts import import_books

from .models import Book 

from .serializers import BookSerializer

# Create your views here.
class ImportBooksAPIView(APIView):
    def post(self, request):
        file_path = request.data['file_path']
        if file_path is None:
            render("File path does not exist", status=500)
            return

        try:
            import_books.run(file_path)
        except ValueError as e:
            render(f"Failure to import books. Error: {e}", status=500)

class BookList(ListCreateAPIView):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer
    #permission_classes = [IsAdminUser]

    def list(self, request):
        query_set = self.get_queryset()
        serializer = BookSerializer(query_set, many=True)
        return Response(serializer.data)

