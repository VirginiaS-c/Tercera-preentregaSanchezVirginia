from django.shortcuts import render
from .models import Book
from .forms import AuthorForm, PublisherForm, BookForm, SearchForm

def index(request):
    books = Book.objects.all()
    return render(request, 'mi_app/index.html', {'books': books})

def insert_data(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        publisher_form = PublisherForm(request.POST)
        book_form = BookForm(request.POST)
        if author_form.is_valid():
            author_form.save()
        if publisher_form.is_valid():
            publisher_form.save()
        if book_form.is_valid():
            book_form.save()
    else:
        author_form = AuthorForm()
        publisher_form = PublisherForm()
        book_form = BookForm()
    return render(request, 'mi_app/insert_data.html', {'author_form': author_form, 'publisher_form': publisher_form, 'book_form': book_form})

def search(request):
    form = SearchForm()
    results = []
    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)
    return render(request, 'mi_app/search.html', {'form': form, 'results': results})


