from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insert_data/', views.insert_data, name='insert_data'),
    path('view_all_data/', views.view_all_data, name='view_all_data'),
    path('get_rank/', views.get_rank, name='get_rank'),
    path('update_score/', views.update_score, name='update_score'),
    path('delete_record/', views.delete_record, name='delete_record'),
]
