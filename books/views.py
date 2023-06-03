from datetime import datetime

from django.shortcuts import render, get_object_or_404

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_all = Book.objects.all()
    context = {'books_all': books_all}
    return render(request, template, context)


def book_view(request, date):
    template = 'books/book_list.html'
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    # book = get_object_or_404(Book, pub_date=date)
    book = Book.objects.filter(pub_date=date_obj)
    book_min_data = False
    book_max_data = False
    if Book.objects.filter(pub_date__lt=date_obj):
        book_min = Book.objects.filter(pub_date__lt=date_obj)[0]
        book_min_data = book_min.pub_date
    if Book.objects.filter(pub_date__gt=date_obj):
        book_max = Book.objects.filter(pub_date__gt=date_obj)[0]
        book_max_data = book_max.pub_date
        print(f'Дата вперед {book_max_data}')

    context = {
        'book': book,
        'pub_date': date_obj,
        'book_min_data': book_min_data,
        'book_max_data': book_max_data
    }
    return render(request, template, context)
