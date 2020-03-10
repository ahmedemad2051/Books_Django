from django.urls import path
import books
from books.views import *

urlpatterns = [
    path('', index, name="home"),
    path('<int:book_id>', show, name = "show_book"),
]
