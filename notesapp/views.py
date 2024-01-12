from django.shortcuts import render
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .forms import NotesForm

# Create your views here.
class NotesUpdateView(UpdateView):
    model = Notes
    #template_name = 'notesapp/notes_form.html'
    #fields = ['title', 'description']
    success_url = '/smart/notes'
    form_class = NotesForm
    
class NotesCreateView(CreateView):
    model = Notes
    template_name = 'notesapp/notes_form.html'
    #fields = ['title', 'description']
    success_url = '/smart/notes'
    form_class = NotesForm
    
    
class NotesListView(ListView):
    model = Notes
    template_name = 'notesapp/notes_list.html'
    context_object_name = 'notes'



class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notesapp/notes_detail.html'
    context_object_name = 'note'

