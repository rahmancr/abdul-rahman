from django.contrib import admin

# Register your models here.
from.models import student
admin.site.register(student)
from.models import register
admin.site.register(register)
from.models import login
admin.site.register(login)