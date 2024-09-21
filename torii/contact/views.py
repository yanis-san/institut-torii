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
            
            # Préparer le message HTML
            html_message = render_to_string('contact/contact_email.html', {
                'name': contact.name,
                'email': contact.email,
                'phone_number': contact.phone_number,
                'why_contact_us': contact.why_contact_us,
                'reason_for_contact': contact.reason_for_contact,
            })
            
            # Convertir le message HTML en texte brut
            plain_message = strip_tags(html_message)
            
            # Envoyer un email
            send_mail(
                subject='Nouveau message de contact',
                message=plain_message,
                from_email='institut-torii@institut-torii.com',  # Assurez-vous que cette adresse est correcte
                recipient_list=['smm.torii@gmail.com', 'charger.com.igg@gmail.com', 'institut.torii@gmail.com'],
                #recipient_list=['smm.torii@gmail.com'],
                fail_silently=False,
                html_message=html_message,
            )
            print(f"je passe par là et voici le mail qui envoi {send_mail}")
            
            # Rediriger
            return redirect("home:homepage")
    else:
        form = ContactForm()
    return render(request, "contact/contact_form.html", context={"form": form})