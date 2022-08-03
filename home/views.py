from django.shortcuts import render


# Create your views here.
def index_page(request):
    return render(request, 'home/index.html', {})


def contact_page(request):
    return render(request, 'home/contact.html', {})


def about_page(request):
    return render(request, 'home/about.html', {})


def services_page(request):
    return render(request, 'home/services.html', {})


def portfolio(request):
    return render(request, 'home/portfolio.html', {})


def header_component(request):
    return render(request, 'main/components/header_component.html', {})


def footer_component(request):
    return render(request, 'main/components/footer_component.html', {})


def hero_component(request):
    return render(request, 'main/components/hero_component.html', {})
