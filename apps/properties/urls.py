from django.urls import path

from apps.properties.views import home, owner, property

urlpatterns = [
    path('', home, name='home'),
    path('owner', owner, name='owner'),
    path('property', property, name='property'),
]
