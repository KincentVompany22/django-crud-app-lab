from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stamps/', views.stamps_index, name='stamp-index'),
    path('stamps/<int:pk>/', views.StampDetail.as_view(), name='stamp-detail'),
    path('stamps/create/', views.StampCreate.as_view(), name='stamp-create'),
    path('stamps/<int:pk>/update/', views.StampUpdate.as_view(), name='stamp-update'),
    path('stamps/<int:pk>/delete/', views.StampDelete.as_view(), name='stamp-delete'),

    path('stamps/<int:stamp_id>/add-stop/', views.add_stop, name='add-stop'),
    
]