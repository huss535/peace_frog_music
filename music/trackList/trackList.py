from flask import Blueprint, render_template
import music.adapters.memory_repository as repo
from music.trackList.services import retrieve_tracks

track_blueprint = Blueprint(
    'trackList_bp', __name__)


@track_blueprint.route('/tracks', methods=['GET'])
def trackList():
    list_of_tracks = retrieve_tracks(repo)
    return render_template(
        'meat.list_of_tracks.html', track_list=list_of_tracks
    )
