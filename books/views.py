
from books.apps import BooksConfig
from books.models import Book
from django.conf import settings
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.conf import path
#import json

#booksData = open(
    #'/Users/syedmohammadhamza/Desktop/ISK_Coding /bookstore_project/educational_Website/books.json').read()

#data = json.loads(booksData)



def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request,'books/index.html',context)



def show(request,id):

   
    singleBook = get_object_or_404(Book,pk=id)
    

    #singleBook  = list()
    #for book in data:
        #if book['id'] == id:
            #singleBook = book

    context = {'book': singleBook}
    return render(request,'books/show.html',context)



