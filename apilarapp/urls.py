from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('books',BookViewset,basename='books')

urlpatterns=[
    # path('book/',Book.as_view()),
    # path('books/',BooksListApiView.as_view()),
    # path('books/detail/<int:pk>/',BooksDetailApiView.as_view()),
    # path('books/delete/<int:pk>/',BooksDeleteApiView.as_view()),
    # path('books/update/<int:pk>/',BooksUpdateApiView.as_view()),
    # path('books/create/',BookCreateApiView.as_view()),
    # path('books/list/create/',BookListCreateApiView.as_view()),
]

urlpatterns=urlpatterns+router.urls
