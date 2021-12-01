import pdb

from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


book_repository.delete_all_books()
author_repository.delete_all_authors()


author_1 = Author("Ronald", "Tolkien")
author_repository.save_author(author_1)


book_1 = Book(author_1, "The Hobbit", 304)
book_repository.save_book(book_1)

book_2 = Book(author_1, "The Fellowship of the Ring", 480)
book_repository.save_book(book_2)

book_3 = Book(author_1, "The Return of the King", 340)
book_repository.save_book(book_3)