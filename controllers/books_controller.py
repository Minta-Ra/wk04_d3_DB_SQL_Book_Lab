from flask import Flask, render_template, request, redirect, url_for

from repositories import author_repository
from repositories import book_repository
from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/")
def home():
    return render_template("home.html")


@books_blueprint.route("/books")
def show_books():
    books = book_repository.select_all_books()
    return render_template("books/show.html", books=books)