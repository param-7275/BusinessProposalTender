from django.contrib import admin
from .models import*
# Register your models here.
# admin.site.register(CoustmerDetail)
class Admin(admin.ModelAdmin):
    list_display = ['name','title', 'companyname','created_at']
admin.site.register(CoustmerDetail,Admin)
admin.site.register(TemplatesName)