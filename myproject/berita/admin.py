from django.contrib import admin
from berita.models import Katagori, Artikel

# Register your models here.

admin.site.register(Katagori)

class ArtikelAdmin(admin.ModelAdmin):
    list_display=['judul','kategori','author']
    search_fields = ['judul']
admin.site.register(Artikel,ArtikelAdmin)


