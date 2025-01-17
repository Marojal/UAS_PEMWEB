import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

x = datetime.datetime.now()

class Katagori(models.Model):
    list_kateg = models.CharField(max_length=100)

    def __str__(self):
        return self.list_kateg

    class Meta:
        verbose_name_plural = '1. Kategori'

class Artikel(models.Model):
    judul = models.CharField(max_length= 100)
    isi = RichTextUploadingField (
        config_name='special',
        external_plugin_resources=[(
            'youtube',
            'https://minio.umkt.ac.id/simpelv2-static/ckeditor_plugins/youtube/youtube/',
            #'http://localhost:8000/static/ckeditor_plugins/youtube/youtube/',
            'plugin.js',
            )],
            blank=True,
            null=True
            )
    kategori = models.ForeignKey(Katagori, on_delete=models.SET_NULL,blank=True , null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True ,null= True)
    thumbnail = models.ImageField(upload_to='artikel',blank=True, null=True)

    create_at =models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True,null=True)

    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{x.year}-{x.month}-{x.day}-{self.judul}')
        super(Artikel, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = '2. Artikel'
