from django.contrib import admin
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from UserAPI import views as user_views
from ItemAPI import views as item_views
from OrdersAPI import views as order_views

urlpatterns = [

    #admin/
    path('admin/', admin.site.urls),

    #users/
    path('users/', user_views.UserList.as_view()),

    #users/1/
    re_path('users/(?P<pk>[0-9]+)/', user_views.UserDetail.as_view()),

    #profiles/
    path('profiles/', user_views.ProfileList.as_view()),

    #profiles/1/
    re_path('profiles/(?P<pk>[0-9]+)/', user_views.ProfileDetail.as_view()),

    #laptop/
    path('laptop/', item_views.LaptopList.as_view()),

    #laptop/1/
    re_path('laptop/(?P<pk>[0-9]+)/', item_views.LaptopDetail.as_view()),

    #order/
    path('order/', order_views.OrderList.as_view()),

    #order/1/
    re_path('order/(?P<pk>[0-9]+)/', order_views.OrderDetail.as_view()),

    #quote/
    path('quote/', order_views.QuoteList.as_view()),

    #quote/1/
    re_path('quote/(?P<pk>[0-9]+)/', order_views.QuoteDetail.as_view()),

    #rec1/
    path('rec1/', order_views.RecommendedList.as_view()),

    #rec2/
    path('rec2/', item_views.LocationRecommendation.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
