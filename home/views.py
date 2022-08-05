from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from post.models import Post


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


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
