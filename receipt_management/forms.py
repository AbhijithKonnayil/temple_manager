from django import forms
from django.forms import ModelForm, CharField, TextInput, ChoiceField
import datetime

class ReceiptForm(forms.Form):
    name=forms.CharField(max_length=50, required=True,widget=TextInput(attrs={'autocomplete':'on'}))
    star=forms.CharField(max_length=20, required=True,widget=TextInput(attrs={'list':'star_choice'}))
    vazhipadu_1=forms.CharField(max_length=20, required=True,widget=TextInput(attrs={'list':'vazhipadu_choice','class':'vazhipadu'}))
    vazhipadu_2=forms.CharField(max_length=20, required=False,widget=TextInput(attrs={'list':'vazhipadu_choice','class':'vazhipadu'}))
    vazhipadu_3=forms.CharField(max_length=20, required=False,widget=TextInput(attrs={'list':'vazhipadu_choice','class':'vazhipadu'}))
    vazhipadu_4=forms.CharField(max_length=20, required=False,widget=TextInput(attrs={'list':'vazhipadu_choice','class':'vazhipadu'}))

class VazhipaduForm(forms.Form):
    title = forms.CharField(max_length=25,required=True)
    amount = forms.CharField(max_length=20, required=True,widget=TextInput(attrs={}))
    
class DailyReportForm(forms.Form):
    date=forms.DateField(initial=datetime.date.today,widget=TextInput(attrs={'type':'date'}))

month_list=(('01','ജനുവരി | January'),('02','ഫെബ്രുവരി | February '),('03','മാർച്ച് | March'),
            ('04','ഏപ്രിൽ | April'),('05','മേയ് | May'),('06','ജൂൺ | June'),('07','ജൂലൈ | July'),
            ('08','ഓഗസ്റ്റ് | August'),('09','സെപ്റ്റംബർ | September'),('10','ഒക്ടോബർ | October'),
            ('11','നവംബർ | November'),('12','ഡിസംബർ | December'))
class MonthlyReportForm(forms.Form):
    month=forms.ChoiceField(choices=month_list)

class ExpenseForm(forms.Form):
    category_choices =(('മാസപ്പടി സദനം','മാസപ്പടി സദനം'),('പാൽ','പാൽ'),('കറന്റ് ബില്','കറന്റ് ബില്'),('ശമ്പളം','ശമ്പളം'),('മറ്റുള്ളവ','മറ്റുള്ളവ '))
    category = forms.ChoiceField(choices=category_choices,required=True)
    amount = forms.CharField(max_length=20, required=True,widget=TextInput(attrs={}))
    remark = forms.CharField(max_length=100, required=False)
