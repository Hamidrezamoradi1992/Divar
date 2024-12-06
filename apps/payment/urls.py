from django.urls import path

from apps.payment import views

urlpatterns = [
    path('api/ladder/payment', views.AddToOrderForLadderView.as_view()),
]