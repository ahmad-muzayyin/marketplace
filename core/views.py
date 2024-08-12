import json
from .models import Kategori, Produk,TransaksiPenjualan, DetailTransaksiPenjualan
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm
from django.http import JsonResponse
from django.contrib import messages
import logging
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone
import requests
logger = logging.getLogger(__name__)
def home(request):
    daftar_kategori = Kategori.objects.all()
    return render(request, 'core/home.html', {'daftar_kategori': daftar_kategori})
def kategori(request):
    return render(request, 'core/kategori.html')

def update_cart(request, produk_id):
    if request.method == 'POST':
        jumlah = int(request.POST.get('jumlah', 1))
        produk = get_object_or_404(Produk, id=produk_id)

        keranjang = request.session.get('keranjang', {})
        if produk_id in keranjang:
            keranjang[produk_id]['jumlah'] = jumlah
            keranjang[produk_id]['subtotal'] = jumlah * produk.harga_jual
        request.session['keranjang'] = keranjang

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def remove_from_cart(request, produk_id):
    if request.method == 'POST':
        keranjang = request.session.get('keranjang', {})
        if produk_id in keranjang:
            del keranjang[produk_id]
            request.session['keranjang'] = keranjang
            return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def get_total_price(request):
    total_harga = 0
    keranjang = request.session.get('keranjang', {})
    for produk_id, item in keranjang.items():
        produk = Produk.objects.get(id=produk_id)
        subtotal = item['jumlah'] * produk.harga_jual
        total_harga += subtotal
    return JsonResponse({'total_harga': total_harga})
    
    

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

def customer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Username atau password salah')
        else:
            messages.error(request, 'Username atau password salah')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def profile(request):
    daftar_kategori = Kategori.objects.all()
    return render(request, 'core/profile.html', {'daftar_kategori': daftar_kategori})

def produk_by_kategori(request, kategori_id):
    daftar_kategori = Kategori.objects.all()
    kategori = Kategori.objects.get(id=kategori_id)
    produk = Produk.objects.filter(kategori=kategori)
    return render(request, 'core/produk_by_kategori.html', {'produk': produk, 'daftar_kategori': daftar_kategori, 'kategori': kategori})

def tambah_ke_keranjang(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Produk, pk=product_id)
        jumlah_qty = int(request.POST.get('jumlah_qty', 0))

        # Validasi jumlah yang diminta tidak melebihi stok
        if jumlah_qty > product.stock:
            error_message = "Jumlah yang diminta melebihi stok yang tersedia."
            return render(request, 'core/produk_by_kategori.html', {'error_message': error_message, 'produk': Produk.objects.filter(kategori=product.kategori), 'kategori': product.kategori})

        # Ambil keranjang dari sesi atau buat keranjang baru jika belum ada
        keranjang = request.session.get('keranjang', {})

        # Jika produk sudah ada di keranjang, tambahkan jumlahnya
        if str(product_id) in keranjang:
            keranjang[str(product_id)]['jumlah'] += jumlah_qty
        else:
            subtotal = jumlah_qty * product.harga_jual
            keranjang[str(product_id)] = {'jumlah': jumlah_qty, 'subtotal': subtotal}

        # Simpan keranjang kembali ke sesi
        request.session['keranjang'] = keranjang

        # Tetap di halaman yang sama
        return redirect('produk_by_kategori', kategori_id=product.kategori.id)
    else:
        return redirect('produk_by_kategori', kategori_id=product.kategori.id)
# def produk_by_kategori(request, kategori_id):
#     daftar_kategori = Kategori.objects.all()
#     kategori = Kategori.objects.get(id=kategori_id)
#     produk = Produk.objects.filter(kategori=kategori)
#     return render(request, 'core/produk_by_kategori.html', {'produk': produk, 'daftar_kategori': daftar_kategori})

# def tambah_ke_keranjang(request, product_id):
#     if request.method == 'POST':
#         try:
#             product = Produk.objects.get(pk=product_id)
#             jumlah_qty = int(request.POST.get('jumlah_qty', 0))  
#             if jumlah_qty > product.stock:
#                 error_message = "Jumlah yang diminta melebihi stok yang tersedia."
#                 return render(request, 'produk_by_kategori.html', {'error_message': error_message, 'produk': Produk.objects.all()})
            
#             subtotal = jumlah_qty * product.harga_jual
            
#             keranjang = request.session.get('keranjang', {})
#             keranjang[product_id] = {'jumlah': jumlah_qty, 'subtotal': subtotal}  # Simpan jumlah dan subtotal
#             request.session['keranjang'] = keranjang
#             return redirect('keranjang')
#         except Produk.DoesNotExist:
#             return redirect('keranjang')
#     else:
#         return redirect('keranjang')

def keranjang(request):
    daftar_kategori = Kategori.objects.all()
    keranjang = request.session.get('keranjang', {})
    total_harga = 0
    items = []
    for product_id, data in keranjang.items():
        try:
            product = Produk.objects.get(pk=product_id)
            jumlah_qty = data['jumlah']
            subtotal = data['subtotal']
            total_harga += subtotal
            items.append({'id': product_id, 'product': product, 'jumlah_qty': jumlah_qty, 'subtotal': subtotal})
        except Produk.DoesNotExist:
            pass

    return render(request, 'core/keranjang.html', {'items': items, 'total_harga': total_harga,'daftar_kategori': daftar_kategori})

def update_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['productId']
        jumlah = data['jumlah']
        subtotal = data['subtotal']  # Ambil subtotal dari data yang dikirimkan
        keranjang = request.session.get('keranjang', {})
        keranjang[product_id] = {'jumlah': jumlah, 'subtotal': subtotal}  # Simpan jumlah dan subtotal
        request.session['keranjang'] = keranjang
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def hapus_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = str(data['productId'])  # Pastikan tipe data sesuai
        keranjang = request.session.get('keranjang', {})
        if product_id in keranjang:
            del keranjang[product_id]
            request.session['keranjang'] = keranjang
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})



from django.db.models import F

@login_required
def checkout(request):
    if request.method == 'POST':
        # Dapatkan data keranjang dari sesi
        keranjang = request.session.get('keranjang', {})
        
        # Buat instance TransaksiPenjualan baru
        customer = request.user
        total_transaksi = sum(item['subtotal'] for item in keranjang.values())
        status = 'Baru'
        date_created = timezone.now()
        tanggal_penjualan = timezone.now()
        no_transaksi = f'PJ-{TransaksiPenjualan.objects.count() + 1}'
        
        transaksi = TransaksiPenjualan.objects.create(
            customer=customer,
            total_transaksi=total_transaksi,
            status=status,
            date_created=date_created,
            tanggal_penjualan=tanggal_penjualan,
            no_transaksi=no_transaksi
        )
        
        # Perbarui stok produk dan buat instance DetailTransaksiPenjualan
        keranjang = request.session.get('keranjang', {})
        for product_id, data in keranjang.items():
            produk = Produk.objects.get(pk=product_id)
            jumlah = data['jumlah']
            
            # Kurangi jumlah yang terjual dari stok produk
            Produk.objects.filter(pk=product_id).update(stock=F('stock') - jumlah)
            
            DetailTransaksiPenjualan.objects.create(
                transaksi_penjualan=transaksi,
                produk=produk,
                jumlah=jumlah
            )
        
        # Kosongkan sesi keranjang setelah proses checkout berhasil
        request.session['keranjang'] = {}
        address = customer.address if hasattr(customer, 'address') else 'Alamat tidak tersedia'
        send_telegram_message(no_transaksi, tanggal_penjualan, customer,address, keranjang)
        return redirect('keranjang')  # Redirect ke halaman sukses checkout
    else:
        return redirect('keranjang')  # Redirect kembali ke keranjang jika diakses melalui permintaan GET
    
def send_telegram_message(no_transaksi, tanggal_penjualan, customer,address, keranjang):
    bot_token = settings.TELEGRAM_BOT_TOKEN     
    chat_id = settings.TELEGRAM_CHAT_ID
    
    # Membuat pesan
    message = f'Pesanan baru!\nNo Transaksi: {no_transaksi}\nTanggal: {tanggal_penjualan}\nNama Outlet: {customer}\nAlamat Outlet: {address}\n\nDetail Keranjang:\n'
    
    for product_id, jumlah in keranjang.items():
        produk = Produk.objects.get(pk=product_id)
        message += f'\nNama Barang: {produk.nama_produk}\nHarga: {produk.harga_jual}\nJumlah: {jumlah}\n'
    
    # Mengirim pesan ke Telegram
    telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"     
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "HTML"}    
    requests.post(telegram_api_url, data=payload)


def transaction_history(request):
    # Get the logged-in customer's transactions
    daftar_kategori = Kategori.objects.all()
    customer = request.user
    transactions = TransaksiPenjualan.objects.filter(customer=customer)

    # Get filter parameters
    bulan = request.GET.get("bulan")

    if bulan:
        try:
            year, month = map(int, bulan.split('-'))
            transactions = transactions.filter(date_created__year=year, date_created__month=month)
        except ValueError:
            pass  # Handle invalid month input

    return render(request, 'core/transaction_history.html', {'transactions': transactions, 'daftar_kategori': daftar_kategori, 'bulan': bulan})