from django.urls import path
from . import views

urlpatterns = [
    # send comment
    path('api/send', views.CommentSendView.as_view()),
]
