"""temple_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from receipt_management.views import add_receipt, view_dashboard, print_receipt, view_report, view_daily_report, view_monthly_report, edit_vazhipadu, add_vazhipadu, add_expense, expense_on_date,edit_expense, del_expense
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'',LoginView.as_view(template_name='receipt_management/login.html'),name='login'),
    path('logout',LogoutView.as_view(template_name='receipt_management/logout.html'),name='logout'),
    
    path('dashboard/', view_dashboard ,name='view_dashboard'),
    path('reports/', view_report ,name='view_report'),
    path('reports/daily', view_daily_report ,name='view_daily_report'),
    path('reports/monthly', view_monthly_report ,name='view_monthly_report'),

    path('vazhipadu/add', add_vazhipadu ,name='add_vazhipadu'),
    path('vazhipadu/edit/<int:id>', edit_vazhipadu ,name='edit_vazhipadu'),

    path('receipt/', add_receipt,name='add_receipt'),
    path('receipt/<int:receipt_id>', print_receipt,name='print_receipt'),

    path('expense/', add_expense,name='add_expense'),
    path('expense/edit/<int:id>', edit_expense,name='edit_expense'),
    path('expense/del/<int:id>', del_expense,name='del_expense'),
    url('expense/(?P<date>\d{4}-\d{2}-\d{2})/', expense_on_date,name='expense_on_date'),

    # path('report/', add_receipt,name='add_receipt'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)