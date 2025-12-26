from flask import Blueprint, jsonify, request

review_bp = Blueprint('review', __name__)

reviews_store = {}


@review_bp.route('/reviews/<string:movie_title>', methods=['GET', 'POST'])
def handle_reviews(movie_title):
    if request.method == 'GET':
        movie_reviews = reviews_store.get(movie_title, [])
        return jsonify({movie_title: movie_reviews})

    elif request.method == 'POST':
        new_review = request.get_json()
        if not new_review or 'text' not in new_review or 'rating' not in new_review:
            return jsonify({'error': 'Invalid review data'}), 400

        if movie_title not in reviews_store:
            reviews_store[movie_title] = []

        reviews_store[movie_title].append(new_review)
        return jsonify({'message': 'Review added successfully'}), 201
