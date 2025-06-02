from django.urls import path
from apps.pillow.views_pillow.views_create import create_pillow_view
from apps.pillow.views_pillow.views_pillow_outlet import get_outlet_pillows_view

urlpatterns = [
    path('pillow/create/', create_pillow_view, name='create-pillow'),
    path('pillow/outlet_pillow/',get_outlet_pillows_view,name='get outlet fields')
]