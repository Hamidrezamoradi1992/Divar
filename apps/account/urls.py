
from django.urls import path
from django.views.generic.base import TemplateView
from apps.account.views import SignUpView, VerifyEmailView,LoginView
from django.contrib.auth import authenticate, login, logout

urlpatterns = [
    path('sigup/', TemplateView.as_view(template_name='signin_signup/sign_up.html'), name='sign_up'),

    path('sigup/api/signin', SignUpView.as_view()),
    path('verify/<str:email>', TemplateView.as_view(template_name='signin_signup/verify.html'), name='verify'),
    path('api/verify', VerifyEmailView.as_view()),

    #test
    path('api/test', LoginView.as_view()),
    path('test/', TemplateView.as_view(template_name='signin_signup/test.html'), name='test'),

]
