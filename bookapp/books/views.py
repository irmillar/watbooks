from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView,
                                    UpdateView, DeleteView, TemplateView)
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.
class BookListView(ListView):
    context_object_name = 'books'
    model = models.Book
    ordering = ['author']

class BookDetailView(DetailView):
    context_object_name = 'book_detail'
    model = models.Book
    template_name = 'books/book_details.html'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


class BookCreateView(CreateView):
    model = models.Book
    form_class = forms.BookForm

class BookUpdateView(UpdateView):
    model = models.Book
    form_class = forms.BookForm


class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('book_app:index')

class AboutView(TemplateView):
    template_name = 'books/about.html'