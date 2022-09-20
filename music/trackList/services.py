from pathlib import Path

from music.adapters.memory_repository import MemoryRepository


def retrieve_tracks(repo: MemoryRepository):

    repo.add_tracks()
    return repo.tracks
