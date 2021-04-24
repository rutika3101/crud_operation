from django.contrib import admin
from .models import register


# Register your models here.
@admin.register(register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'First_name', 'Last_name', 'Email', 'Password')
