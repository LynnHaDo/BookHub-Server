from django.urls import path

from .views import ImportBooksAPIView, BookList

urlpatterns = [
    path('import-books', ImportBooksAPIView.as_view()),
    path('get-books', BookList.as_view())
    #path('get-books/<int:id>/', )
]