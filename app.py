# app.py
from flask import Flask
from data_api import data_bp  # Import the data blueprint

app = Flask(__name__)

# Register the data blueprint with the Flask app
app.register_blueprint(data_bp)

if __name__ == '__main__':
    app.run(debug=True)
