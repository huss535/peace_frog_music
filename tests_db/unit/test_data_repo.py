from datetime import date, datetime

import pytest

import music.adapters.repository as repo
from music.adapters.database_repository import database_repository
from music.adapters.repository import RepositoryException
from music.domainmodel.review import Review


def test_repository_can_add_a_review(session_factory):
    repo = database_repository(session_factory)

    review = Review('Side A', 'Not good')
    repo.add_reviews(review)

    repo.add_reviews(Review('Side A', 'Not good'))

    rev2 = repo.get_reviews('Side A')

    assert  review in rev2