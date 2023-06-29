from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Save the form data to the database using the Contact model
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()

            # Display a success message
            messages.success(request, 'Your message has been sent!')
            form = ContactForm()  # Reset the form after successful submission
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})
