from flask import Blueprint, jsonify, request

recommendation_bp = Blueprint('recommendation', __name__)

MOVIE_CATALOG = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "imdb_rating": 9.3},
    {"title": "The Godfather", "genre": "Crime,Drama", "imdb_rating": 9.2},
    {"title": "The Dark Knight", "genre": "Action,Crime,Drama", "imdb_rating": 9.0},
    {"title": "Pulp Fiction", "genre": "Crime,Drama", "imdb_rating": 8.9},
    {"title": "Inception", "genre": "Action,Adventure,Sci-Fi", "imdb_rating": 8.8},
    {"title": "Toy Story", "genre": "Animation,Adventure,Comedy", "imdb_rating": 8.3},
    {"title": "The Matrix", "genre": "Action,Sci-Fi", "imdb_rating": 8.7}
]


@recommendation_bp.route('/recommendations', methods=['GET'])
def get_recommendations():
    genre_filter = request.args.get('genre', '').lower()
    min_rating = float(request.args.get('min_rating', 0))

    recommended_movies = []
    for movie in MOVIE_CATALOG:
        genres = [g.strip().lower() for g in movie['genre'].split(',')]
        if (not genre_filter or genre_filter in genres) and movie['imdb_rating'] >= min_rating:
            recommended_movies.append(movie)

    recommended_movies.sort(key=lambda x: x['imdb_rating'], reverse=True)

    return jsonify(recommended_movies)
