import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor, db,db_drop_and_create_all
from datetime import datetime
import random
import dateutil.parser
import babel
#from auth import AuthError, requires_auth

# def create_app(test_config=None):
#   # create and configure the app
app = Flask(__name__, instance_relative_config=True)
setup_db(app)
  #uncomment to create database for the first time

#db_drop_and_create_all() 
CORS(app)

def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format)

    app.jinja_env.filters['datetime'] = format_datetime


'''
Movies
'''

'''
Create an endpoint to handle GET requests for all movies
'''
@app.route("/movies",methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    if len(movies) == 0:
      abort(404)
    data = []
    for movie in movies:
      data.append(movie.format())

    return jsonify({
        'success': True,
        'movies': data,
        'total_movies': len(movies)
      })

'''
Create an endpoint to delete a movie
'''
@app.route("/movies/<int:movie_id>",methods=['DELETE'])
#@requires_auth('delete:movies')
def delete_movie(payload,movie_id):
  try:
    Movie.query.filter(Movie.id == movie_id).one_or_none().delete
    
    return jsonify({
      'success': True,
      'message': "Movie was deleted successfully",
      'deleted': movie_id
    })
  except BaseException:
    abort(404)

'''
Create an endpoint to post a new movie
'''
@app.route("/movies",methods=['POST'])
##@requires_auth('post:movies')
def add_movie(payload):
  try:
    new_movie = Movie(
      title = "Test title",
      release_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    )
    new_movie.insert()
    return jsonify({
      'success': True,
      'movies': new_movie.format(),
      'created': new_movie.id,
      'total_movies': len(Movie.query.all())
    })
  except BaseException:
    abort(422)

'''
Create an endpoint to patch an existing movie
'''
@app.route("/movies/<int:movie_id>",methods=['PATCH'])
#@requires_auth('patch:movies')
def patch_movie(payload, movie_id):
  try:
    title_update = 'Updated title',
    release_date_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    movie_update = Movie.query.filter(Movie.id == movie_id).one_or_none()

    if movie_update is None:
      abort(404)
    
    movie_update.title = title_update
    movie_update.release_date = release_date_update
    movie_update.update()

    return jsonify({
      'success': True,
      'movies': movie_update.format(),
      'total_movies': len(Movie.query.all())
    })
  
  except BaseException:
    abort(422)


'''
Actors
'''

  # Create an endpoint to handle GET requests for all actors
@app.route("/actors",methods=['GET'])
def get_actors():
  actors = Actor.query.all()
  if len(actors) == 0:
    abort(404)
  data = []
  for actor in actors:
    data.append(actor.format())
  return jsonify({
    'success': True,
    'actors': data,
    'total_actors': len(actors)
  })

