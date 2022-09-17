
from music.adapters.repository import AbstractRepository
from music.adapters.csvdatareader import TrackCSVReader

class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):

        self.file_reader = TrackCSVReader("","")
        self.tracks = list()

    def get_tracks(self, user_name):
        return 0

