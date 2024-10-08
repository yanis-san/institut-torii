from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from torii.contact.models import Contact
from torii.contact.forms import ContactForm

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            
            # Préparer le message HTML pour l'email de notification
            html_message = render_to_string('contact/contact_email.html', {
                'name': contact.name,
                'email': contact.email,
                'phone_number': contact.phone_number,
                'why_contact_us': contact.why_contact_us,
                'reason_for_contact': contact.reason_for_contact,
            })
            
            # Convertir le message HTML en texte brut
            plain_message = strip_tags(html_message)
            
            # Envoyer un email de notification
            send_mail(
                subject='Nouveau message de contact',
                message=plain_message,
                from_email='charger.com.igg@gmail.com',  
                recipient_list=['smm.torii@gmail.com', 'charger.com.igg@gmail.com'],
                #recipient_list=['smm.torii@gmail.com'],
                fail_silently=False,
                html_message=html_message,
            )
            
            # Préparer le message HTML pour l'email de confirmation
            confirmation_html_message = render_to_string('contact/confirmation_email.html', {
                'name': contact.name,
            })
            
            # Convertir le message HTML en texte brut
            confirmation_plain_message = strip_tags(confirmation_html_message)
            
            # Envoyer un email de confirmation
            send_mail(
                subject='Nous avons bien reçu ta demande',
                message=confirmation_plain_message,
                from_email='charger.com.igg@gmail.com',
                recipient_list=[contact.email],
                fail_silently=False,
                html_message=confirmation_html_message,
            )
            
            # Rediriger
            return redirect("home:homepage")
    else:
        form = ContactForm()
    return render(request, "contact/contact_form.html", context={"form": form})










