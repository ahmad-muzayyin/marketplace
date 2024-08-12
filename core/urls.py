from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),

    
    path('kategori/', views.kategori, name='kategori'),
    path('keranjang/', views.keranjang, name='keranjang'),
    # Definisikan URL lainnya sesuai kebutuhan
    path('register/', views.register, name='register'),
    path('login/', views.customer_login, name='login'),  # Perbaiki di sini
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # path('produk/<int:kategori_id>/', views.produk_by_kategori, name='produk_by_kategori'),
    # path('tambah_ke_keranjang/<int:product_id>/', views.tambah_ke_keranjang, name='tambah_ke_keranjang'),

    path('produk/<int:kategori_id>/', views.produk_by_kategori, name='produk_by_kategori'),
    path('tambah_ke_keranjang/<int:product_id>/', views.tambah_ke_keranjang, name='tambah_ke_keranjang'),


    path('update_session/', views.update_session, name='update_session'),
    path('hapus_item/', views.hapus_item, name='hapus_item'),
    path('checkout/', views.checkout, name='checkout'),  # Define the checkout URL
    path('transaction-history/', views.transaction_history, name='transaction_history'),

]

