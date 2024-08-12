from django import forms
from core.models import Kategori,Produk,Customer
from django.contrib.auth.forms import UserCreationForm
class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama']

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'gambar_produk', 'harga_beli', 'harga_jual', 'stock', 'kategori']
class CustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control'
        

