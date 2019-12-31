
from django.urls import path
from . import views

urlpatterns = [
    path('values/',views.key_val),
    path('values/<int:pk>/',views.value_detail),
]
