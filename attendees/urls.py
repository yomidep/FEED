from django.urls import path

from attendees import views

urlpatterns = [
    path('attendees_reg/',views.attendees_reg),
]
