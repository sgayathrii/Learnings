from django.contrib import admin
from basicapp.models import Contact_Info
# Register your models here.

@admin.register(Contact_Info)
class AccessRecord(admin.ModelAdmin):
    list_display = ('name', 'email', 'text' )











