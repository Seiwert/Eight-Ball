from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)

# Install the bootstrap extension
Bootstrap(app)

from app import serve