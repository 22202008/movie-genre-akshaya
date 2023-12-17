from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

app = Flask(__name__)

# Sample data for demonstration purposes
movie_data = [
    {'plot': 'An epic tale of love and war', 'genre': 'Drama'},
    {'plot': 'A group of friends embark on a thrilling adventure', 'genre': 'Adventure'},
    # Add more data as needed
]

# Training the model
X_train = [item['plot'] for item in movie_data]
y_train = [item['genre'] for item in movie_data]

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    plot_summary = data['plotSummary']
    predicted_genre = model.predict([plot_summary])[0]
    return jsonify({'genre': predicted_genre})

if __name__ == '__main__':
    app.run(debug=True)



Flask installed (pip install Flask) before running the Python code. You can run the Flask app (python app.py) and access the web application in your browser at http://localhost:5000.


from flask_sqlalchemy import SQLAlchemy

# Create a Flask application to access the SQLAlchemy configuration
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'  # SQLite database file
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plot = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

# Connect to the database
with app.app_context():
    db.init_app(app)

    # Retrieve all movies from the database
    movies = Movie.query.all()

    # Print the results
    for movie in movies:
        print(f"ID: {movie.id}, Plot: {movie.plot}, Genre: {movie.genre}")



Install Flask-SQLAlchemy:

pip install Flask-SQLAlchemy

Modified Python Code (app.py):
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'  # SQLite database file
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plot = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

# Sample data for demonstration purposes
movie_data = [
    {'plot': 'An epic tale of love and war', 'genre': 'Drama'},
    {'plot': 'A group of friends embark on a thrilling adventure', 'genre': 'Adventure'},
    # Add more data as needed
]

# Initialize the database with sample data
with app.app_context():
    db.create_all()
    for item in movie_data:
        movie = Movie(plot=item['plot'], genre=item['genre'])
        db.session.add(movie)
    db.session.commit()

# Training the model
X_train = [item.plot for item in Movie.query.all()]
y_train = [item.genre for item in Movie.query.all()]

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    plot_summary = data['plotSummary']
    predicted_genre = model.predict([plot_summary])[0]
    return jsonify({'genre': predicted_genre})

if __name__ == '__main__':
    app.run(debug=True)

