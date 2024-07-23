from django.urls import path

from Home import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index_page'),
    path('about-us',views.about.as_view(),name='about_us'),

]