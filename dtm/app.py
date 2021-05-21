from flask import Flask
from dtm.config.configure import init_app, load_extensions
from dtm.services.socketio import start_app
from flask_migrate import Migrate
import os

app = Flask(__name__)
url = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = url if "localhost" in url else url.replace('postgres://', 'postgresql://')
init_app(app)
load_extensions(app)
Migrate(app, app.db)

if __name__ == "__main__":
  start_app(app)
