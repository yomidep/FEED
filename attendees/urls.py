from django.urls import path

from .views import Attendees

urlpatterns = [
    path("attendees/", Attendees.as_view(), name = "attendees")
]
