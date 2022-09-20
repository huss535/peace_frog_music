import os
from pathlib import Path

from music.adapters.repository import AbstractRepository
from music.adapters.csvdatareader import TrackCSVReader

from music.domainmodel import track


class MemoryRepository(AbstractRepository):

    def __init__(self):

        self.tracks = []

    def add_tracks(self ):
        albums = str(Path('music') / 'adapters' / 'data' / 'raw_albums_excerpt.csv')
        tracks = str(Path('music') / 'adapters' / 'data' / 'raw_tracks_excerpt.csv')
        file_reader = TrackCSVReader(albums, tracks)
        self.tracks = file_reader.read_csv_files()

    def get_tracks_album(self, album_name):
        tracks = []
        for song in self.tracks:
            if song.album is not None:
                if type(song.album.title) == str and song.album.title == album_name:
                    tracks.append(song)
        return tracks

    def get_tracks_genre(self, genre_name):
        tracks = []
        for song in self.tracks:
            if len(song.genres) != 0:
                for genre in song.genres:
                    if genre.name == genre_name:
                        tracks.append(song)
        return tracks

    def get_tracks_artist(self, artist_name):
        tracks = []
        for song in self.tracks:
            if song.artist.full_name == artist_name:
                tracks.append(song)

        return tracks


def populate(repo: MemoryRepository):
    repo.add_tracks()


trial = MemoryRepository()
print(trial.get_tracks_artist("AWOL"))
