from pathlib import Path

from music.adapters.repository import AbstractRepository


class UnknownUserException(Exception):
    pass


def add_review(repo: AbstractRepository, review):
    repo.add_reviews(review)
