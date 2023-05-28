from django.contrib import admin
from .models import User, Saldo, Kategori, Transaksi

@admin.register(Saldo)
class PenggunaDooit(admin.ModelAdmin):
    list_display = ('id_pengguna', 'saldo')
    raw_id_fields = ('id_pengguna',)
    
@admin.register(Kategori)
class KategoriDooit(admin.ModelAdmin):
    list_display = ('nama_kategori', 'keterangan')
    search_fields = ('nama_kategori', 'keterangan')

@admin.register(Transaksi)
class TransaksiDooit(admin.ModelAdmin):
    list_display = ('pengguna', 'kategori', 'tanggal_transaksi', 'jenis_transaksi', 'nominal', 'deskripsi')
    raw_id_fields = ('pengguna', 'kategori')
    search_fields = ('pengguna', 'kategori', 'deskripsi')

