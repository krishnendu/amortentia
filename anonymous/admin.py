from django.contrib import admin
from .models import AnonymousClass
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(AnonymousClass,ImportExportModelAdmin)