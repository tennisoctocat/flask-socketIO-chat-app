"""
Changes made that were different than the tutorial:

In order to run this, I had to create a python virtual env called flask-socketio-env)
so that I wouldn't already have all the other random packages installed. 
This is because some of the other packages I installed because of the other
Flask Video app like wsgi were made for production time, and did not work with this tutorial.

In general, it is porbably better to use virtual environments, to avoid having thousands of packages installed everywhere.

I also had to use pip install flask-socketio==4.3.2 in order to make sure that 
the flask-socketio, python-socketio, and python-engineio verisons would all be compatible 
with each other.

Had to add 'cors_allowed_origins="*"' to the SocketIO call. to allow ngrok as an origin.

Had to take out the parameters in io.connect() to avoid Mixed types (i.e. http from the parameter and https from ngrok)
It seemed to work just fine even though I took out the parameter.
"""

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app, cors_allowed_origins="*") # Had to include cors_allowed_origins="*" (see https://stackoverflow.com/questions/57397269/get-socket-io-eio-3transport-pollingt-mnihjpm-http-1-1) in order for this to work with ngrok.


@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)
