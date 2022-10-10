import abc

from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre
from music.domainmodel.review import Review

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_tracks(self, alb):
        raise NotImplementedError

    @abc.abstractmethod
    def add_albums(self, album: Album):
        raise NotImplementedError

    @abc.abstractmethod
    def add_genres(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def add_artists(self, artist: Artist):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_album(self,album_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_genre(self,genre_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_artist(self, artist_name):
        raise NotImplementedError

# NEW ABSTRACT METHODS FOR REVIEW

    @abc.abstractmethod
    def get_track(self, track_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a review to the repository.

        We care little for so called 'bidrectional links' between Tracks and Users.
        A great review can come from an instant spark of creativity, something which may be hindered when
        a user is smacked with an error calling for registration.
        """
        if review.track is None or review not in review.track.reviews:
            raise RepositoryException('Review not correctly attached to a Track')

    @abc.abstractmethod
    def get_reviews(self):
        """ Returns the reviews stored in the repository. """
        raise NotImplementedError

# @abc.abstractmethod
# def get_tracks_album(self, album_name):
# raise NotImplementedError

# @abc.abstractmethod
# def get_tracks_genre(self, album_name):
# raise NotImplementedError

# @abc.abstractmethod
#  def get_tracks_artist(self, album_name):
#  raise NotImplementedError
