from django.shortcuts import render

# Create your views here.
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views import generic

class Attendees(generic.CreateView):
    form_class = ModelForm
    success_url = reverse_lazy("attendees")
    template_name = "registration/attendees_reg.html"
    