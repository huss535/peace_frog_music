from music.adapters.csvdatareader import load_tracks
from music.adapters.repository import AbstractRepository


def populate(alb, repo: AbstractRepository):
    load_tracks(alb, repo)

