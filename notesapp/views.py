from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Notes

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import NotesForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = 'notesapp/notes_confirm_delete.html'
    success_url = '/smart/notes'
    login_url ='/login'
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    #template_name = 'notesapp/notes_form.html'
    #fields = ['title', 'description']
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url ='/login'
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    template_name = 'notesapp/notes_form.html'
    #fields = ['title', 'description']
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url ='/login'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notesapp/notes_list.html'
    context_object_name = 'notes'
    login_url ='/login'
    
    def get_queryset(self):
        return self.request.user.notes.all()



class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = 'notesapp/notes_detail.html'
    context_object_name = 'note'
    login_url ='/login'
    
    def get_queryset(self):
        return self.request.user.notes.all()

