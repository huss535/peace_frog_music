from typing import Iterable
import random

from music.adapters.repository import AbstractRepository
from music.domainmodel.track import Track

def get_tracks_names(repo: AbstractRepository):
    pass
    #tags = repo.get_tags()
    #tag_names = [tag.tag_name for tag in tags]

    #return tag_names

# TODO we COULD salvage this piece of code to get tracks instead of tracks
# def get_random_tracks(quantity, repo: AbstractRepository):
#     track_count = repo.get_number_of_tracks()

#     if quantity >= track_count:
#         # Reduce the quantity of ids to generate if the repository has an insufficient number of tracks.
#         quantity = track_count - 1

#     # Pick distinct and random tracks.
#     random_ids = random.sample(range(1, track_count), quantity)
#     tracks = repo.get_tracks_by_id(random_ids)

#     return tracks_to_dict(tracks)


# ============================================
# Functions to convert dicts to model entities
# ============================================

def track_to_dict(track: Track):
    track_dict = {
        'track_id': track.track_id,
        'title': track.title,
        'track_duration': track.track_duration,
        'artist': track.artist,
        'album': track.album,
        'genres': track.genres,
        'track_url': track.track_url

    }
    return track_dict


def tracks_to_dict(tracks: Iterable[Track]):
    return [track_to_dict(track) for track in tracks]






