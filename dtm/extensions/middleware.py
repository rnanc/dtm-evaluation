from flask_socketio import SocketIO
from engineio.payload import Payload
from dtm.listeners.exam import open_measurement, shut_measurement
import os

Payload.max_decode_packets = 1000
web = {'async_mode': 'eventlet', 'pingTimeout': 900, 'logger': True, 'engineio_logger': True, 'cors_allowed_origins': "*"}
local = {'pingTimeout': 900, 'cors_allowed_origins': "*"}

socketio = SocketIO(cors_allowed_origins="*")
socketio.on_event('open_measurement', open_measurement, namespace='/exam')
socketio.on_event('shut_measurement', shut_measurement, namespace='/exam')

def init_app(app):
  #socketio.server_options.update(local if os.environ.get('FLASK_ENV') == 'development' else web)
  socketio.init_app(app)

def start_app(app):
  socketio.run(app, host='0.0.0.0', port='443')

