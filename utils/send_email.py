from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from ShopDjango import settings


def sendEmail(subject, to, content,template):
    try:
        html_content = render_to_string(template, content)
        text_content = strip_tags(html_content)
        send_mail(subject, text_content, settings.EMAIL_HOST_USER, [to], html_content)
    except:
        pass

