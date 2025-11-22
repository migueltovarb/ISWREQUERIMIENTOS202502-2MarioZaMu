from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Candidate, Company

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': ('role', 'phone', 'address')
        }),
    )

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user', 'skills_preview')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'skills')
    
    def skills_preview(self, obj):
        return obj.skills[:50] + '...' if obj.skills and len(obj.skills) > 50 else obj.skills
    skills_preview.short_description = 'Habilidades'

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'contact_email', 'website')
    search_fields = ('company_name', 'user__username', 'contact_email')