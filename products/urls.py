from django.urls import path
from .views import home,chart_page

app_name = 'products'
urlpatterns = [
    path('',home,name='home'),
    path('chart/',chart_page,name='chart'),
]