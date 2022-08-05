from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from post.models import Post


class HomePageView(TemplateView):
    template_name = 'home/index.html'


class AboutPartialView(TemplateView):
    template_name = 'home/about.html'


class ServicesPartialView(TemplateView):
    template_name = 'home/services.html'


class PortfolioPartialView(TemplateView):
    template_name = 'home/portfolio.html'


class HeaderComponentView(TemplateView):
    template_name = 'main/components/header_component.html'


class FooterComponentView(TemplateView):
    template_name = 'main/components/footer_component.html'


class HeroComponentView(TemplateView):
    template_name = 'main/components/hero_component.html'
