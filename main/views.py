from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("hello world!")

def test(request):
    return render(request, "test.html")

def third(request):
    return HttpResponse("This is page test3")