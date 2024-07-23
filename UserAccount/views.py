from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import generic, View

from UserAccount.forms import *
from UserAccount.models import User
from utils import send_email
from utils.send_email import sendEmail


# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'userAccount/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email__iexact=form.cleaned_data['email']).exists():
                form.add_error('email', 'Email already registered')
            else:
                print(form.cleaned_data['confirm_pass'])
                user = User(email=form.cleaned_data['email'], email_active_code=get_random_string(72),
                            username=form.cleaned_data['email'], is_active=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                sendEmail('register user',user.email,{'user':user},'emails/activate_account.html')
                return redirect(reverse('login view'))

        return render(request, 'userAccount/register.html', {'form': form})


class ActivateAccount(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            print(user.is_active)
            if user.is_active is False:
                user.is_active = True
                user.save()
                return redirect(reverse('login view'))
        raise Http404


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'userAccount/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user : User = User.objects.filter(email__iexact=email).first()
            if user is not None and user.check_password(password):
                if user.is_active is True:
                    login(request, user)
                    return redirect('/')
            form.add_error('email', 'user not found')
        return render(request, 'userAccount/login.html', {'form': form})



class ForgotPasswordView(View):

    def get(self, request):
        form=ForgotForm()
        return render(request,'userAccount/forgot.html',{'form':form})

    def post(self, request):
        form=ForgotForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                pass
                # todo : send a email
        return render(request,'userAccount/forgot.html',{'form':form})




class ResetPasswordView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is None:
            raise Http404

        form = ResetPasswordForm()
        return render(request, 'userAccount/reset.html', {'form': form,'user': user})

    def post(self, request, email_active_code):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
            if user is None:
                raise Http404

            user.set_password(form.cleaned_data['password'])
            user.email_active_code=get_random_string(72)
            user.is_active=True
            user.save()
            return redirect(reverse('login view'))
        return render(request, 'userAccount/reset.html', {'form': form})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login view'))

