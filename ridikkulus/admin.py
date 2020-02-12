from django.contrib import admin
from .models import Ridikkulus
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Ridikkulus,ImportExportModelAdmin)