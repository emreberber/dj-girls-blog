from django.db import models

# Create your models here.


class Post(models.Model):  # Class isimleri (Post) her zaman buyuk harfle baslamalidir
    # Daha fazla field için django dökümantasyonunda Field Types kısmına bak
    title = models.CharField(max_length=120,verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    publishing_date = models.DateTimeField(verbose_name="Publishing Date")
    # verbose_name panelde gözükmesi istediğimiz isim

    def __str__(self):  # Bu özel fonksiyon ile panelde postların title ları gözükecek
        return self.title


