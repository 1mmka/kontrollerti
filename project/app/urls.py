from django.urls import path
from app.views import home_page,add_data,show_data

urlpatterns = [
    path('',home_page,name='home-page'),
    path('add-data/',add_data,name='add-data'),
    path('show-data/<str:name>/<str:surname>/<str:age>/',show_data,name='show-data'),
    path('show-data/',show_data,name='show-data2')
]
