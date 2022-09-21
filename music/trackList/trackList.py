from flask import Blueprint, render_template, url_for
from music.adapters.memory_repository import MemoryRepository
from music.trackList.services import retrieve_tracks
import music.adapters.repository as repo
import music.trackList.services as services

track_blueprint = Blueprint(
    'trackList_bp', __name__)


@track_blueprint.route('/track-forward', methods=['GET'])
def trackList():
    list_of_tracks = services.retrieve_tracks(repo.repo_instance)
    increment_indices(repo.repo_instance.first, repo.repo_instance.last, list_of_tracks)
    track_list = list_of_tracks[repo.repo_instance.first:repo.repo_instance.last]
    return render_template(
        'meat/list_of_tracks.html', track_list=track_list
    )


@track_blueprint.route('/track-backward', methods=['GET'])
def backward_trackList():
    list_of_tracks = services.retrieve_tracks(repo.repo_instance)
    # indices = increment_indices(repo.repo_instance.first, repo.repo_instance.last, list_of_tracks)
    repo.repo_instance.first = repo.repo_instance.prev_first
    repo.repo_instance.last = repo.repo_instance.prev_last
    repo.repo_instance.prev_first = 0
    repo.repo_instance.prev_last = 0
    track_list = list_of_tracks[repo.repo_instance.first:repo.repo_instance.last]

    return render_template(
            'meat/list_of_tracks.html', track_list=track_list
        )


def increment_indices(first, last, track_list):
    repo.repo_instance.prev_first = first
    repo.repo_instance.prev_last = last
    first = (last + 1) % len(track_list)
    last = (last + 10) % len(track_list)
    repo.repo_instance.first = first
    repo.repo_instance.last = last


