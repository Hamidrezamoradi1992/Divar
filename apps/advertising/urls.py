from django.urls import path

from apps.advertising import views

urlpatterns = [

    path('', views.AllAdvertisingView.as_view(), name='advertising-list'),
    path('api/view/advertise/cartegory/<int:category_id>', views.ViewAdvertisingForCategory.as_view()),

    #add advertise
    path('api/add/advertise/<int:category_id>', views.AddAdvertiseView.as_view()),
    path('api/add/advertise/all_category', views.ViewAllCategory.as_view()),
]