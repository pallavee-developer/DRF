
from django.urls import path
from .import views
urlpatterns = [
    path('',views.Homeview),
    path('CreateView', views.CreateView, name='CreateView'),
    path('UpdateView/<str:pk>', views.UpdateView, name='UpdateView'),
    path('detailview/<str:pk>', views.detailview, name='detailview'),
    path('deleteview/<str:pk>', views.deleteview, name='deleteview'),



]