from django.urls import path

from ContactUs import views

urlpatterns = [
    path('',views.contactUs,name='contactUs'),
    path('send',views.Send.as_view(),name='send'),
]
