from relationship_app.models import Book, Author, Library, Librarian

def get_book_by_author(author_name):
    # 1. Query all books by a specific author
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author) 
    return books

    # 2. List all books in a library
def get_all_books_by_library(library_name):
    library = Library.objects.get(name=library_name)
    books= library.books.all()
    return books

    # 3. Retrieve the librarian for a library
def get_librarian_of_library(library_name):
     library= Library.objects.get(name=library_name)
     librarian = Librarian.objects.get(library=library)
     return librarian
   
      
    