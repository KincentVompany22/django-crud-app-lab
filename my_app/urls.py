from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('all-stamps/',views.all_stamps_index, name='all-stamp-index'),

    path('stamps/', views.stamps_index, name='stamp-index'),
    path('stamps/<int:pk>/', views.StampDetail.as_view(), name='stamp-detail'),
    path('stamps/create/', views.StampCreate.as_view(), name='stamp-create'),
    path('stamps/<int:pk>/update/', views.StampUpdate.as_view(), name='stamp-update'),
    path('stamps/<int:pk>/delete/', views.StampDelete.as_view(), name='stamp-delete'),

    path('stamps/<int:stamp_id>/stop-create/', views.StopCreate.as_view(), name='stop-create'),
    path('stamps/<int:stamp_id>/stop/<int:pk>/stop-update', views.StopUpdate.as_view(), name='stop-update'),
    path('stamps/<int:stamp_id>/stop/<int:pk>/stop-delete', views.StopDelete.as_view(), name='stop-delete'),

    path('accounts/signup/', views.signup, name='signup'),

]