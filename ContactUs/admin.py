from django.contrib import admin

import ContactUs
from ContactUs.models import Contact, SendClass


# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'message']
    readonly_fields = ['title', 'email', 'message','is_read','slug','full_name','start_date']

admin.site.register(Contact, ContactUsAdmin)
admin.site.register(SendClass)