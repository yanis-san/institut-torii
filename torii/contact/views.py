from django.core.mail import send_mail
from django.shortcuts import render, redirect
from torii.contact.models import Contact
from torii.contact.forms import ContactForm

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            
            # Envoyer un email
           #send_mail(subject='Nouveau message de contact',message=f'Nom: {contact.name}\nEmail: {contact.email}\nNuméro: {contact.phone_number}\nMessage: {contact.why_contact_us}',from_email='yanis@yanis-san.com',recipient_list=['yanisbarbara98@gmail.com'],fail_silently=False,)
            
            # Rediriger
            return redirect("home:homepage")
    else:
        form = ContactForm()
    return render(request, "contact/contact_form.html", context={"form": form})