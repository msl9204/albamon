from django.shortcuts import render
from .models import Main
from django.views.generic import ListView, DetailView

class MainList(ListView):
    model = Main

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = Main.objects.all()

        return context

class ContentList(DetailView):
    pass
