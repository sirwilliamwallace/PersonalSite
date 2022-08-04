from django.shortcuts import render


# Create your views here.
def contact_form(request):
    return render(request, 'contact/contact.html', {})
