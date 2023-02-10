from django.contrib import admin
from first_app.models import AccessRecord, Webpage, Topic
# Register your models here.
"""
@admin.register(AccessRecord)
class AccessRecord(admin.ModelAdmin):
    list_display = ( 'name',  'date')
"""
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)


