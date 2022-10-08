from abc import ABC
from datetime import date
from typing import List

from sqlalchemy import desc, asc
# from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.orm import scoped_session

from music.adapters.repository import AbstractRepository
from music.domainmodel import Track, Album, Genre, Artist


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class database_repository(AbstractRepository):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_tracks(self, track: Track):
        with self._session_cm as scm:
            scm.session.add(track)
            scm.commit()

    def add_albums(self, album: Album):
        with self._session_cm as scm:
            scm.session.add(album)
            scm.commit()

    def add_genres(self, genre: Genre):
        with self._session_cm as scm:
            scm.session.add(genre)
            scm.commit()

    def add_artists(self, artist: Artist):
        with self._session_cm as scm:
            scm.session.add(artist)
            scm.commit()

    def get_tracks_album(self, album_name) -> List[Track]:
        if album_name is None:
            Tracks = self._session_cm.session.query(Track).all()
        else:
            # Return Tracks matching album_name; return an empty list if there are no matches.
            # Track.__album should return album object associated with the Track
            # Track.__album.__title returns the title of the associated album
            Tracks = self._session_cm.session.query(Track).filter(Track.__album.__title == album_name).all()
        return Tracks, album_name
    
    def get_tracks_artist(self, artist_name):
        if artist_name is None:
            Tracks = self._session_cm.session.query(Track).all()
        else:
            # Return Tracks matching artist_name; return an empty list if there are no matches.
            # Track.__artist should return artist object associated with the Track
            # Track.__artist.__full_name should return the artist name
            Tracks = self._session_cm.session.query(Track).filter(Track.__artist.__full_name == artist_name).all()
        return Tracks, artist_name

    # BANDAID SOLUTION, USING METHOD RAXXED FROM MEMORY REPO, MAY CHANGE IF HAVE TIME
    def get_tracks_genre(self, genre_name: str):
        Tracks = []
        all_tracks = self._session_cm.session.query(Track).all()
        for song in all_tracks:
            if len(song.genres) != 0:
                for genre in song.genres:
                    if genre.name == genre_name:
                        Tracks.append(song)
        return Tracks, genre_name