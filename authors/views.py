from django.shortcuts import render, redirect
from authors.models import Author


# Create your views here.
def profile(request, author_id):
    author = Author.objects.get(id=author_id)
    if not author:
        return redirect("home")
    return render(request, "authors/index.html", {"author": author})
