from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.

class UserPanelView(TemplateView):
    template_name = 'UserPanel/user_panel.html'



def user_panel_component(request):
    return render(request, 'UserPanel/user_panel_component.html')