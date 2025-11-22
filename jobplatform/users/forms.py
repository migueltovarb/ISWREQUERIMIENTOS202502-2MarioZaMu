from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Candidate, Company

class CandidateSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Requerido')
    first_name = forms.CharField(max_length=30, required=True, help_text='Requerido')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requerido')
    phone = forms.CharField(max_length=15, required=True)
    skills = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'candidate'
        if commit:
            user.save()
            Candidate.objects.create(
                user=user,
                skills=self.cleaned_data.get('skills', '')
            )
        return user

class CompanySignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Requerido')
    company_name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    contact_email = forms.EmailField(required=True)
    website = forms.URLField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'company_name', 'contact_email', 'website', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'company'
        if commit:
            user.save()
            Company.objects.create(
                user=user,
                company_name=self.cleaned_data['company_name'],
                description=self.cleaned_data.get('description', ''),
                contact_email=self.cleaned_data['contact_email'],
                website=self.cleaned_data.get('website', '')
            )
        return user