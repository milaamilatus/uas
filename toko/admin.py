from django.contrib import admin
from .models import pembeli

# Register your models here.

class MemberPembeli():
    list_display = ("NAMA", "NO_ANTREAN", "PESANAN",)

admin.site.register(pembeli)


