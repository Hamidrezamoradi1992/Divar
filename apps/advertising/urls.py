from django.urls import path
from django.views.generic import TemplateView

from apps.advertising import views

urlpatterns = [

    path('api/all/advertising', views.AllAdvertisingView.as_view(), name='advertising-list'),
    # path('api/view/advertise/cartegory/<int:category_id>', views.ViewAdvertisingForCategory.as_view()),

    # add advertise
    path('view/add/advertise', TemplateView.as_view(template_name='AddAdvertise/AddAdvertise.html'), name='home'),
    # view all state
    path('api/add/advertise/state', views.AllStateView.as_view()),
    path('api/add/advertise/city/<int:state_id>', views.AllCityView.as_view()),

    # view detail
    path('view/add/advertise/<int:pk>', TemplateView.as_view(template_name='advertising/detayleAdvertisinng.html'),
         name='home'),
# delete advertising test
    path('view/add/advertise/test/<int:pk>', TemplateView.as_view(template_name='admin_panel/detayleAdvertisinng.html'),
         name='home'),

    path('api/detail/advertise/<int:pk>', views.DetailAdvertiseView.as_view()),

    path('api/add/advertise/', views.AddAdvertiseView.as_view()),
    # add image advertising
    path('api/add/image/', views.UploadAdvertiseImageView.as_view()),
    # add field advertising
    path('api/add/field/<int:category_id>', views.AddFieldAdvertiseView.as_view()),
    path('api/add/field/', views.AddFieldAdvertiseView.as_view()),

    path('api/add/advertise/all_category/<int:category_id>', views.AllCategoryView.as_view()),
    path('api/add/advertise/all_category/', views.AllCategoryView.as_view(), name='my_view_default'),

    # admin panel
    path('api/adminpanel/advertising', views.AdvertisingPublishedView.as_view()),
    path('api/adminpanel/favorite/advertising', views.AdvertisingFavoriteView.as_view()),
    path('api/adminpanel/forpayment/advertising', views.AdvertisingAllForPaymentView.as_view()),
    path('api/adminpanel/all/advertising', views.AdvertisingAllView.as_view()),
    # delete advertising
    path('api/destroy', views.DestroyAdvertising.as_view()),



    # accepted
    path('api/accepted/', views.AcceptSiteAdminAdvertising.as_view()),

    # filter

    path('view/filter/<int:category>', TemplateView.as_view(template_name='advertising/filter.html'), name='home'),
    path('api/add/advertise/filter/category/<int:category_id>', views.FilterAdvertising.as_view()),
    path('api/add/advertise/filter', views.FilterAdvertising.as_view()),
]
