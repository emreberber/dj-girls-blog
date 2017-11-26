from django.shortcuts import render, HttpResponse

# Create your views here.


def home_view(request):  # request yerine baska isim verebiliriz
    if request.user.is_authenticated():  # Kullanici siteye giris yamis ise
        context = {
            'isim': 'Emre',
        }
    else:
        context = {
            'isim': 'Misafir',
        }
    return render(request, 'home.html', context)
