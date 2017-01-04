from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    form = ContactForm(request.POST)
    title = 'Contact'
    context = {
        'title':title,
        'form':form,

    }
    if form.is_valid():
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('name') + ' writes:\n' + form.cleaned_data.get('message')
        email_from = form.cleaned_data.get('email')
        email_to = [settings.EMAIL_HOST_USER]
        contact = form.save(commit=False)
        contact.subject = subject
        contact.message = form.cleaned_data.get('message')
        contact.name = form.cleaned_data.get('name')
        contact.email = email_from
        contact.save()
        send_mail(
            subject,
            message,
            email_from,
            email_to,
            fail_silently=False,
        )
    template = 'contact.html'
    return render(request, template, context)