from db.run_sql import run_sql

from models.author import Author
from models.book import Book


def save_author(author):
    sql = "INSERT INTO authors (name, surname) VALUES (%s, %s) RETURNING *"
    values = [author.name, author.surname]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author


def select_all_authors():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['surname'], row['id'] )
        authors.append(author)
    return author


def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['name'], result['surname'], result['id'] )
    return author


def delete_all_authors():
    sql = "DELETE  FROM authors"
    run_sql(sql)