from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def home_page(request):
    return render(request, 'index.html')


def contact_function(request):
    admin_email = 'ebilebilli@gmail.com'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
    
            send_mail(
                subject,
                f'Name: {name}, Email:{email}, Message:{message}',
                email,
                [admin_email],
                fail_silently=True
            )
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('app:home_page')
        
        messages.error(request, 'Please correct the errors below.')

    form = ContactForm()
    return render(request, 'app:home_page', {form: 'form'})
    