from django.contrib import admin

import SiteSetting
from SiteSetting.models import *

# Register your models here.

admin.site.register(SiteSettings)
admin.site.register(FooterTitleLink)
admin.site.register(FooterLinks)