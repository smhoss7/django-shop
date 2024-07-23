from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, CreateView

from ContactUs.forms import ContactForm, sendForm
from ContactUs.models import Contact, SendClass
from SiteSetting.models import SiteSettings


# Create your views here.

def contactUs(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            complete_contact = Contact(title=contact_form.cleaned_data['subject'],
                                       email=contact_form.cleaned_data['email'],
                                       full_name=contact_form.cleaned_data['name'],
                                       message=contact_form.cleaned_data['message']
                                       )
            complete_contact.save()
            return redirect('index_page')

    else:

        contact_form = ContactForm()
        setting: SiteSettings = SiteSettings.objects.filter(is_active=True).first()
        context = {
            'setting': setting
        }
    return render(request, 'contactUs/contact_us.html', {'contact_form': contact_form,'setting': setting})


def store_file(file):
    with open(file, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class Send(CreateView):
    template_name = 'contactUs/send.html'
    model = SendClass
    fields = '__all__'
    success_url = '/'

    # def get(self, request):
    #     form = sendForm()
    #     return render(request, 'contactUs/send.html', {'form': form})
    #
    # def post(self, request):
    #     form = sendForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         # store_file(form.cleaned_data['image'])
    #         prof = SendClass(image=request.FILES['image'])
    #         prof.save()
    #         return redirect('index_page')
    #     return render(request, 'contactUs/send.html', {'form': form})

# class contactUs(FormView):
#     form_class = ContactForm
#     template_name = 'ContactUs/contact_us.html'
#     success_url = '/'
#     def form_valid(self, form):
#         contact=Contact(title=form.cleaned_data['title'],
#                         email=form.cleaned_data['email'],
#                         phone=form.cleaned_data['phone'],
#                         message=form.cleaned_data['message'])
#         contact.save()
#         return super(contactUs, self).form_valid(form)
#
