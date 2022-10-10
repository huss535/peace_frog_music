from pathlib import Path

from music.adapters.repository import AbstractRepository
from music.adapters.memory_repository import MemoryRepository

class UnknownUserException(Exception):
    pass

def add_review(repo: AbstractRepository, review):
    return repo.add_reviews(review)


