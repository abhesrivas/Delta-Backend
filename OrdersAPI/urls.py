from django.urls import path, re_path
from OrdersAPI import views

urlpatterns = [
    #order/
    path('order/', views.OrderList.as_view()),

    #order/1/
    re_path('order/(?P<pk>[0-9]+)/', views.OrderDetail.as_view()),

    #quote/
    path('quote/', views.QuoteList.as_view()),

    #quote/1/
    re_path('quote/(?P<pk>[0-9]+)/', views.QuoteDetail.as_view()),

    #rec1/
    path('rec1/', views.RecommendedList.as_view()),

]
