import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import exc
import json
from database.models import db_drop_and_create_all, setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  #db_drop_and_create_all()

  #Public
  @app.route('/')
  def get_greeting():
    return "Hello, welcome to my FSND Capstone project! \"Casting Agency\" " 
  
  #Casting Assistant, Casting Director and Executive Producer have permission to get:movies 
  @app.route('/movies')
  @requires_auth('get:movies')
  def get_movies(jwt):
    try:
      movies = [movie.format() for movie in Movie.query.order_by(Movie.title).all()]
    except:
      abort(422)
    return jsonify({
      'success': True,
      'movies': movies
    })

  #Casting Assistant, Casting Director and Executive Producer have permission to get:actors   
  @app.route('/actors')
  @requires_auth('get:actors')
  def get_actors(jwt):
    try:
      actors = [actor.format() for actor in Actor.query.order_by(Actor.name).all()]
    except:
      abort(422)
    return jsonify({
      'success': True,
      'actors': actors
    })

  #Executive Producer has permission to delete:movies
  @app.route("/movies/<id>", methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(jwt, id):
      movie = Movie.query.get(id)
      if movie:
          try:
              movie.delete()
              return jsonify({
                  'success': True,
                  'delete': id
              })
          except:
              abort(422)
      else:
          abort(404)

  #Casting Director and Executive Producer have permission to delete:actors
  @app.route("/actors/<id>", methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(jwt, id):
      actor = Actor.query.get(id)
      if actor:
          try:
              actor.delete()
              return jsonify({
                  'success': True,
                  'delete': id
              })
          except:
              abort(422)
      else:
          abort(404)

  #Executive Producer has permission to post:movies
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def post_movies(jwt):
    body = request.get_json()
    if body is None or not ('title' in body and 'release_date' in body) :
      abort(422)      
    new_title = body.get('title')      
    new_release_date = body.get('release_date')
    try:
      movie = Movie(title=new_title, release_date=new_release_date)
      movie.insert()
    except:
      abort(422)
    return jsonify({
      'success': True,
      'created': movie.id,
      'movie': movie.title,
    })

  #Casting Director and Executive Producer have permission to post:actors
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def post_actors(jwt):
    body = request.get_json()
    if body is None or not ('name' in body and 'age' in body and 'gender' in body):
      abort(422)      
    new_name = body.get('name')      
    new_age = body.get('age')
    new_gender = body.get('gender')
    try:
      actor = Actor(name=new_name, age=new_age, gender= new_gender )
      actor.insert()
    except:
      abort(422)
    return jsonify({
      'success': True,
      'created': actor.id,
      'actor': actor.name,
    })

  #Casting Director and Executive Producer have permission to patch:movies
  @app.route("/movies/<id>", methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movies(jwt, id):
      movie = Movie.query.get(id)
      if movie:
          try:
              body = request.get_json()

              title = body.get('title')
              release_date = body.get('release_date')

              if title:
                  movie.title = title
              if release_date:
                  movie.release_date = release_date
              movie.update()
              return jsonify({
                  'success': True,
                  'movie': movie.title,
                  'release_date': movie.release_date
              })
          except:
              abort(422)
      else:
          abort(404)

  #Casting Director and Executive Producer have permission to patch:actors
  @app.route("/actors/<id>", methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actors(jwt, id):
      actor = Actor.query.get(id)
      if actor:
          try:
            body = request.get_json()
            name = body.get('name')
            age = body.get('age')
            gender = body.get('gender')
            if name:
                actor.name = name
            if age:
                actor.age = age
            if gender:
                actor.gender = gender
            actor.update()
            return jsonify({
                'success': True,
                'actor': actor.name,
                'age': actor.age,
                'gender': actor.gender
            })
          except:
            abort(422)
      else:
          abort(404)
  
  ## Error Handling

  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
      }), 422

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
      }), 404

  @app.errorhandler(AuthError)
  def handle_auth_error(ex):
      return jsonify({
        "success": False,
        "error": ex.status_code,
        'message': ex.error
      }), 401

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)