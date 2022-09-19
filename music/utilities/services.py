from typing import Iterable
import random

from music.adapters.repository import AbstractRepository
from music.domainmodel import Track


def get_tracks_names(repo: AbstractRepository):
    # pass
    tracks = repo.add_tracks()
    tracks_names = [track.track_name for track in tracks]
    return tracks_names

# TODO we COULD salvage this piece of code to get tracks instead of articles
def get_random_tracks(quantity, repo: AbstractRepository):
    tracks_count = repo.get_number_of_tracks()

    if quantity >= tracks_count:
        # Reduce the quantity of ids to generate if the repository has an insufficient number of articles.
        quantity = tracks_count - 1

    # Pick distinct and random articles.
    random_ids = random.sample(range(1, tracks_count), quantity)
    tracks = repo.get_tracks_by_id(random_ids)

    return tracks_to_dict(tracks)


# ============================================
# Functions to convert dicts to model entities
# ============================================


def track_to_dict(track: Track):
    track_dict = {
        'date': track.date,
        'title': track.title,
        'image_hyperlink': track.image_hyperlink
    }
    return track_dict


def tracks_to_dict(tracks: Iterable[Track]):
    return [track_to_dict(track) for track in tracks]