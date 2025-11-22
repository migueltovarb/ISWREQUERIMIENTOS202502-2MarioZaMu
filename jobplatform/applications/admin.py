from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job_offer', 'status', 'applied_date')
    list_filter = ('status',)
    search_fields = ('candidate__user__username', 'job_offer__title')