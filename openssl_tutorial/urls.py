from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home , name='blog-home'),
    path('about/',views.about, name='blog-about'),
    path('ope/',views.ope, name='ope'),
    path('ope2/',views.ope2, name='ope2'),
    path('ope3/',views.ope3, name='ope3'),
    path('ope4/',views.ope4, name='ope4'),
    path('ope5/',views.ope5, name='ope5'),
    path('ope6/',views.ope6, name='ope6'),
    path('ope7/',views.ope7, name='ope7'),
    path('ope8/',views.ope8, name='ope8'),
    path('ope9/',views.ope9, name='ope9'),
    path('ope10/',views.ope10, name='ope10'),
    path('form/',views.form, name='form'),
]