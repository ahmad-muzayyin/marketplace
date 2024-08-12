# core/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone','username', 'email', 'password1', 'password2']
