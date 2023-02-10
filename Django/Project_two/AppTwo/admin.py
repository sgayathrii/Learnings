from django.contrib import admin
from AppTwo.models import User_data
# Register your models here.

@admin.register(User_data)
class User_data(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'e_mail' )
