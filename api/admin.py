from django.contrib import admin

from api.models import Customer, Party

# Register your models here.

admin.site.register(Party)
admin.site.register(Customer)