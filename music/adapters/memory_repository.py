import os
from music.adapters.repository import AbstractRepository
from music.adapters.csvdatareader import TrackCSVReader


class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):

        album_path = str(os.path.abspath("data/raw_albums_excerpt.csv"))
        tracks_path = str(os.path.abspath("data/raw_tracks_excerpt.csv"))
        self.file_reader = TrackCSVReader(album_path,tracks_path )
        self.tracks = self.file_reader.read_csv_files()

    def get_tracks_album(self,album_name):
        tracks = []
        for song in self.tracks:
            if song.album is not None:
                if type(song.album.title) == str and song.album.title == album_name:
                    tracks.append(song)
        return tracks

    def get_tracks_genre(self,genre_name):
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


trial = MemoryRepository()
print(trial.get_tracks_artist("AWOL"))
