from django.db import models
from users.models import Company

class JobOffer(models.Model):
    CONTRACT_TYPES = (
        ('full_time', 'Tiempo Completo'),
        ('part_time', 'Medio Tiempo'),
        ('freelance', 'Freelance'),
        ('internship', 'Pasantía'),
    )
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPES)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.company.company_name}"