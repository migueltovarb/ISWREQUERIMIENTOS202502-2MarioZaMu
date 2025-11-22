from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_to_job, name='apply_to_job'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('company-applications/', views.company_applications, name='company_applications'),
    path('company-applications/<int:job_id>/', views.company_applications, name='company_applications_job'),
    path('update-status/<int:application_id>/', views.update_application_status, name='update_application_status'),
]