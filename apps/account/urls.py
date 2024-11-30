
from django.urls import path
from django.views.generic.base import TemplateView
from apps.account.views import SignUpView, VerifyEmailView, UpdateUserView, UserProfileView, LogoutView
from django.contrib.auth import authenticate, login, logout

urlpatterns = [
    path('signup/', TemplateView.as_view(template_name='signin_signup/sign_up.html'), name='sign_up'),

    path('signup/api/signin', SignUpView.as_view()),
    path('verify/<str:email>', TemplateView.as_view(template_name='signin_signup/verify.html'), name='verify'),
    path('api/verify', VerifyEmailView.as_view()),
    path('api/logout', LogoutView.as_view()),

    #profile
    path('api/user/<int:pk>', UserProfileView.as_view()),
    path('api/update/user/<int:pk>', UpdateUserView.as_view()),
    # path('api/update/user/image/<int:user_id>', UserImageView.as_view()),

    #test
    # path('api/test/<int:pk>', UpdateUserView.as_view()),
    path('test/', TemplateView.as_view(template_name='signin_signup/test.html'), name='test'),

    #view
    path('adminuser/', TemplateView.as_view(template_name='admin_panel/mainAdminPanel.html'), name='adminuser'),

]
