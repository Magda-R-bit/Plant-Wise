from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def index(request):

    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., send email or save to database)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # For now, just show a success message
            messages.success(request, "Thank you for your message!")
            return redirect("contact")  # Redirect to prevent form resubmission
    else:
        form = ContactForm()

    return render(request, "home/contact.html", {"form": form})
