from django import template
from receipt_management.models import ReceiptItem, Vazhipadu
register = template.Library()

@register.filter(name='idToTitle')
def idToTitle(id):
    print(id)
    R=Vazhipadu.objects.get(id=id)
    return R.title
