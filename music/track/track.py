from flask import Blueprint, render_template

import music.utilities.utilities as utilities


track_blueprint = Blueprint(
    'track_bp', __name__)


@track_blueprint.route('/', methods=['GET'])
def track():
    return render_template(
        'track/track.html',
        # selected_articles=utilities.get_selected_articles(),
        # tag_urls=utilities.get_tags_and_urls()
    )
