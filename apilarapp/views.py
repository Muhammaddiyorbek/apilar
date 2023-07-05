from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .seralizers import *
from rest_framework import generics, status
from .models import *

# Create your views here.
# ------------------------------------------
class Book(APIView):
    def get(self,request):
        books=Books.objects.all()
        serializer_data=BookSeralizer(books,many=True).data
        data={
            'status':f"Returned {books.count()} books",
            'books':serializer_data
        }
        return Response(data)

class BooksListApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSeralizer

# ------------------------------------------
# class BooksDetailApiView(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSeralizer

class BooksDetailApiView(APIView):
    def get(self,request,pk):
        try:
            book=Books.objects.get(id=pk)
            serialzer_data=BookSeralizer(book).data
            data={
                'status':f'Books detail {pk}',
                'book':serialzer_data
            }
            return Response(data,status=status.HTTP_200_OK)
        except:
            return Response(
                {'status':'Detail Not Found',
                 'message':'Book is not found'},status=status.HTTP_404_NOT_FOUND
            )


# ------------------------------------------
# class BooksDeleteApiView(generics.DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSeralizer


class BooksDeleteApiView(APIView):
    def delete(self,request,pk):
        try:
            Books.objects.get(id=pk).delete()
            return Response(
                {'status':'Delete',
                 'message':'Success delete'},status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'status':False,
                 'message':'Book is not found'},status=status.HTTP_404_NOT_FOUND
            )


# ------------------------------------------
# class BooksUpdateApiView(generics.UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSeralizer

class BooksUpdateApiView(APIView):
    def put(self,request,pk):
        data=request.data
        book=Books.objects.get(id=pk)
        serialser=BookSeralizer(instance=book,data=data,partial=True)
        if serialser.is_valid():
            book_save=serialser.save()
            return Response(
                {'status':True,
                 'message':'success update',
                 'book':data}
            )




# ------------------------------------------
# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSeralizer

class BookCreateApiView(APIView):
    def post(self,request):
        data=request.data
        seralizer=BookSeralizer(data=data)
        if seralizer.is_valid():
            book=seralizer.save()
            data={
                'status':'Book saved to database',
                'book':data
            }
            return Response(data)
        else:
            return Response({'errors': seralizer.errors},status=status.HTTP_400_BAD_REQUEST)
# ------------------------------------------

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSeralizer
# ------------------------------------------
class BookViewset(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSeralizer


# def orqali api yaratish
# @api_view(["GET"])
# def book_list_view(request,*args,**kwargs):
#     book=Books.objects.all()
#     seralizer=BookSeralizer(book,many=True)
#     return Response(seralizer.data)