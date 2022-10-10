from flask import Blueprint, render_template

import music.utilities.utilities as utilities
from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

# WE CONDONE PROFANITY
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import music.adapters.repository as repo
import music.utilities.utilities as utilities
import music.reviews.services as services

review_blueprint = Blueprint(
    'reviews_bp', __name__)


@review_blueprint.route('/', methods=['GET'])
def review():
    return render_template(
        'review/review.html',
        # selected_tracks=utilities.get_selected_tracks(),
        # tag_urls=utilities.get_tags_and_urls()
    )

@review_blueprint.route('/review', methods=['GET', 'POST'])
def review_on_track():
    # (COMMENTED OUT)Obtain the user name of the currently logged in user. 
    # user_name = session['user_name']

    # Create form. The form maintains state, e.g. when this method is called with a HTTP GET request and populates
    # the form with an track id, when subsequently called with a HTTP POST request, the track id remains in the
    # form.
    form = reviewForm()

    if form.validate_on_submit():
        # Successful POST, i.e. the review text has passed data validation.
        # Extract the track id, representing the reviewed track, from the form.
        track_id = int(form.track_id.data)

        # Use the service layer to store the new review.
        services.add_review(track_id, form.review.data, repo.repo_instance)

        # Retrieve the track in dict form.
        track = services.get_track(track_id, repo.repo_instance)

        # (COMMENTED OUT)Cause the web browser to display the page of all tracks that have the same date as the reviewed track,
        # and display all reviews, including the new review.
        # return redirect(url_for('tracks_bp.tracks_by_date', date=track['date'], view_reviews_for=track_id))
        return

    if request.method == 'GET':
        # Request is a HTTP GET to display the form.
        # Extract the track id, representing the track to review, from a query parameter of the GET request.
        track_id = int(request.args.get('track'))

        # Store the track id in the form.
        form.track_id.data = track_id
    else:
        # Request is a HTTP POST where form validation has failed.
        # Extract the track id of the track being reviewed from the form.
        track_id = int(form.track_id.data)

    # For a GET or an unsuccessful POST, retrieve the track to review in dict form, and return a Web page that allows
    # the user to enter a review. The generated Web page includes a form object.
    track = services.get_track(track_id, repo.repo_instance)
    return render_template(
        'meat/reviews.html',
        title='Edit Review',
        track=track,
        form=form,
        handler_url=url_for('reviews_bp.review_on_track')
    )

class reviewForm(FlaskForm):
    review = TextAreaField('review', [
        DataRequired(),
        Length(min=4, message='Your review is too short')])
    track_id = HiddenField("track id")
    submit = SubmitField('Submit')