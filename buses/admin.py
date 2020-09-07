from django.contrib import admin

# Register your models here.
from buses.models import BussesCompany,Bus

class InLine(admin.TabularInline):
    model = Bus
    extra = 0

@admin.register(BussesCompany)
class BussesCompanyAmin(admin.ModelAdmin):
    search_fields = ('name',)
    inlines = [InLine]

# admin.site.register(Bus)
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ['serial_number','operator','site_count']
    list_filter = ['operator']