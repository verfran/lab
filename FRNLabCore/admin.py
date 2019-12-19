from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):
	list_display = ('firstName', 'secondName', 'gender', 'dateOfBirth', 'notes',
		'phoneNumber', 'email')
