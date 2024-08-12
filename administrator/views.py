
from django import template
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from core import models
from core.models import Customer, Kategori, Produk, TransaksiPenjualan,DetailTransaksiPenjualan,TransaksiPembelian,DetailTransaksiPembelian
from django.http import JsonResponse
from .forms import KategoriForm,ProdukForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.http import HttpResponse
from django.db.models import Max
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import numpy as np
from sklearn.linear_model import LinearRegression
from .forms import CustomerForm
from django.contrib import messages

from datetime import datetime
def user_login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Simpan username di dalam sesi
            request.session['username'] = username
            # Redirect ke halaman yang sesuai
            return redirect('berandaadmin')  # Ganti 'berandaadmin' dengan nama view yang sesuai
        else:
            # Tampilkan pesan error jika login gagal
            messages.error(request, 'Login tidak valid. Silakan periksa username dan password Anda.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
@login_required
def beranda_admin(request):
    # Mengambil jumlah entitas dari setiap model
    username = request.session.get('username')
    jumlah_customer = Customer.objects.count()
    jumlah_kategori = Kategori.objects.count()
    jumlah_produk = Produk.objects.count()
    jumlah_transaksi = TransaksiPenjualan.objects.count()

    # Menyiapkan konteks
    context = {
        'judul': 'Halaman Beranda',
        'menu':'berandaadmin',
        'username':username,
        'jumlah_customer': jumlah_customer,
        'jumlah_kategori': jumlah_kategori,
        'jumlah_produk': jumlah_produk,
        'jumlah_transaksi': jumlah_transaksi,
    }

    # Memuat template dan meneruskan konteks
    return render(request, 'beranda.html', context)

# menampilkan kategori
@login_required
def data_kategori(request):
    kategoris = Kategori.objects.all()
    context = {
        'judul': 'Halaman Kategori',
        'menu':'datakategori',
        'kategoris':kategoris,
    }

    return render(request, 'kategori_admin.html', context)
def tambah_kategori(request):
    if request.method == 'POST':
        form = KategoriForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kategoriadmin')
    else:
        form = KategoriForm()
    
    context = {
        'judul': 'Tambah Kategori',
        'menu':'datakategori',
        'form':form,
    }
    return render(request, 'kategori_admintambah.html', context)
def edit_kategori(request, kategori_id):
    kategori = Kategori.objects.get(id=kategori_id)
    if request.method == 'POST':
        form = KategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            return redirect('kategoriadmin')
    else:
        form = KategoriForm(instance=kategori)
    
    context = {
        'judul': 'Edit Kategori',
        'menu':'datakategori',
        'form':form,
        'kategori':kategori,
    }
    return render(request, 'kategori_adminedit.html', context)
def delete_kategori(request, kategori_id):
    kategori = Kategori.objects.get(id=kategori_id)
    if request.method == 'POST':
        kategori.delete()
        return redirect('kategoriadmin')
    context = {
        'judul': 'Hapus Kategori',
        'kategori': kategori,
    }
    return render(request, 'kategori_adminhapus.html', context)


# menampilkan produk
@login_required
def data_produk(request):
    nama_produk_query = request.GET.get('nama_produk')
    kategori_query = request.GET.get('kategori')
    sort_by_stock = request.GET.get('sort_by_stock')

    produks = Produk.objects.all()

    if nama_produk_query:
        produks = produks.filter(nama_produk__icontains=nama_produk_query)
    if kategori_query:
        produks = produks.filter(kategori__nama__icontains=kategori_query)

    if sort_by_stock:
        produks = produks.order_by('stock')

    kategoris = Kategori.objects.all()

    paginator = Paginator(produks, 10)
    page = request.GET.get('page')

    try:
        produks = paginator.page(page)
    except PageNotAnInteger:
        produks = paginator.page(1)
    except EmptyPage:
        produks = paginator.page(paginator.num_pages)

    context = {
        'judul': 'Halaman Produk',
        'menu': 'dataproduk',
        'produks': produks,
        'kategoris': kategoris,
    }

    return render(request, 'produk_admin.html', context)

def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produkadmin')
    else:
        form = ProdukForm()
    kategoris = Kategori.objects.all()
    context = {
        'judul': 'Tambah Produk',
        'menu':'dataproduk',
        'form':form,
        'kategoris':kategoris,
    }
    return render(request, 'produk_admintambah.html', context)

def edit_produk(request, produk_id):
    produk = Produk.objects.get(id=produk_id)
    if request.method == 'POST':
        form = ProdukForm(request.POST, request.FILES, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produkadmin')
    else:
        form = ProdukForm(instance=produk)
    kategoris = Kategori.objects.all()  # Mendapatkan daftar semua kategori

    context = {
        'judul': 'Edit Kategori',
        'menu':'dataproduk',
        'form':form,
        'produk': produk,
        'kategoris':kategoris,
    }
    return render(request, 'produk_adminedit.html', context)

def delete_produk(request, produk_id):
    produk = Produk.objects.get(id=produk_id)
    if request.method == 'POST':
        produk.delete()
        return redirect('produkadmin')
    context = {
        'judul': 'Hapus Produk',
        'produk': produk,
    }
    return render(request, 'produk_adminhapus.html', context)

@login_required
def data_customer(request):
    nama_customer_query = request.GET.get('nama_customer')
    
    # Mengambil semua customer kecuali superadmin
    customers = Customer.objects.exclude(is_superuser=True)
    
    if nama_customer_query:
        customers = customers.filter(name__icontains=nama_customer_query)
    
    paginator = Paginator(customers, 10)  # Menampilkan 10 customer per halaman
    page = request.GET.get('page')

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    context = {
        'judul': 'Halaman Outlet',
        'menu': 'datacustomer',
        'customers': customers,
    }

    return render(request, 'customer_admin.html', context)
@login_required
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customeradmin')
    else:
        form = CustomerForm()
    return render(request, 'create_customer.html', {'form': form})

@login_required
def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customeradmin')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'update_customer.html', {'form': form})
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customeradmin')
    return render(request, 'customer_adminhapus.html', {'customer': customer})


@login_required
def data_transaksi_penjualan(request):
    penjualan_list = TransaksiPenjualan.objects.all()
    query = request.GET.get("q")
    bulan = request.GET.get("bulan")

    if query:
        penjualan_list = penjualan_list.filter(customer__name__icontains=query)
    
    if bulan:
        try:
            # Extract year and month from input value
            year, month = map(int, bulan.split('-'))
            penjualan_list = penjualan_list.filter(tanggal_penjualan__month=month, tanggal_penjualan__year=year)
        except ValueError:
            pass  # Handle invalid month input

    paginator = Paginator(penjualan_list, 10)
    page = request.GET.get('page')

    try:
        penjualan_list = paginator.page(page)
    except PageNotAnInteger:
        penjualan_list = paginator.page(1)
    except EmptyPage:
        penjualan_list = paginator.page(paginator.num_pages)

    return render(request, 'transaksi_penjualan_admin.html', {'penjualan_list': penjualan_list, 'query': query, 'bulan': bulan})
def delete_penjualan(request, pk):
    penjualan = get_object_or_404(TransaksiPenjualan, pk=pk)
    if request.method == 'POST':
        penjualan.delete()
        return redirect('penjualanadmin')
    return render(request, 'transaksi_penjualan_delete.html', {'penjualan': penjualan})
@login_required
def update_status(request, penjualan_id):
    penjualan = get_object_or_404(TransaksiPenjualan, id=penjualan_id)
    penjualan.status = 'Selesai'
    penjualan.save()
    return redirect('penjualanadmin')
@login_required
def cetak_struk(request, pk):
    penjualan = get_object_or_404(TransaksiPenjualan, pk=pk)
    subtotal_list = []
    for detail in penjualan.detail_penjualans.all():
        subtotal = detail.produk.harga_jual * detail.jumlah
        subtotal_list.append(subtotal)
    total_transaksi = sum(subtotal_list)
    context = {'penjualan': penjualan, 'total_transaksi': total_transaksi}
    return render(request, 'cetak_struk.html', context)

@login_required
def data_transaksi_pembelian(request):
    pembelian_list = TransaksiPembelian.objects.all()

    # Pencarian berdasarkan nomor transaksi
    query = request.GET.get("q", '')
    bulan = request.GET.get("bulan")

    if query:
        pembelian_list = pembelian_list.filter(no_transaksi__icontains=query)

    if bulan:
        try:
            year, month = map(int, bulan.split('-'))
            pembelian_list = pembelian_list.filter(tanggal_kulakan__year=year, tanggal_kulakan__month=month)
        except ValueError:
            pass  # Handle invalid month input

    # Urutkan berdasarkan tanggal_kulakan
    pembelian_list = pembelian_list.order_by('tanggal_kulakan')

    paginator = Paginator(pembelian_list, 10)
    page = request.GET.get('page')

    try:
        pembelian_list = paginator.page(page)
    except PageNotAnInteger:
        pembelian_list = paginator.page(1)
    except EmptyPage:
        pembelian_list = paginator.page(paginator.num_pages)

    return render(request, 'transaksi_pembelian_admin.html', {'pembelian_list': pembelian_list, 'query': query, 'bulan': bulan})

def get_next_transaksi_penjualan_number():
    # Ambil nomor transaksi terakhir
    last_transaksi = TransaksiPenjualan.objects.all().aggregate(Max('no_transaksi'))['no_transaksi__max']

    # Jika belum ada nomor transaksi, mulai dari 1
    if not last_transaksi:
        return "Pb-1"

    # Ambil nomor urut dan tambahkan 1
    last_transaksi_number = int(last_transaksi.split('-')[1])
    next_transaksi_number = last_transaksi_number + 1

    return f"Pb-{next_transaksi_number}"

# def tambah_pembelian(request):
#     produk_list = Produk.objects.all()  # Ambil daftar produk untuk dipilih dalam form
#     return render(request, 'pembelian_tambah.html', {'produk_list': produk_list})
def tambah_pembelian(request):
    produk_list = Produk.objects.all()  # Ambil daftar produk untuk dipilih dalam form

    try:
        latest_transaksi = TransaksiPembelian.objects.latest('id')
        last_id = latest_transaksi.id
    except TransaksiPembelian.DoesNotExist:
        last_id = 0

    nomor_transaksi = f"Pb-{last_id + 1:04d}"  # Format nomor transaksi dengan 'Pb-' diikuti oleh nomor urut 4 digit

    return render(request, 'pembelian_tambah.html', {'produk_list': produk_list, 'nomor_transaksi': nomor_transaksi})

# def simpan_pembelian(request):
#     if request.method == 'POST':
#         no_transaksi = request.POST['no_transaksi']
#         nama_suplayer = request.POST['nama_suplayer']
#         tanggal_kulakan = request.POST['tanggal_kulakan']
        
#         # Simpan Transaksi Pembelian
#         transaksi_pembelian = TransaksiPembelian.objects.create(
#             no_transaksi=no_transaksi,
#             nama_suplayer=nama_suplayer,
#             tanggal_kulakan=tanggal_kulakan
#         )
        
#         # Simpan Detail Transaksi Pembelian
#         for key, value in request.POST.items():
#             if key.startswith('produk_'):
#                 index = key.split('_')[1]
#                 produk_id = value
#                 jumlah = request.POST['jumlah_' + index]
#                 if produk_id and jumlah:
#                     produk = Produk.objects.get(id=produk_id)
#                     DetailTransaksiPembelian.objects.create(
#                         transaksi_pembelian=transaksi_pembelian,
#                         produk=produk,
#                         jumlah=jumlah
#                     )
        
#         return redirect('penjualan_list')  # Redirect ke halaman lain setelah menyimpan data

#     return render(request, 'pembelian_tambah.html')

# def simpan_pembelian(request):
#     if request.method == 'POST':
#         # Ambil data dari formulir POST
#         no_transaksi = request.POST.get('no_transaksi')
#         nama_suplayer = request.POST.get('nama_suplayer')
#         tanggal_kulakan = request.POST.get('tanggal_kulakan')
        
#         # Pastikan tanggal_kulakan dalam format yang benar
#         try:
#             tanggal_kulakan = timezone.datetime.strptime(tanggal_kulakan, '%Y-%m-%d').date()
#         except ValueError:
#             # Jika format tanggal tidak valid, tampilkan pesan kesalahan atau lakukan penanganan sesuai kebutuhan Anda
#             return render(request, 'error.html', {'message': 'Format tanggal tidak valid.'})

#         # Lakukan simpan transaksi pembelian dan detail transaksi pembelian
#         transaksi_pembelian = TransaksiPembelian.objects.create(no_transaksi=no_transaksi, nama_suplayer=nama_suplayer, tanggal_kulakan=tanggal_kulakan)
        
#         # Simpan detail transaksi pembelian
#         for key, value in request.POST.items():
#             if key.startswith('produk_'):
#                 produk_id = key.split('_')[-1]
#                 jumlah = value
#                 # Simpan detail transaksi pembelian
#                 detail_pembelian = DetailTransaksiPembelian.objects.create(transaksi_pembelian=transaksi_pembelian, produk_id=produk_id, jumlah=jumlah)
        
#         # Redirect ke halaman yang sesuai setelah berhasil menyimpan transaksi
#         return redirect('penjualanadmin')

#     # Jika metode bukan POST, kembali ke halaman pembelian_tambah
#     return redirect('tambah_pembelian')

def simpan_pembelian(request):
    if request.method == 'POST':
        # Ambil data dari formulir POST
        no_transaksi = request.POST.get('no_transaksi')
        nama_suplayer = request.POST.get('nama_suplayer')
        tanggal_kulakan = request.POST.get('tanggal_kulakan')
        
        # Pastikan tanggal_kulakan dalam format yang benar
        try:
            tanggal_kulakan = timezone.datetime.strptime(tanggal_kulakan, '%Y-%m-%d').date()
        except ValueError:
            # Jika format tanggal tidak valid, tampilkan pesan kesalahan atau lakukan penanganan sesuai kebutuhan Anda
            return render(request, 'error.html', {'message': 'Format tanggal tidak valid.'})

        # Lakukan simpan transaksi pembelian dan detail transaksi pembelian
        transaksi_pembelian = TransaksiPembelian.objects.create(no_transaksi=no_transaksi, nama_suplayer=nama_suplayer, tanggal_kulakan=tanggal_kulakan)
        
        # Simpan detail transaksi pembelian
        for key, value in request.POST.items():
            if key.startswith('produk_'):
                index = key.split('_')[1]
                produk_id = value
                # Ambil nilai jumlah produk yang sesuai
                jumlah = int(request.POST.get('jumlah_' + index, 0))
                if jumlah > 0:
                    # Simpan detail transaksi pembelian
                    detail_pembelian = DetailTransaksiPembelian.objects.create(transaksi_pembelian=transaksi_pembelian, produk_id=produk_id, jumlah=jumlah)

                    # Perbarui jumlah stok produk
                    produk = Produk.objects.get(id=produk_id)
                    produk.stock += jumlah
                    produk.save()
        return redirect('pembelianadmin')

    # Jika metode bukan POST, kembali ke halaman pembelian_tambah
    return redirect('tambah_pembelian')


from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone

def penjualan_per_produk_per_bulan(request):
    # Mendapatkan bulan dan tahun saat ini
    now = timezone.now()
    year = now.year

    # Daftar bulan
    bulan_list = [
        'Bulan 1', 'Bulan 2', 'Bulan 3', 'Bulan 4', 'Bulan 5', 'Bulan 6',
        'Bulan 7', 'Bulan 8', 'Bulan 9', 'Bulan 10', 'Bulan 11', 'Bulan 12'
    ]

    # Mendapatkan data penjualan per bulan untuk setiap produk
    produk_list = Produk.objects.all()
    data = {}
    for produk in produk_list:
        data_produk = []
        for bulan in range(1, 13):
            total_penjualan = DetailTransaksiPenjualan.objects.filter(
                transaksi_penjualan__tanggal_penjualan__year=year,
                transaksi_penjualan__tanggal_penjualan__month=bulan,
                produk=produk
            ).aggregate(Sum('jumlah'))['jumlah__sum'] or 0
            data_produk.append(total_penjualan)
        data[produk.nama_produk] = data_produk

    return render(request, 'penjualan_per_produk_per_bulan.html', {'data': data, 'bulan_list': bulan_list})




from django.db.models import Sum  # Ensure correct importfrom django.shortcuts import
from django.shortcuts import render
# from .models import TransaksiPenjualan, DetailTransaksiPenjualan
from sklearn.linear_model import LinearRegression
from django.db.models import Sum
from datetime import datetime, timedelta
@login_required
def regresi_linear_view(request):
    # Ambil data transaksi penjualan dari database
    transaksi_penjualan = TransaksiPenjualan.objects.all()

    # Proses data transaksi penjualan untuk mendapatkan total penjualan per bulan
    data = []
    for transaksi in transaksi_penjualan:
        total_penjualan = transaksi.detail_penjualans.aggregate(Sum('jumlah'))['jumlah__sum']
        if total_penjualan:
            data.append({'bulan': transaksi.tanggal_penjualan.strftime('%B %Y'), 'total_penjualan': total_penjualan})

    # Persiapkan data untuk regresi linear
    X = [[datetime.strptime(d['bulan'], '%B %Y').month] for d in data]
    y = [d['total_penjualan'] for d in data]

    # Buat model regresi linear
    model = LinearRegression()
    model.fit(X, y)

    # Prediksi jumlah penjualan pada bulan selanjutnya
    bulan_saat_ini = datetime.now().month
    bulan_selanjutnya = bulan_saat_ini + 1 if bulan_saat_ini < 12 else 1
    prediksi_bulan_selanjutnya = model.predict([[bulan_selanjutnya]])

    # Render template dengan data prediksi
    return render(request, 'regresi_linear.html', {'data_penjualan': data, 'prediksi': prediksi_bulan_selanjutnya[0]})

from django.shortcuts import render
from django.db.models import Sum, Case, When, IntegerField
# from .models import DetailTransaksiPenjualan
from datetime import datetime, timedelta

def get_sales_data():
    # Mengambil data penjualan produk dari database
    sales_data = DetailTransaksiPenjualan.objects.filter(
        transaksi_penjualan__tanggal_penjualan__range=[
            (datetime.now() - timedelta(days=365)), 
            datetime.now()
        ]
    ).values('produk__nama_produk').annotate(
        month_1=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=1, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_2=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=2, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_3=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=3, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_4=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=4, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_5=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=5, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_6=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=6, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_7=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=7, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_8=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=8, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_9=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=9, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_10=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=10, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_11=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=11, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
        month_12=Sum(Case(
            When(transaksi_penjualan__tanggal_penjualan__month=12, then='jumlah'),
            default=0, output_field=IntegerField()
        )),
    )

    # Inisialisasi dictionary untuk menyimpan data penjualan produk
    array_data_penjualan = {}
    for data in sales_data:
        product_name = data['produk__nama_produk']
        array_data_penjualan[product_name] = [
            data['month_1'], data['month_2'], data['month_3'], data['month_4'],
            data['month_5'], data['month_6'], data['month_7'], data['month_8'],
            data['month_9'], data['month_10'], data['month_11'], data['month_12']
        ]

    return array_data_penjualan

# def sales_data_view(request):
#     # Mengambil data penjualan
#     array_data_penjualan = get_sales_data()

#     return render(request, 'sales_data.html', {'array_data_penjualan': array_data_penjualan})



def sales_data_view(request):
    # Mengambil data penjualan produk dari database
    array_data_penjualan = get_sales_data()

    # Persiapan data untuk regresi linear
    X = np.array(range(1, 13)).reshape(-1, 1)  # Bulan
    prediksi = {}

    for produk, penjualan_per_bulan in array_data_penjualan.items():
        y = np.array(penjualan_per_bulan).reshape(-1, 1)  # Total penjualan
        
        # Buat model regresi linear
        model = LinearRegression()
        model.fit(X, y)

        # Prediksi penjualan pada bulan selanjutnya
        bulan_terakhir = X[-1][0]
        bulan_selanjutnya = bulan_terakhir + 1 if bulan_terakhir < 12 else 1
        prediksi_penjualan = int(model.predict([[bulan_selanjutnya]]).flatten()[0])

        # Simpan prediksi untuk produk ini
        prediksi[produk] = prediksi_penjualan

    # Menyiapkan data prediksi dalam bentuk list untuk ditampilkan dalam tabel HTML
    tabel_prediksi = []
    for produk, prediksi_penjualan in prediksi.items():
        tabel_prediksi.append({'produk': produk, 'prediksi_penjualan': prediksi_penjualan})

    # Memasukkan hasil prediksi ke dalam konteks dan merender template
    return render(request, 'sales_data.html', {'array_data_penjualan': array_data_penjualan, 'tabel_prediksi': tabel_prediksi})





   




