from django.db import models

# Create your models here.

class Vazhipadu(models.Model):
    title = models.CharField(max_length=50,null=False,blank=False,unique=True)
    amount = models.FloatField()

    def __str__(self):
        return "{}".format(self.title)

class Receipt(models.Model):
    STAR_CHOICES=(('അശ്വതി','അശ്വതി'),('ഭരണി','ഭരണി'),('കാർത്തിക','കാർത്തിക'),
                    ('രോഹിണി','രോഹിണി'),('മകയിരം','മകയിരം'),('തിരുവാതിര','തിരുവാതിര'),
                    ('പുണർതം','പുണർതം'),('പൂയം','പൂയം'),('ആയില്യം','ആയില്യം'),
                    ('മകം','മകം'),('പൂരം','പൂരം'),('ഉത്രം','ഉത്രം'),
                    ('അത്തം','അത്തം'),('ചിത്തിര ','ചിത്തിര '),('ചോതി','ചോതി'),
                    ('വിശാഖം','വിശാഖം'),('അനിഴം','അനിഴം'),('തൃക്കേട്ട','തൃക്കേട്ട'),
                    ('  മൂലം',' മൂലം'),('പൂരാടം','പൂരാടം'),('ഉത്രാടം','ഉത്രാടം'),
                    ('തിരുവോണം','തിരുവോണം'),('അവിട്ടം','അവിട്ടം'),('ചതയം','ചതയം'),    
                    ('പൂരുരുട്ടാതി','പൂരുരുട്ടാതി'),('ഉത്രട്ടാതി','ഉത്രട്ടാതി'),('രേവതി','രേവതി'),
                )
    name = models.CharField(max_length=50,null=False,blank=False)
    star = models.CharField(max_length=20, choices=STAR_CHOICES,)
    total_amount = models.FloatField(default=0)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return "{} {} {} {}".format(self.id,self.name,self.star,self.date)

class ReceiptItem(models.Model):
    vazhipadu = models.ForeignKey(Vazhipadu,null=True,on_delete=models.SET_NULL)
    count = models.IntegerField()
    receipt= models.ForeignKey(Receipt,related_name='receipt_item',on_delete=models.CASCADE,null=False,blank=True)
    amount = models.FloatField(default=0)

    def __str__(self):
        return "{} {}".format(self.id,self.vazhipadu)

class Expense(models.Model):
    category_choices =(('Salary','salary'),)
    category = models.CharField(max_length=50,null=False,blank=True,choices=category_choices,)
    amount = models.FloatField(null=False,blank=False,default=0)
    date=models.DateField()
    remark = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return "{}-{}".format(self.id,self.category)