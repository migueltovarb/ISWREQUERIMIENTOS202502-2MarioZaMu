from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JobOffer
from .forms import JobOfferForm
from users.models import Company

def job_list(request):
    jobs = JobOffer.objects.filter(is_active=True).select_related('company')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(JobOffer, id=job_id, is_active=True)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def create_job(request):
    # Verificar que el usuario sea una empresa
    if not hasattr(request.user, 'company'):
        messages.error(request, 'Solo las empresas pueden publicar ofertas laborales.')
        return redirect('home')
    
    if request.method == 'POST':
        form = JobOfferForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company
            job.save()
            messages.success(request, '¡Oferta laboral publicada exitosamente!')
            return redirect('job_list')
    else:
        form = JobOfferForm()
    
    return render(request, 'jobs/create_job.html', {'form': form})

@login_required
def my_company_jobs(request):
    # Verificar que el usuario sea una empresa
    if not hasattr(request.user, 'company'):
        messages.error(request, 'Acceso denegado.')
        return redirect('home')
    
    jobs = JobOffer.objects.filter(company=request.user.company)
    
    # Calcular estadísticas
    active_jobs_count = jobs.filter(is_active=True).count()
    total_applications = sum(job.application_set.count() for job in jobs)
    pending_applications = sum(job.application_set.filter(status='applied').count() for job in jobs)
    
    return render(request, 'jobs/my_company_jobs.html', {
        'jobs': jobs,
        'active_jobs_count': active_jobs_count,
        'total_applications': total_applications,
        'pending_applications': pending_applications
    })