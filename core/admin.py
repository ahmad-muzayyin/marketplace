from django.contrib import admin
from .models import Kategori, Produk, Customer, TransaksiPenjualan, DetailTransaksiPenjualan

# Register your models here.
admin.site.register(Kategori)
admin.site.register(Produk)
# admin.site.register(Transaksi_pembelian)
# admin.site.register(DetailTransaksi_pembelian)
admin.site.register(Customer)
admin.site.register(TransaksiPenjualan)
admin.site.register(DetailTransaksiPenjualan)
