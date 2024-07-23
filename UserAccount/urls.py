from django.urls import path

from UserAccount import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register view'),
    path('login', views.LoginView.as_view(), name='login view'),
    path('activate-acc/<email_active_code>',views.ActivateAccount.as_view(), name='activate account'),
    path('reset-pass/<email_active_code>',views.ResetPasswordView.as_view(),name='reset password'),
    path('forgot-password', views.ForgotPasswordView.as_view(), name='forgot password'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]