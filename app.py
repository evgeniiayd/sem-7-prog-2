from flask import Flask
from movie_info_service import movie_info_bp
from recommendation_service import recommendation_bp
from review_service import review_bp

app = Flask(__name__)

# Регистрируем blueprint'ы
app.register_blueprint(movie_info_bp, url_prefix='/movie-info')
app.register_blueprint(recommendation_bp, url_prefix='/recommendations')
app.register_blueprint(review_bp, url_prefix='/review')

@app.route('/')
def index():
    return "Movie Recommendation Microservices are running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)