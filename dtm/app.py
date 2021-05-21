import os
from dtm.extensions.configure import init_app, load_extensions
from dtm.extensions.middleware import start_app
from flask import Flask

app = Flask(__name__)
url = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
init_app(app)
load_extensions(app)

if __name__ == "__main__":
  start_app(app)
