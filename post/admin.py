from django.contrib import admin
from .models import Post  # .models in önündeki nokta aynı dizinde olduğumuz için
# from post.models import Post şeklinde de tanımlayabilirdik


# Register your models here.

admin.site.register(Post)  # Post modelimiz artık admin panelinde gözükecek
