from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.display),
    path('sec/<int:a>',views.display1),
    path('vow/<b>',views.vowels),
path('a',views.display3),
path('b',views.display4),
path('0',views.palindrome),
path('8',views.numberv),
path('5',views.multi),
path('7',views.prime),
path('11',views.currentbill),
path('about.html',views.about),
path('update',views.studsandu),
path('13',views.studsearch),
path('14',views.studv),
path('delete',views.studdel),
path('15',views.regist),
]
