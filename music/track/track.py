from flask import Blueprint, render_template, url_for, request
from music.adapters.memory_repository import MemoryRepository
from music.authentication.authentication import login_required
from music.trackList.services import retrieve_tracks

import music.adapters.repository as repo
import music.utilities.utilities as utilities
import music.track.services as services

import music.adapters.repository as repo
import music.track.services as services

from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


track_blueprint = Blueprint(
    'track_bp', __name__)


@track_blueprint.route('/track', methods=['GET', 'POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    tracks = track(projectpath)
    return render_template("meat/track.html", track_list=tracks[0],track_name =tracks[1] )


def track(track_name):
    return services.retrieve_track(repo.repo_instance, track_name)


@track_blueprint.route('/track', methods=['GET', 'POST'])
def form_page():
    return render_template('meat/track.html')



@track_blueprint.route('/comment', methods=['GET', 'POST'])
@login_required
def comment_on_track():
    # Obtain the user name of the currently logged in user.
    user_name = session['user_name']

    # Create form. The form maintains state, e.g. when this method is called with a HTTP GET request and populates
    # the form with an track id, when subsequently called with a HTTP POST request, the track id remains in the
    # form.
    form = CommentForm()

    if form.validate_on_submit():
        # Successful POST, i.e. the comment text has passed data validation.
        # Extract the track id, representing the commented track, from the form.
        track_id = int(form.track_id.data)

        # Use the service layer to store the new comment.
        services.add_comment(track_id, form.comment.data, user_name, repo.repo_instance)

        # Retrieve the track in dict form.
        track = services.get_track(track_id, repo.repo_instance)

        # Cause the web browser to display the page of all tracks that have the same date as the commented track,
        # and display all comments, including the new comment.
        return redirect(url_for('news_bp.tracks_by_date', date=track['date'], view_comments_for=track_id))

    if request.method == 'GET':
        # Request is a HTTP GET to display the form.
        # Extract the track id, representing the track to comment, from a query parameter of the GET request.
        track_id = int(request.args.get('track'))

        # Store the track id in the form.
        form.track_id.data = track_id
    else:
        # Request is a HTTP POST where form validation has failed.
        # Extract the track id of the track being commented from the form.
        track_id = int(form.track_id.data)

    # For a GET or an unsuccessful POST, retrieve the track to comment in dict form, and return a Web page that allows
    # the user to enter a comment. The generated Web page includes a form object.
    track = services.get_track(track_id, repo.repo_instance)
    return render_template(
        'news/comment_on_track.html',
        title='Edit track',
        track=track,
        form=form,
        handler_url=url_for('news_bp.comment_on_track'),
        selected_tracks=utilities.get_selected_tracks(),
        tag_urls=utilities.get_tags_and_urls()
    )

# for now, no profanity filters because I don't know how to make one.
# show society it's ills.

# from better_profanity import profanity
# class ProfanityFree:
#     def __init__(self, message=None):
#         if not message:
#             message = u'Field must not contain profanity'
#         self.message = message
#     def __call__(self, form, field):
#         if profanity.contains_profanity(field.data):
#             raise ValidationError(self.message)


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short'),
        #ProfanityFree(message='Your comment must not contain profanity') TOOO LAZY TO IMPLEMENT
    ])
    track_id = HiddenField("Track id")
    submit = SubmitField('Submit')