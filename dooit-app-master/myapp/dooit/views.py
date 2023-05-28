from .forms import LoginForm, RegisterForm, TransaksiForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dooit.models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()

    return render(request, 'login_pengguna.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print('errornya :', form.errors)
        print(form.data)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register_pengguna.html', {'form': form})

@login_required
def dashboard_view(request):
    semua_pengguna = User.objects.all()
    context = {'daftar_pengguna': semua_pengguna}
    return render(request, 'dashboard_pengguna.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib import messages
def transaksi_view(request):
    if request.method == 'POST':
        transaksi_form = TransaksiForm(request.POST)
        if transaksi_form.is_valid():
            transaksi_form.save()
            messages.success(request, ('Transaksi Berhasil'))
        else:
            messages.error(request, 'Error saving form')
        return redirect('dashboard')
    transaksi_form = TransaksiForm()
    context = {
        'transaksi_form' : transaksi_form,
    }
    return render(request, 'transaksi.html',context)
