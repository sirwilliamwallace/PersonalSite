from django.shortcuts import render, redirect
from django.urls import reverse


def contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # print(f"{name} - {message} - {email} - {subject} - {message}")
        return redirect(reverse('home:index_page'))
    return render(request, 'contact/contact.html', {})
