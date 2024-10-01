from django.shortcuts import render, redirect
from .models import Book
from .validators import validate_publication_year, validate_genre

def home(request):
    return render(request, 'home.html')  # You can create a template for the home page

# View for listing books
def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


# View for adding books
def add_book(request):
    errors = {}

    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        publication_year = request.POST['publication_year']
        availability_status = request.POST.get('availability_status', False)

        # Validate publication year
        year_error = validate_publication_year(publication_year)
        if year_error:
            errors['publication_year'] = year_error

        # Validate genre
        genre_error = validate_genre(genre)
        if genre_error:
            errors['genre'] = genre_error

        # If no errors, create the book
        if not errors:
            Book.objects.create(
                title=title,
                author=author,
                genre=genre,
                publication_year=publication_year,
                availability_status=availability_status
            )
            return redirect('book_list')

    return render(request, 'library/add_book.html', {'errors': errors})

# Implement update and delete similarly
