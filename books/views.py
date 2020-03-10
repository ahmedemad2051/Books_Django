from django.shortcuts import render
import json
import os
from books.models import Book

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.
def index(request):
    # with open(BASE_DIR + "/books/books.txt") as books_file:
    #     data = json.load(books_file)
    #     books = data["books"]
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "books/index.html", context)


def show(request, book_id):
    context = {}
    # with open(BASE_DIR + "/books/books.txt") as books_file:
    #     data = json.load(books_file)
    #
    # for book in data["books"]:
    #     if book["id"] == book_id:
    #         context["book"] = book
    #         break
    # else:
    #     pass

    context["book"] = Book.objects.get(id=book_id)

    return render(request, "books/show.html", context)
