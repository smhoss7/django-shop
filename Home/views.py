from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from Product.models import Product
from Product.views import slide_list
from SiteSetting.models import *


# Create your views here.

def index(request):
    return render(request, 'index_page.html')


class IndexPageView(TemplateView):
    # def get(self, request):
    #     return render(request,'index_page.html')
    template_name = 'index_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['last_products']=slide_list(Product.objects.filter(is_published=True).order_by('-id'))[:8]
        return context


def header_partial(request):
    setting: SiteSettings = SiteSettings.objects.filter(is_active=True).first()
    context = {
        'setting': setting
    }
    return render(request, 'share/header_patial.html', context)


def footer_partial(request):
    setting: SiteSettings = SiteSettings.objects.filter(is_active=True).first()
    footer_box = FooterTitleLink.objects.all()
    print(footer_box)
    context = {
        'setting': setting,
        'footer_box': footer_box

    }
    return render(request, 'share/footer_partial.html', context)


class about(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context=super(about, self).get_context_data(**kwargs)
        site_setting: SiteSettings = SiteSettings.objects.filter(is_active=True).first()
        context['site_setting'] = site_setting
        return context

