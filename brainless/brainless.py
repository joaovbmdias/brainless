"""
Brainless launcher
"""

from flask import render_template
from configuration import app, db
from models.account import Account
from datetime import datetime
import time, continuous_threading

# Create a URL route in our application for "/"
@app.route('/')

def sync():
    time.sleep(5)
    print('SSSYYYYYNNNNNCCC')

def brainless():
    time.sleep(5)
    print('BBRRRAAAIIIINNNNSSSS')

# background workder daemons
sync_daemon = continuous_threading.PausableThread(target=sync)
brainless_daemon = continuous_threading.PausableThread(target=brainless)

def startup():
    """
    Responsible for all needed operations
    before starting the full applications
    """
    db.metadata.create_all(db.engine)
    db.engine.connect().execute('PRAGMA foreign_keys=ON')


def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    startup()
    
    #sync_daemon.start()
    #brainless_daemon.start()

    app.run(host='0.0.0.0', port=5000, debug=True)

    sync_daemon.stop()
    brainless_daemon.stop()