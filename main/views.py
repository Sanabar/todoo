from django.shortcuts import render, HttpResponse
from .models import ToDo, Book

# Create your views here.
def outdata(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def added(request):
    return render(request, "added.html")

def edit(request):
    return render(request, "Edit.html")

def deleted(request):
    return render(request, "deleted.html")


def third(request):
    return HttpResponse("This is page test3")