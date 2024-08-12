from django.urls import path
from . import views 
# from .decorators import login_perlindungan
from django.contrib.auth import views as auth_views


urlpatterns = [

# URL untuk login admin dengan trailing slash
    path('', views.user_login_admin, name='loginadmin'),
    path('beranda-admin/', views.beranda_admin, name='berandaadmin'),
    # kategori
    path('kategori-admin/', views.data_kategori, name='kategoriadmin'),
    path('kategori/tambah/', views.tambah_kategori, name='tambah_kategori'),
    path('kategori/edit/<int:kategori_id>/', views.edit_kategori, name='edit_kategori'),
    path('kategori/hapus/<int:kategori_id>/', views.delete_kategori, name='delete_kategori'),



    path('produk-admin/', views.data_produk, name='produkadmin'),
    path('produk/tambah/', views.tambah_produk, name='tambah_produk'),
    path('produk/edit/<int:produk_id>/', views.edit_produk, name='edit_produk'),
    path('produk/hapus/<int:produk_id>/', views.delete_produk, name='delete_produk'),

    path('data-outlet/', views.data_customer, name='customeradmin'),
    path('update-outlet/<int:customer_id>/', views.update_customer, name='update_customer'),
    path('create-outlet/', views.create_customer, name='create_customer'),
    path('delete-outlet/<int:customer_id>/', views.delete_customer, name='delete_customer'),

    path('data-transaksi-penjualan/', views.data_transaksi_penjualan, name='penjualanadmin'),
    path('penjualan/<int:pk>/delete/', views.delete_penjualan, name='delete_penjualan'),
    path('penjualan/<int:pk>/cetak_struk/', views.cetak_struk, name='cetak_struk'),
    path('update-status/<int:penjualan_id>/', views.update_status, name='update_status'),

    path('data-transaksi-pembelian/', views.data_transaksi_pembelian, name='pembelianadmin'),
    path('tambah_pembelian/', views.tambah_pembelian, name='tambah_pembelian'),
    path('simpan_pembelian/', views.simpan_pembelian, name='simpan_pembelian'),

    path('regresilinear/', views.sales_data_view, name='regresilinear'),
    # path('regresilinear/', views.regresi_linear_view, name='regresilinear'),
    path('logout/', auth_views.LogoutView.as_view(next_page='loginadmin'), name='logoutadmin'),


]
