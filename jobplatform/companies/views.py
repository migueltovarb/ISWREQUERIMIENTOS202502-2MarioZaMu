from django.shortcuts import render
from users.models import Company
from jobs.models import JobOffer

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'companies/company_list.html', {'companies': companies})

def company_detail(request, company_id):
    company = Company.objects.get(id=company_id)
    active_jobs = JobOffer.objects.filter(company=company, is_active=True)
    return render(request, 'companies/company_detail.html', {
        'company': company,
        'active_jobs': active_jobs
    })