from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Book
from .forms import BookForm
import requests
from .importBooks import importBook

def homepage(request):
    books = Book.objects.all()
    return render(request, "booksapp/home.html", {"books": books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "booksapp/book_detail.html", {"book": book})

def search(request):
    title = request.GET.get("title")
    authors = request.GET.get("authors")
    language = request.GET.get("language")
    results = Book.objects.filter(Q(title__icontains=title),
                                  Q(authors__icontains=authors),
                                  Q(language__icontains=language))     
    return render(request, "booksapp/home.html", {"books": results})

def book_add(request):
    # When method == POST create filled form
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect("booksapp:book_detail", pk=book.pk)

    # When method == GET create new clean form
    else:
        form = BookForm()
        return render(request, "booksapp/book_add.html", {"form": form})


def book_import(request):
    if request.method == "POST":
        apiKey = "AIzaSyCaMMhH6FhpWq1--hDsEfCZTP0NV_5CkIc"
        if request.POST.get("add") == None:
            search = request.POST.get("search1")
        else:
            search = request.POST.get("search2")
        wholeQuery = {"q": search, "key": apiKey}
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes", params=wholeQuery)        
        imported = response.json()
        all_results = importBook(imported)

        if request.POST.get("add") != None:
            id = request.POST.get("add")
            for i in all_results:
                if i["id"] == id:
                    del i["id"]
                    add_book = Book(**i)
                    add_book.save()
                    break
            return redirect("booksapp:book_detail", pk=add_book.pk)
        else:
            return render(request, "booksapp/book_import.html", {"all_results": all_results, "last": search})
    else:
        return render(request, "booksapp/book_import.html", {})

