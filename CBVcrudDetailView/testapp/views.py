from django.shortcuts import render
from testapp.models import Books
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
class CBVListView(ListView):
    model = Books
    template_name = 'books_list.html'
    context_object_name = 'books_list'

class CBVDetailView(DetailView):
    model = Books
    template_name = 'books_detail.html'
#    context_object_name = 'books_detail'

class CBVCreateView(CreateView):
    model = Books
    fields = ('title','author','pages','price')
    template_name = 'books2.html'
