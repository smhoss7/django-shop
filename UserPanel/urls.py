from django.urls import path

from UserPanel import views

urlpatterns = [
    path('', views.UserPanelView.as_view(), name='dashboard'),

]