from django.shortcuts import render, HttpResponse

# Create your views here.


def home_view(request):  # request yerine baska isim verebiliriz
    return HttpResponse("<b>Welcome to my dj project 101 </b>")  # urls.py de belirtmemiz gerekir
