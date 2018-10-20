from django.db import models

# Create your models here.

class Vazhipadu(models.Model):
    title = models.CharField(max_length=50,null=False,blank=False,unique=True)
    amount = models.FloatField()

    def __str__(self):
        return "{}".format(self.title)


class ReceiptItem(models.Model):
    vazhipadu = models.ForeignKey(Vazhipadu,null=True,on_delete=models.SET_NULL)
    count = models.IntegerField()
    amount = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.id,self.vazhipadu)

class Receipt(models.Model):
    STAR_CHOICES=(('a','2'),('b','1'))
    name = models.CharField(max_length=50,null=False,blank=False)
    star = models.CharField(max_length=20, choices=STAR_CHOICES, default='1')
    receipt_items= models.ManyToManyField(ReceiptItem)
    total_amount = models.FloatField()

    def __str__(self):
        return "{} {} {}".format(self.id,self.name,self.star)
        