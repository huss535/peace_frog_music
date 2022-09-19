import os
from music.adapters.repository import AbstractRepository
from music.adapters.csvdatareader import TrackCSVReader


class MemoryRepository(AbstractRepository):

    def __init__(self):

        self.tracks = []

    def add_tracks(self,albums,tracks):
        #album_path = str(os.path.abspath("data/raw_albums_excerpt.csv"))
        #tracks_path = str(os.path.abspath("data/raw_tracks_excerpt.csv"))
        file_reader = TrackCSVReader(albums, tracks)
        self.tracks = file_reader.read_csv_files()

    def get_number_of_tracks(self):
        return len(self.tracks)

    # def filter_tracks(self, album_name, genre_name, artist_name):
    #     master_tracks = []
    #     if album_name is not None or 

    #     return None

    def get_tracks_by_id(self, id_list):
        # Strip out any ids in id_list that don't represent Article ids in the repository.
        existing_ids = [id for id in id_list if id in self.__tracks_index]

        # Fetch the Articles.
        tracks = [self.__tracks_index[id] for id in existing_ids]
        return tracks

    def get_tracks_album(self, album_name, master_tracks):
        tracks = []
        if len(master_tracks) == 0:
            for song in self.tracks:
                if song.album is not None:
                    if type(song.album.title) == str and song.album.title == album_name:
                        master_tracks.append(song)
        else:
            for song in master_tracks:
                if song.album is not None:

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

    


def populate(albums,tracks,repo: MemoryRepository):
    repo.add_tracks(albums,tracks)


trial = MemoryRepository()
print(trial.get_tracks_artist("AWOL"))
