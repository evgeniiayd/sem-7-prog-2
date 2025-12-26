from flask import Blueprint, jsonify
import requests
import os

# Создаем Blueprint вместо Flask app
movie_info_bp = Blueprint('movie_info', __name__)

OMDB_API_KEY = os.environ.get('OMDB_API_KEY', 'your_default_key_here')


@movie_info_bp.route('/movies/<string:title>', methods=['GET'])
def get_movie_info(title):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if data.get('Response') == 'False':
            return jsonify({'error': 'Movie not found'}), 404

        movie_data = {
            'title': data.get('Title'),
            'year': data.get('Year'),
            'genre': data.get('Genre'),
            'director': data.get('Director'),
            'actors': data.get('Actors'),
            'imdb_rating': data.get('imdbRating'),
            'plot': data.get('Plot')
        }
        return jsonify(movie_data)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from OMDb API: {e}")
        return jsonify({'error': 'Failed to fetch movie data'}), 500
