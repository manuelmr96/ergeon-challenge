from django.db import models

# Assuming these are the models defined in your Django project.
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# 6.1 Using Django ORM, write a function that will print the book title and the author name (who wrote it) for all the books we have in the database
def print_books_with_authors():
    books_with_authors = Book.objects.select_related('author').all()
    for book in books_with_authors:
        print(f"\"{book.title}\". {book.author.name}")

# 6.2 Write another function that will print the author’s name and all the books he wrote. For all the authors we have in the database
def print_authors_with_books():
    authors_with_books = Author.objects.prefetch_related('book_set').all()
    for author in authors_with_books:
        book_titles = [book.title for book in author.book_set.all()]
        books_str = ', '.join(f"\"{title}\"" for title in book_titles)
        print(f"{author.name}: {books_str}")

# 6.3 Implement the third function, it should print the author’s name and the number of books he wrote. Order by the number of books written, descending.
def print_authors_book_count():
    authors_with_book_counts = Author.objects.annotate(book_count=models.Count('book')).order_by('-book_count')
    for author in authors_with_book_counts:
        print(f"{author.name}: {author.book_count}")

