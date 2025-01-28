import random

import pytest

from books_collector import BooksCollector


@pytest.fixture
def book_name():
    return "Tern"


@pytest.fixture
def random_all_genres():
    bc = BooksCollector()
    return random.choice(bc.genre)


@pytest.fixture
def random_children_genre():
    bc = BooksCollector()
    return random.choice(list(set(bc.genre) - set(bc.genre_age_rating)))


@pytest.fixture
def random_age_rating_genre():
    bc = BooksCollector()
    return random.choice(bc.genre_age_rating)
