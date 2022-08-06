from django.views.generic.base import TemplateView

from .models import Hero, SiteSettings


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data()
        context['settings'] = SiteSettings.objects.all().first()
        return context


class AboutPartialView(TemplateView):
    template_name = 'home/about.html'


class ServicesPartialView(TemplateView):
    template_name = 'home/services.html'
    hero = Hero.objects.all().first()

    def get_context_data(self, **kwargs):
        base = super(ServicesPartialView, self).get_context_data()
        base['skills'] = self.hero.skills
        return base


class HeaderComponentView(TemplateView):
    template_name = 'main/components/header_component.html'

    def get_context_data(self, **kwargs):
        context = super(HeaderComponentView, self).get_context_data()
        context['settings'] = SiteSettings.objects.all().first()
        return context


class FooterComponentView(TemplateView):
    template_name = 'main/components/footer_component.html'


class HeroComponentView(TemplateView):
    template_name = 'main/components/hero_component.html'

    def get_context_data(self, **kwargs):
        base = super(HeroComponentView, self).get_context_data()
        hero = Hero.objects.all().first()
        base['name'] = hero.name.get_full_name()
        base['skills'] = hero.skills
        base['bg_image'] = hero.bg_image
        return base
