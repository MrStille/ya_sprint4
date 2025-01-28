import pytest

from books_collector import BooksCollector
from conftest import random_children_genre


class TestBooksCollector:

    @staticmethod
    def add_book(book_collection, book_name, book_genre):
        book_collection.add_new_book(book_name)
        book_collection.set_book_genre(book_name, book_genre)

    def test_add_new_book(self, book_name):
        book_collector = BooksCollector()
        book_collector.add_new_book(book_name)
        assert len(book_collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name', ["","Forty one symbols symbols symbols symbols"])
    def test_book_with_bad_name_is_not_added(self, book_name):
        book_collector = BooksCollector()
        book_collector.add_new_book(book_name)
        assert len(book_collector.get_books_genre()) == 0

    def test_get_book_genre(self, book_name, random_all_genres):
        book_collector = BooksCollector()
        book_collector.add_new_book(book_name)
        book_collector.set_book_genre(book_name, random_all_genres)
        assert book_collector.get_book_genre(book_name) == random_all_genres

    def test_get_book_with_wrong_genre(self, book_name):
        book_collector = BooksCollector()
        book_collector.add_new_book(book_name)
        book_collector.set_book_genre(book_name, "Some Genre")
        assert book_collector.get_book_genre(book_name) == ""

    def test_get_books_with_specific_genre(self, book_name, random_all_genres):
        book_collector = BooksCollector()
        book_collector.add_new_book(book_name)
        book_collector.set_book_genre(book_name, random_all_genres)
        assert book_collector.get_books_with_specific_genre(random_all_genres) == [book_name]

    def test_get_books_genre(self, book_name, random_all_genres):
        book_collector = BooksCollector()
        book_collector.add_new_book(book_name)
        assert len(book_collector.get_books_genre()) > 0

    def test_get_books_for_children(self, random_children_genre, random_age_rating_genre):
        child_book = "Колобок"
        age_rating_book = "Дракула"
        book_collector = BooksCollector()
        self.add_book(book_collector, child_book, random_children_genre)
        self.add_book(book_collector, age_rating_book, random_age_rating_genre)
        books_for_children = book_collector.get_books_for_children()
        assert len(books_for_children) == 1
        assert child_book in books_for_children

    def test_add_book_in_favorites(self, book_name, random_all_genres):
        book_collector = BooksCollector()
        self.add_book(book_collector, book_name, random_all_genres)
        book_collector.add_book_in_favorites(book_name)
        favorites = book_collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert book_name in favorites

    def test_remove_book_from_favorites(self, book_name, random_all_genres):
        book_collector = BooksCollector()
        self.add_book(book_collector, book_name, random_all_genres)
        book_collector.add_book_in_favorites(book_name)
        book_collector.delete_book_from_favorites(book_name)
        favorites = book_collector.get_list_of_favorites_books()
        assert len(favorites) == 0

    def test_remove_only_one_book_from_favorites(self, book_name, random_all_genres):
        book_collector = BooksCollector()
        self.add_book(book_collector, book_name, random_all_genres)
        book_collector.add_book_in_favorites(book_name)
        book_name_2 = "Алиедора"
        self.add_book(book_collector, book_name_2, random_all_genres)
        book_collector.add_book_in_favorites(book_name_2)
        book_collector.delete_book_from_favorites(book_name)
        favorites = book_collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert book_name_2 in favorites

