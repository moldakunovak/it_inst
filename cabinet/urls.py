from django.urls import path
from .views import get_cabinet, detail_cabinet

urlpatterns = [
    path('', get_cabinet),
    path('detail/<int:id>/', detail_cabinet, name='cabinet'),
]