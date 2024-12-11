from django.urls import path

from apps.payment import views

urlpatterns = [
    path('api/ladder/payment', views.AddToOrderForLadderView.as_view()),
    path('api/pay', views.PayOrderView.as_view()),
    # path('request/', views.send_request, name='request'),
    # path('verify/', views.verify, name='verify'),
]