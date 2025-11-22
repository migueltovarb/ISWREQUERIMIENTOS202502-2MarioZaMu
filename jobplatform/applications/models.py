from django.db import models
from users.models import Candidate
from jobs.models import JobOffer

class Application(models.Model):
    STATUS_CHOICES = (
        ('applied', 'Postulado'),
        ('review', 'En Revisión'),
        ('interview', 'Entrevista'),
        ('rejected', 'Rechazado'),
        ('hired', 'Contratado'),
    )
    
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['candidate', 'job_offer']
    
    def __str__(self):
        return f"{self.candidate} - {self.job_offer}"