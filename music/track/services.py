from pathlib import Path

from music.adapters.repository import AbstractRepository
from music.adapters.memory_repository import MemoryRepository

class UnknownUserException(Exception):
    pass

def retrieve_track(repo: AbstractRepository, track_name):

    return repo.get_track(track_name)


