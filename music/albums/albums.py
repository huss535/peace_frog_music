from flask import Blueprint, render_template, url_for, request
from music.adapters.memory_repository import MemoryRepository
from music.trackList.services import retrieve_tracks
import music.adapters.repository as repo
import music.albums.services as services

albums_blueprint = Blueprint(
    'albums_bp', __name__)


@albums_blueprint.route('/tracks_by_album', methods=['GET', 'POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    tracks = tracks_by_album(projectpath)
    return render_template("meat/album.html", track_list=tracks[0],album_name =tracks[1] )


def tracks_by_album(album_name):
    return services.retrieve_tracks(repo.repo_instance, album_name)


@albums_blueprint.route('/searchAlbum', methods=['GET', 'POST'])
def form_page():
    return render_template('meat/search_albums.html')


