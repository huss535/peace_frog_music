from pathlib import Path

from music.adapters.repository import AbstractRepository
from music.adapters.memory_repository import MemoryRepository


def retrieve_tracks(repo: AbstractRepository):

    return repo.tracks


