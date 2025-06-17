from tkinter.font import names

from django.urls import path

from articles import views

urlpatterns = [
    path('', views.article_list, name='article'),
    path('<slug:slug>', views.article_item, name='article_detail'),
]