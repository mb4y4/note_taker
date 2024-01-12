from django.shortcuts import render
from .models import Notes

from django.views.generic import ListView, DetailView

# Create your views here.

class NotesListView(ListView):
    model = Notes
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'

# def detail(request, pk):
#     note = Notes.objects.get(pk=pk)
#     return render(request, 'notes/notes_detail.html', {'note': note})