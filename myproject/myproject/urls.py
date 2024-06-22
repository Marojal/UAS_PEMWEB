
from django.contrib import admin
from django.urls import path, include

#
from django.conf import settings
from django.conf.urls.static import static

from myproject.views import home,about,detail_artikel,contact
from myproject.authentifikasi import akun_login,akun_registrasi,akun_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),

    path('contact', contact, name="contact"),
    path('about', about, name="about"),
    path('detail_artikel/<slug:slug>', detail_artikel, name="detail_artikel"),
    path('dashboard/',include('berita.urls')),

    path('authentifikasi/login',akun_login, name="akun_login"),
    path('authentifikasi/regitrasi',akun_registrasi, name="akun_registrasi"),
    path('authentifikasi/logout',akun_logout, name="akun_logout"),

    path('ckeditor/',include('ckeditor_uploader.urls')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)