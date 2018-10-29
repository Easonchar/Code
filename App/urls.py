from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^detail/$',views.detail,name='detail'),
    url(r'^list/$',views.list,name='list'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^shoppingCar/$',views.shoppingCar,name='shoppingCar'),


]