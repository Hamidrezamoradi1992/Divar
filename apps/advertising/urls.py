from django.urls import path
from django.views.generic import TemplateView

from apps.advertising import views

urlpatterns = [

    path('', views.AllAdvertisingView.as_view(), name='advertising-list'),
    path('api/view/advertise/cartegory/<int:category_id>', views.ViewAdvertisingForCategory.as_view()),

    # add advertise
    path('view/add/advertise', TemplateView.as_view(template_name='AddAdvertise/AddAdvertise.html'), name='home'),
    #view all state
    path('api/add/advertise/state', views.AllStateView.as_view()),
    path('api/add/advertise/city/<int:state_id>', views.AllCityView.as_view()),


    path('api/add/advertise/<int:category_id>', views.AddAdvertiseView.as_view()),
    path('api/add/advertise/', views.AddAdvertiseView.as_view()),
    #add image advertising
    path('api/add/image/', views.UploadAdvertiseImageView.as_view()),


    path('api/add/advertise/all_category/<int:category_id>', views.AllCategoryView.as_view()),
    path('api/add/advertise/all_category/', views.AllCategoryView.as_view(), name='my_view_default'),
]
