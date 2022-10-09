from pathlib import Path

from music.adapters.repository import AbstractRepository
from music.adapters.memory_repository import MemoryRepository


class UnknownUserException(Exception):
    pass


def retrieve_tracks(repo: AbstractRepository, artist_name):
    return repo.get_tracks_artist(artist_name)
