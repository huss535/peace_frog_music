from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship, synonym

from music.domainmodel import album, artist, genre, playlist, review, track, user

# global variable giving access to the MetaData (schema) information of the database
metadata = MetaData()

tracks_table = Table(
    'tracks', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('track_id', Integer, unique=True, nullable=False),
    Column('artists_id',  ForeignKey('artists.artist_id')),
    Column('title', String(255), nullable=False),
    Column('track_url', String(255), nullable=False),
    Column('track_duration', Integer, nullable=False)
)

artists_table = Table(
    'artists', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('artist_id', Integer, unique=True, nullable=False),
    Column('full_name', String(1024), nullable=False)

)

users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, unique=True, nullable=False),
    Column('user_name', String(1024), unique=True, nullable=False),
    Column('password', String(1024), nullable=False)
)

genres_table = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('genre_id', Integer, unique=True, nullable=False),
    Column('name', String(1024), unique=True, nullable=False)
)

albums_table = Table(
    'albums', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('album_id', Integer, unique=True, nullable=False),
    Column('title', String(255), nullable=False),
    Column('album_url', String(255), nullable=False),
    Column('album_type', String(255), nullable=False),
    Column('release_year', Integer)
)


def map_model_to_tables():
    mapper(track, tracks_table, properties={
        '_track__title': tracks_table.c.title,
        '_track__tracks_id': tracks_table.c.track_id,
        '_track__track_url': tracks_table.c.track_url,
        '_track__track_duration': tracks_table.c.track_duration,
        '_track__artist': relationship(artist, backref="_artist__artist_id")

    })

