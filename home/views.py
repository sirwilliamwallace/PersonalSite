from django.views.generic.base import TemplateView

from .models import Hero, SiteSettings, Profile, Seo


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data()
        context['settings'] = SiteSettings.objects.all().first()
        return context


class AboutPartialView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.all().first()
        base = super(AboutPartialView, self).get_context_data()
        base['profile'] = profile
        base['hero_skills'] = Hero.objects.all().first()
        return base


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
        base['name'], base['skills'], base[
            'bg_image'] = hero.name.get_full_name() if hero.name.get_full_name() else hero.name.username, hero.skills, hero.bg_image
        return base


class SeoModelView(TemplateView):
    template_name = "main/components/meta_tags_components.html"

    def get_context_data(self, **kwargs):
        base_context = super(SeoModelView, self).get_context_data(**kwargs)
        base_context['seo']: Seo = Seo.objects.filter(isMain=True).prefetch_related('keywords_connection').first()
        return base_context
