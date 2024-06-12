from django.contrib import admin
from .models import CSVFile


@admin.register(CSVFile)
class CSVFileForm(admin.ModelAdmin):
    list_display = ["file", "uploaded_at"]
