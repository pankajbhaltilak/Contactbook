from pydoc import visiblename
from django.urls import path
from django.urls import include
from . import views
from .views import ContactList,ContactDetailsView, search

urlpatterns = [
    path('', views.saveinfo, name='saveinfo'),
    path('saveinfo/', views.saveinfo, name='saveinfo'),
    path('index/', views.index, name='index'),
    path('<int:id>/formupdate/', views.formupdate, name='formupdate'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('', ContactList.as_view()),
    path('<int:id>',ContactDetailsView.as_view())
]
