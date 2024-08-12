from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.username

class Kategori(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=True)

class Produk(models.Model):
    nama_produk = models.CharField(max_length=200, blank=True, null=True)
    gambar_produk = models.ImageField(upload_to='gambar/banner', blank=False, null=True)
    harga_beli = models.IntegerField(blank=True, null=True)
    harga_jual = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    kategori = models.ForeignKey(Kategori, null=True, blank=True, related_name="produks", on_delete=models.SET_NULL)

class TransaksiPenjualan(models.Model):
    Status = (('Baru', 'Baru'), ('Lunas', 'Lunas'))
    no_transaksi = models.CharField(max_length=200, blank=False, null=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, related_name="transaksi_penjualan_customers", on_delete=models.SET_NULL)
    total_transaksi = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=200, default="Baru", blank=True, null=True, choices=Status)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tanggal_penjualan = models.DateTimeField(null=True, blank=False)

class DetailTransaksiPenjualan(models.Model):
    transaksi_penjualan = models.ForeignKey(TransaksiPenjualan, null=True, on_delete=models.CASCADE, related_name='detail_penjualans')
    produk = models.ForeignKey(Produk, null=True, on_delete=models.SET_NULL, related_name="transaksi_penjualan_produk")
    jumlah = models.IntegerField(blank=True, null=True)


class TransaksiPembelian(models.Model):
    Status = (('Baru', 'Baru'), ('Lunas', 'Lunas'))
    no_transaksi = models.CharField(max_length=200, blank=False, null=True)
    nama_suplayer = models.CharField(max_length=200, blank=False, null=True)
    total_transaksi = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=200, default="Baru", blank=True, null=True, choices=Status)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tanggal_kulakan = models.DateTimeField(null=True, blank=False)

class DetailTransaksiPembelian(models.Model):
    transaksi_pembelian = models.ForeignKey(TransaksiPembelian, null=True, on_delete=models.CASCADE, related_name='detail_pembelians')
    produk = models.ForeignKey(Produk, null=True, on_delete=models.SET_NULL, related_name="transaksi_pembelian_produk")
    jumlah = models.IntegerField(blank=True, null=True)

