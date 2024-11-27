from django.urls import path


from apps.favorite import views

urlpatterns = [

    path('add/favorite',views.AddFavoriteView.as_view()),
]