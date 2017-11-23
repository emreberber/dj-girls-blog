from django.db import models

# Create your models here.


class Post(models.Model):  # Class isimleri (Post) her zaman büyük harfle başlamalıdır
    # Daha fazla field için django dökümantasyonunda Field Types kısmına bak
    title = models.CharField(max_length=120,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    publishing_date = models.DateTimeField(verbose_name="Yayımlanma Tarihi")
    # verbose_name panelde gözükmesi istediğimiz isim

    def __str__(self):  # Bu özel fonksiyon ile panelde postların title ları gözükecek
        return self.title


