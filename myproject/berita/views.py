from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test

from berita.models import Katagori,Artikel
from berita.forms import ArtikelForm

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    template_name = "dashboard/index.html"
    context = {
        'title' : 'Halaman Dashboard'
    }

    return render(request,template_name,context)

@login_required
@user_passes_test(is_operator, login_url='/authentifikasi/logout')
def kategori_list(request):
    template_name = "dashboard/snippets/kategori_list.html"
    katagori= Katagori.objects.all()
    print(katagori)
    context = {
        'title' : 'Halaman Kategori',
        'katagori' : katagori
    }

    return render(request,template_name,context)

@login_required
@user_passes_test(is_operator, login_url='/authentifikasi/logout')
def kategori_add(request):
    template_name = "dashboard/snippets/kategori_add.html"
    if request.method == "POST":
        new_list_kateg = request.POST.get('nama_kategori')
        Katagori.objects.create(
            kategori = new_list_kateg
            )
        return redirect(kategori_list)
    context = {
        'title' : 'Tambah Kategori',
    }
    return render(request,template_name,context)

@login_required
@user_passes_test(is_operator, login_url='/authentifikasi/logout')
def kategori_update(request, id_katagori):
    template_name = "dashboard/snippets/kategori_update.html"
    try:
        up_kategori = Katagori.objects.get(id=id_katagori)
    except:
        return(kategori_list)
    if request.method == "POST":
        new_kategori = request.POST.get('nama_kategori')
        up_kategori.list_kateg = new_kategori
        up_kategori.save()
        return redirect(kategori_list)
    context = {
        'title' : 'Tambah Kategori',
        'up_kategori' : up_kategori
    }
    return render(request,template_name,context)

def kategori_delete(request, id_katagori):
    try:
        Katagori.objects.get(id=id_katagori).delete()
    except:
        pass
    return redirect(kategori_list)

@login_required
def artikel_list(request):
    template_name = "dashboard/snippets/artikel_list.html"

    if request.user.groups.filter(name='Operator'):
        artikel = Artikel.objects.all()
    else:
        artikel = Artikel.objects.filter(author=request.user)

    context = {
        'title' : 'daftar artikel',
        'artikel' : artikel
    }
    return render(request,template_name,context)

@login_required
def artikel_add(request):
    print(request.user)
    template_name ="dashboard/snippets/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES)
        if forms.is_valid:
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
        else:
            print(forms.error_class)
    forms = ArtikelForm()
    context ={
        'title' : 'Tambah Artikel Baru',
        'forms' : forms
    }
    return render(request,template_name,context)

@login_required
def artikel_detail(request, id_artikel):
    template_name = "dashboard/snippets/artikel_detail.html"
    artikel = Artikel.objects.get(id=id_artikel)
    context = {
        'title' : artikel.judul,
        'artikel': artikel
    }
    return render(request,template_name,context)

@login_required
def artikel_update(request, id_artikel):
    template_name = "dashboard/snippets/artikel_forms.html"
    artikel = Artikel.objects.get(id=id_artikel)

    if request.user.groups.filter(name='Operator'):
        pass
    else:
        if artikel.author != request.user:
            return redirect('/')

    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid:
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
    forms = ArtikelForm(instance=artikel)
    context ={
        'title' : 'Edit Artikel Baru',
        'forms' : forms
    }
    return render(request,template_name,context)

@login_required
def artikel_delete(request, id_artikel):
    try:
        artikel = Artikel.objects.get(id=id_artikel)
        if request.user.groups.filter(name='Operator'):
            pass
        else:
            if artikel.author != request.user:
                return redirect('/')
            artikel.delete()
            
    except:
        pass
    return redirect(artikel_list)