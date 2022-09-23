import pytest

from flask import session


def test_start(client):
    # Check that we can retrieve the home page.
    response = client.get('/')
    assert response.status_code == 200
    assert b'Music Library' in response.data


def test_tracks_page_forward(client):
    response = client.get('/track-forward')
    assert response.status_code == 200
    assert b'Song List' in response.data


def test_tracks_page_backward(client):
    response = client.get('/track-backward')
    assert response.status_code == 200
    assert b'Song List' in response.data


def test_tracks_genres(client):
    response = client.get('/searchGenre')
    assert response.status_code == 200
    assert b'Search by Genre' in response.data

def test_tracks_genres(client):
    response = client.get('/searchArtist')
    assert response.status_code == 200
    assert b'Search by Artist' in response.data