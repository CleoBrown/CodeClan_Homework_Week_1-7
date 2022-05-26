import pdb
from models.author import Author
from models.book import Book

from repositories import authors_repository, books_repository

authors_repository.delete_all()
books_repository.delete_all()

author_1 = Author("JK", "Rowling")
authors_repository.save(author_1)

author_2 = Author("RL", "Stine")
authors_repository.save(author_2)

authors_repository.select_all()

book_1 = Book("The Goblet of Fire", author_1)
books_repository.save(book_1)

book_2 = Book("The haunted Mask", author_2)
books_repository.save(book_2)

books_repository.select_all()

# pdb.set_trace()