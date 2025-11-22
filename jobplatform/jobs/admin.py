from django.contrib import admin
from .models import JobOffer

@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'contract_type', 'location', 'salary', 'is_active')
    list_filter = ('contract_type', 'is_active')
    search_fields = ('title', 'company__company_name', 'description')