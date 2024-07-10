import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

from mi_app.models import Book

books = [
    {"title": "Cien Años de Soledad", "author": "Gabriel García Márquez"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "El Gran Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Orgullo y Prejuicio", "author": "Jane Austen"},
    {"title": "Matar a un Ruiseñor", "author": "Harper Lee"},
    {"title": "Crimen y Castigo", "author": "Fyodor Dostoevsky"},
    {"title": "El Guardián entre el Centeno", "author": "J.D. Salinger"},
    {"title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes"},
    {"title": "Ulises", "author": "James Joyce"},
    {"title": "En el Camino", "author": "Jack Kerouac"},
]

for book_data in books:
    book, created = Book.objects.get_or_create(title=book_data['title'], author=book_data['author'])
    if created:
        print(f'Inserted {book.title} by {book.author}')
    else:
        print(f'{book.title} by {book.author} already exists')
