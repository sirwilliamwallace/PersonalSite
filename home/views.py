from django.views.generic.base import TemplateView
from .models import Hero
from post.models import Post
from django.contrib.auth import get_user_model
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/index.html'


class AboutPartialView(TemplateView):
    template_name = 'home/about.html'


class ServicesPartialView(TemplateView):
    template_name = 'home/services.html'


class HeaderComponentView(TemplateView):
    template_name = 'main/components/header_component.html'


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
