from pathlib import Path

from music.adapters.repository import AbstractRepository


def retrieve_tracks(repo: AbstractRepository):

    repo.add_tracks()
    return repo.tracks
