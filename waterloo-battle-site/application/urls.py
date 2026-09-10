from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("battle", views.battle_map_view, name="battle_map")
]