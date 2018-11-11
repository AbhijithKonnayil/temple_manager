from django.shortcuts import render
from .forms import ReceiptForm, DailyReportForm, MonthlyReportForm, VazhipaduForm, ExpenseForm
from .models import Vazhipadu, Receipt, ReceiptItem, Expense
from django.http import Http404, HttpResponseRedirect
from datetime import datetime
from django.db.models import Sum, Count
# STAR_CHOICESsd=('അശ്വതി','ഭരണി','കാർത്തിക',
#                     'രോഹിണി','മകയിരം','തിരുവാതിര',
#                     'പുണർതം','പൂയം','ആയില്യം',
#                     'മകം','പൂരം','ഉത്രം',
#                     'അത്തം','ചിത്തിര ','ചിത്തി',
#                     'വിശാഖം','അനിഴം','തൃക്കേട്ട',
#                     ' മൂലം','പൂരാടം','ഉത്രാടം',
#                     'തിരുവോണം','അവിട്ടം','ചതയം',
#                     'പൂരുരുട്ടാതി','ഉത്രട്ടാതി','രേവതി',
#                   )
STAR_CHOICES=(('അശ്വതി','Aswathy'),('ഭരണി','Bharani'),('കാർത്തിക','Karthika'),
                    ('രോഹിണി','Rohinini'),('മകയിരം','Makayiram'),('തിരുവാതിര','Thiruvathira'),
                    ('പുണർതം','Punartham'),('പൂയം','Pooyam'),('ആയില്യം','Aayilyam'),
                    ('മകം','Makam'),('പൂരം','Pooram'),('ഉത്രം','Uthrdam'),
                    ('അത്തം','Atham'),('ചിത്തിര ','Chithira'),('ചോതി','Chothi'),
                    ('വിശാഖം','Vishakam'),('അനിഴം','Anizham'),('തൃക്കേട്ട','Thrikketa'),
                    ('മൂലം','Moolam'),('പൂരാടം','Pooradam'),('ഉത്രാടം','Uthradam'),
                    ('തിരുവോണം','Thiruvonam'),('അവിട്ടം','Avittam'),('ചതയം','Chathayam'),    
                    ('പൂരുരുട്ടാതി','Puruttathi'),('ഉത്രട്ടാതി','Uthrattathi'),('രേവതി','Revathi'),
                )

def add_receipt(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = ReceiptForm(request.POST)
            print(form.errors)
            if form.is_valid():
                print("valid")
                R=Receipt.objects.create(name=form.cleaned_data['name'],star=form.cleaned_data['star'])

                vazhipadu_1=Vazhipadu.objects.get(title=form.cleaned_data['vazhipadu_1'])
                # count_1=form.cleaned_data['count_1']
                print(type(vazhipadu_1.amount))
                print(type(form.cleaned_data['count_1']))
                r1=ReceiptItem.objects.create(vazhipadu=vazhipadu_1,
                                        count=form.cleaned_data['count_1'],
                                        receipt=R,
                                        amount=vazhipadu_1.amount*int(form.cleaned_data['count_1']),
                                        )
                R.total_amount=R.total_amount+r1.amount
                
                if form.cleaned_data['vazhipadu_2']:
                    vazhipadu_2=Vazhipadu.objects.get(title=form.cleaned_data['vazhipadu_2'])
                    # count_1=form.cleaned_data['count_1']
                    r2=ReceiptItem.objects.create(vazhipadu=vazhipadu_2,
                                        count=form.cleaned_data['count_2'],
                                        receipt=R,
                                        amount=vazhipadu_2.amount*int(form.cleaned_data['count_2']),
                                        )
                    R.total_amount=R.total_amount+r2.amount
                if form.cleaned_data['vazhipadu_3']:
                    vazhipadu_3=Vazhipadu.objects.get(title=form.cleaned_data['vazhipadu_3'])
                    # count_1=form.cleaned_data['count_1']
                    r3=ReceiptItem.objects.create(vazhipadu=vazhipadu_3,
                                        count=form.cleaned_data['count_3'],
                                        receipt=R,
                                        amount=vazhipadu_3.amount*int(form.cleaned_data['count_3']),
                                        )
                    R.total_amount=R.total_amount+r3.amount
                if form.cleaned_data['vazhipadu_4']:
                    vazhipadu_4=Vazhipadu.objects.get(title=form.cleaned_data['vazhipadu_4'])
                    # count_1=form.cleaned_data['count_1']
                    r4=ReceiptItem.objects.create(vazhipadu=vazhipadu_4,
                                        count=form.cleaned_data['count_4'],
                                        receipt=R,
                                        amount=vazhipadu_4.amount*int(form.cleaned_data['count_4']),
                                        )
                    R.total_amount=R.total_amount+r4.amount
                R.save()
                context={'receipt_items':R.receipt_item.all(),'receipt':R}
                #return render(request,'receipt_management/add_receipts.html',context)  
                return HttpResponseRedirect('./'+str(R.id))
            form = ReceiptForm()
            vazhipadu_list = Vazhipadu.objects.all()
            receipt=Receipt.objects.all()
            context={'form':form,'stars':STAR_CHOICES,'vazhipadu':vazhipadu_list,'receipt':receipt}
            return HttpResponseRedirect('./')
        else:
            form = ReceiptForm()
            vazhipadu_list = Vazhipadu.objects.all()
            receipt=Receipt.objects.all().order_by('-id')
            context={'form':form,'stars':STAR_CHOICES,'vazhipadu':vazhipadu_list,'receipt':receipt[:5]}
            return render(request,'receipt_management/add_receipts.html',context)  

    else:
        return HttpResponseRedirect('../accounts/login/')

def print_receipt(request,receipt_id):
    if request.user.is_authenticated:
        R=Receipt.objects.get(id=receipt_id)
        context={'receipt_items':R.receipt_item.all(),'receipt':R}
        return render(request,'receipt_management/print_receipts.html',context)  
    else:
        return HttpResponseRedirect('/')

def view_dashboard(request):
    if request.user.is_authenticated:
        context={}
        return render(request,'receipt_management/dashboard.html',context)  
    else:
        return HttpResponseRedirect('/')

def view_report(request):
    if request.user.is_authenticated:
        context={}
        return render(request,'receipt_management/reports.html',context)
    else:
        return HttpResponseRedirect('/')
        
def view_daily_report(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=DailyReportForm(request.POST)
            if form.is_valid():
                print('valid')
                date=form.cleaned_data['date']
                todays_receipt = Receipt.objects.filter(date=date)
                report=ReceiptItem.objects.filter(receipt__in=todays_receipt).values('vazhipadu').annotate(count=Sum('count'),sum=Sum('amount')).order_by('vazhipadu')    
                total_sum = ReceiptItem.objects.filter(receipt__in=todays_receipt).aggregate(Sum('amount'))
        else:
            form=DailyReportForm()
            todays_receipt = Receipt.objects.filter(date=datetime.today())
            report=ReceiptItem.objects.filter(receipt__in=todays_receipt).values('vazhipadu').annotate(count=Sum('count'),sum=Sum('amount')).order_by('vazhipadu')
            total_sum = ReceiptItem.objects.filter(receipt__in=todays_receipt).aggregate(Sum('amount'))
            date=datetime.today()
        expense_list = Expense.objects.filter(date=date)
        expense = Expense.objects.filter(date=date)
        total_expense = Expense.objects.filter(date=date).aggregate(Sum('amount'))
        print(total_expense['amount__sum'] , " \n\n" ,total_expense['amount__sum'])

        if not(total_expense['amount__sum']) and total_sum['amount__sum']:
            net = total_sum['amount__sum']
            print("1")
        elif total_expense['amount__sum'] and not(total_sum['amount__sum']):
            net = 0-total_expense['amount__sum'] 
            print("2")
        elif total_sum['amount__sum'] and total_expense['amount__sum']:
            net = total_sum['amount__sum'] - total_expense['amount__sum']
            print("3")
        else:
            net=0
        context={'form':form,'report':report,'total_sum':total_sum['amount__sum'],
                    'expense_list':expense_list,'net':net,'total_expense':total_expense['amount__sum'],
                    'date':date}
        return render(request,'receipt_management/daily_report.html',context)  
    else:
        return HttpResponseRedirect('/')
        
def view_monthly_report(request):
    if request.user.is_authenticated:
        month_list=(('01','ജനുവരി | January'),('02','ഫെബ്രുവരി | February '),('03','മാർച്ച് | March'),
            ('04','ഏപ്രിൽ | April'),('05','മേയ് | May'),('06','ജൂൺ | June'),('07','ജൂലൈ | July'),
            ('08','ഓഗസ്റ്റ് | August'),('09','സെപ്റ്റംബർ | September'),('10','ഒക്ടോബർ | October'),
            ('11','നവംബർ | November'),('12','ഡിസംബർ | December'))
        if request.method=='POST':
            form=MonthlyReportForm(request.POST)
            if form.is_valid():
                print('valid')
                month=form.cleaned_data['month']
                monthly_receipt = Receipt.objects.filter(date__month=month)
                print(monthly_receipt)
                report=ReceiptItem.objects.filter(receipt__in=monthly_receipt).values('vazhipadu').annotate(count=Sum('count'),sum=Sum('amount')).order_by('vazhipadu')    
                total_sum = ReceiptItem.objects.filter(receipt__in=monthly_receipt).aggregate(Sum('amount'))
        else:
            today=datetime.now()
            form=MonthlyReportForm(initial={'month':today.month})
            month=today.month
            monthly_receipt = Receipt.objects.filter(date__year=today.year,date__month=today.month)
            print(monthly_receipt)
            report=ReceiptItem.objects.filter(receipt__in=monthly_receipt).values('vazhipadu').annotate(count=Sum('count'),sum=Sum('amount')).order_by('vazhipadu')
            total_sum = ReceiptItem.objects.filter(receipt__in=monthly_receipt).aggregate(Sum('amount'))
            print(report)
            # .values('vazhipadu').annotate(count=Sum('count'),sum=Sum('amount')).order_by('vazhipadu')
        context={'form':form,'report':report,'total_sum':total_sum['amount__sum'],'month':month_list[int(month)-1]}
        return render(request,'receipt_management/monthly_report.html',context)  
    else:
        return HttpResponseRedirect('/')

def add_vazhipadu(request):
    if request.user.is_authenticated:
        vazhipadu_list = Vazhipadu.objects.all()
        if request.method=='POST':
            form=VazhipaduForm(request.POST)
            if form.is_valid():
                obj=Vazhipadu()
                obj.title=form.cleaned_data['title']
                obj.amount=form.cleaned_data['amount']
                obj.save()
                form=VazhipaduForm()
        else:
            form=VazhipaduForm()
            
        context={'form':form,'vazhipadu_list':vazhipadu_list}
        return render(request,'receipt_management/add_vazhipadu.html',context)  
    else:
        return HttpResponseRedirect('/')

def add_expense(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=DailyReportForm(request.POST)
            if form.is_valid():
                date = form.cleaned_data['date']
                return HttpResponseRedirect('./'+str(date))  
        else:
            form=DailyReportForm()
            
        context={'form':form,}
        return render(request,'receipt_management/expense.html',context)  
    else:
        return HttpResponseRedirect('/')

def expense_on_date(request,date):
    if request.user.is_authenticated:
        expense_list = Expense.objects.filter(date=date)
        if request.method=='POST':
            form=ExpenseForm(request.POST)
            if form.is_valid():
                obj=Expense()
                obj.category=form.cleaned_data['category']
                obj.amount=form.cleaned_data['amount']
                obj.date=date
                if form.cleaned_data['remark']:
                    obj.remark=form.cleaned_data['remark']

                obj.save()
                form=ExpenseForm()
        else:
            form=ExpenseForm()
            
        context={'form':form,'expense_list':expense_list}
        return render(request,'receipt_management/add_expense.html',context)  
    else:
        return HttpResponseRedirect('/')

def edit_expense(request,id):
    if request.user.is_authenticated:
        obj=Expense.objects.get(id=id)
        if request.method=='POST':
            form=ExpenseForm(request.POST)
            if form.is_valid():
                obj.category=form.cleaned_data['category']
                obj.amount=form.cleaned_data['amount']
                if form.cleaned_data['remark']:
                    obj.remark=form.cleaned_data['remark']

                obj.save()
                form=ExpenseForm()
                return HttpResponseRedirect('../'+ str(obj.date))
        else:
            form=ExpenseForm(initial={'category':obj.category,'amount':obj.amount,'remark':obj.remark})
            
        context={'form':form,}
        return render(request,'receipt_management/edit_expense.html',context)  
    else:
        return HttpResponseRedirect('/')

def del_expense(request,id):
    if request.user.is_authenticated:
        obj=Expense.objects.get(id=id)
        if request.method=='POST':
            print("dfskj")
            obj.delete()
            return HttpResponseRedirect('../'+ str(obj.date))
        context={'record':obj,}
        return render(request,'receipt_management/del_expense.html',context)  
    else:
        return HttpResponseRedirect('/')