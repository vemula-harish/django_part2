from django.shortcuts import render
from django.views.generic import ListView
from testapp.models import Book
# Create your views here.

# if its a function based views
#def book_view(request):
#    book_list = Book.objects.all()
#    return render(request,'book.html',{'book_list':book_list})

class BookListView(ListView):
    model = Book
#    default template file is: book_list.html
#    default context object name is : book_list
    template_name = 'book.html'
    context_object_name = 'books'
