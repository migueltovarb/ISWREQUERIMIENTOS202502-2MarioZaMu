from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Application
from jobs.models import JobOffer
from users.models import Candidate

@login_required
def apply_to_job(request, job_id):
    # Verificar que el usuario sea un candidato
    if not hasattr(request.user, 'candidate'):
        messages.error(request, 'Solo los candidatos pueden postularse a ofertas.')
        return redirect('job_list')
    
    job = get_object_or_404(JobOffer, id=job_id, is_active=True)
    candidate = request.user.candidate
    
    # Verificar si ya está postulado
    if Application.objects.filter(candidate=candidate, job_offer=job).exists():
        messages.warning(request, 'Ya te has postulado a esta oferta.')
        return redirect('job_detail', job_id=job_id)
    
    # Crear la postulación
    application = Application.objects.create(
        candidate=candidate,
        job_offer=job,
        status='applied'
    )
    
    messages.success(request, f'¡Te has postulado exitosamente a {job.title}!')
    return redirect('job_detail', job_id=job_id)

@login_required
def my_applications(request):
    # Verificar que el usuario sea un candidato
    if not hasattr(request.user, 'candidate'):
        messages.error(request, 'Acceso denegado.')
        return redirect('home')
    
    applications = Application.objects.filter(candidate=request.user.candidate).select_related('job_offer__company')
    return render(request, 'applications/my_applications.html', {'applications': applications})

@login_required
def company_applications(request, job_id=None):
    # Verificar que el usuario sea una empresa
    if not hasattr(request.user, 'company'):
        messages.error(request, 'Acceso denegado.')
        return redirect('home')
    
    company = request.user.company
    
    if job_id:
        # Postulaciones para una oferta específica
        job = get_object_or_404(JobOffer, id=job_id, company=company)
        applications = Application.objects.filter(job_offer=job).select_related('candidate__user')
        return render(request, 'applications/company_applications.html', {
            'applications': applications,
            'current_job': job
        })
    else:
        # Todas las postulaciones de la empresa
        applications = Application.objects.filter(job_offer__company=company).select_related('job_offer', 'candidate__user')
        return render(request, 'applications/company_applications.html', {'applications': applications})

@login_required
def update_application_status(request, application_id):
    if not hasattr(request.user, 'company'):
        return JsonResponse({'error': 'Acceso denegado.'}, status=403)
    
    application = get_object_or_404(Application, id=application_id, job_offer__company=request.user.company)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Application.STATUS_CHOICES):
            application.status = new_status
            application.save()
            return JsonResponse({'success': True, 'new_status': application.get_status_display()})
    
    return JsonResponse({'error': 'Solicitud inválida.'}, status=400)