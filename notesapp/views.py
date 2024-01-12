from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.
class NotesCreateView(CreateView):
    model = Notes
    template_name = 'notes/notes_form.html'
    fields = ['title', 'description']
    success_url = ''
    
    
class NotesListView(ListView):
    model = Notes
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'



class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'

