from django.contrib import admin

from .models import Smartphone

class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('pk', 'model_name', 'color', 'display_resolution', 'display_size',
                    'display_type', 'processor_model', 'release_date', 'add_date')
    list_filter = ('add_date', )
    search_fields = ('model_name', )


admin.site.register(Smartphone, SmartphoneAdmin)