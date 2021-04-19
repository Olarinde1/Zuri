from django.shortcuts import render
from django.http import HttpResponse
from .models import Bookstore
# Create your views here.

def home_view(request):
    book = Bookstore.objects.get(year_published=2030)
    book_author = Bookstore.objects.get(book_author="Chinua Achebe")
    return render(request, "home.html",{"book": book, 'book_author':book_author})