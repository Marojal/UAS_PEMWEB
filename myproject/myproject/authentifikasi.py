from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password

@csrf_protect
def akun_login(request):
    # Cek jika pengguna sudah terautentikasi
    if request.user.is_authenticated:
        return redirect('/')
    
    template_name = "halaman/login.html"
    pesan = ''
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            pesan = "Login Gagal"
    
    # Pastikan konteks terbentuk dan di-render dalam kedua kasus (GET dan POST)
    context = {
        'pesan': pesan
    }
    return render(request, template_name, context)


def akun_registrasi(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    pesan = ''
    template_name = "halaman/registrasi.html"
    
    if request.method == "POST":
        username = request.POST.get('username')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).count() == 0:
                User.objects.create(
                    username=username,
                    first_name=nama_depan,
                    last_name=nama_belakang,
                    email=email,
                    password=make_password(password1), # type: ignore
                    is_active=True
                )
                return redirect('/')      
            else:
                pesan = 'Username sudah ada'
        else:
            pesan = 'Password tidak sama'
    
    context = {
        'pesan': pesan
    }
    return render(request, template_name, context)

def akun_logout(request):
    logout(request)
    return redirect('/')