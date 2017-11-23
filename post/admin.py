from django.contrib import admin
from .models import Post  # .models in önündeki nokta aynı dizinde olduğumuz için
# from post.models import Post şeklinde de tanımlayabilirdik


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "publishing_date"]  # Post'da hangileri gozuksun ?
    list_display_links = ["title", "publishing_date"]  # Hangilerine link ozelligi verilsin ?
    list_filter = ["publishing_date"]  # Sag kenarda filtreleme kutucugu neye gore filtrelesin ?
    search_fields = ["title", "content"]  # Arama kutucugu neye gore arama yapsin ?


admin.site.register(Post, PostAdmin)  # Post modelimiz artık admin panelinde gözükecek.PostAdmini de ekledik !
