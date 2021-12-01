from db.run_sql import run_sql

from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository 


def save_book(book):
    sql = "INSERT INTO books (title, author_id, pages) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.pages]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def select_all_books():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['pages'], row['id'] )
        books.append(book)
    return books



def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['pages'], result['id'] )
    return book


def delete_all_books():
    sql = "DELETE  FROM books"
    run_sql(sql)