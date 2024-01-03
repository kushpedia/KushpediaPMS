from django.urls import path
from . import views


urlpatterns = [
    path('',views.addProperties, name='addProperty'),
    path('add_property/',views.addProperties, name='addProperty'),
    path('view_property/',views.viewProperty, name='single_property'),
]
