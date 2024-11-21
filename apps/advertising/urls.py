from django.urls import path

from apps.advertising import views

urlpatterns = [

    path('', views.AllAdvertisingView.as_view(), name='advertising-list'),
]