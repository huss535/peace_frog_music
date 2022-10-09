from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship, synonym

# global variable giving access to the MetaData (schema) information of the database
from music.domainmodel.track import Track
from music.domainmodel import track, artist, album
from music.domainmodel.album import Album
from music.domainmodel.artist import Artist
from music.domainmodel.genre import Genre

metadata = MetaData()

albums_table = Table(
    'albums', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),

    Column('title', String(255)),
    Column('album_url', String(255)),
    Column('album_type', String(255)),
    Column('release_year', Integer)
)

artists_table = Table(
    'artists', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, unique=True),

    Column('full_name', String(1024))

)

genres_table = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),

    Column('name', String(1024)),
    Column('tracks', String(1024))

)

tracks_table = Table(
    'tracks', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),

    Column('artists_id', ForeignKey('artists.id')),
    Column('albums_id', ForeignKey('albums.id')),
    Column('genres_id', ForeignKey('genres.id')),

    Column('title', String(255)),
    Column('track_url', String(255)),
    Column('track_duration', Integer)
)

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),

    Column('user_name', String(1024), unique=True),
    Column('password', String(1024))
)
genres_tracks_table = Table(
    'genres_tracks', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('track_id', ForeignKey('tracks.id')),
    Column('genre_id', ForeignKey('genres.id'))
)


def map_model_to_tables():
    mapper(Album, albums_table, properties={
        '_Album__title': albums_table.c.title,
        '_Album__album_id': albums_table.c.id,
        '_Album__album_url': albums_table.c.album_url,
        '_Album__album_type': albums_table.c.album_type,
        '_Album__release_year': albums_table.c.release_year

    })

    mapper(Artist, artists_table, properties={
        '_Artist__full_name': artists_table.c.full_name,
        '_Artist__artist_id': artists_table.c.id,

    })

    mapper(Genre, genres_table, properties={
        '_Genre__genre_id': genres_table.c.id,
        '_Genre__name': genres_table.c.name,
        '_Genre__tracks':  relationship(
            Track,
            secondary=genres_tracks_table,
            back_populates="_Track__genres"
        )

    })

    mapper(Track, tracks_table, properties={
        '_Track__title': tracks_table.c.title,
        '_Track__track_id': tracks_table.c.id,
        '_Track__track_url': tracks_table.c.track_url,
        '_Track__track_duration': tracks_table.c.track_duration,
        '_Track__album': relationship(Album, backref="_Track__album_id"),
        '_Track__artist': relationship(Artist, backref="_Track__artist_id"),
        '_Track__genres': relationship(Genre, secondary=genres_tracks_table,
                                       back_populates='_Genre__tracks')
    })
