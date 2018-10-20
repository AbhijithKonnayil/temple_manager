from django.contrib import admin
from .models import Vazhipadu, ReceiptItem, Receipt
#Register your models here.
admin.site.register(Vazhipadu)
admin.site.register(Receipt)
admin.site.register(ReceiptItem)