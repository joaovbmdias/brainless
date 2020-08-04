"""
Brainless launcher
"""

from flask import render_template
from configuration import app, db
from datetime import datetime
import continuous_threading
from daemons.sync import sync_accounts

# Create a URL route in our application for "/"
@app.route('/')

def brainless():
    print('BBRRRAAAIIIINNNNSSSS')

# background workder daemons
sync_daemon = continuous_threading.PeriodicThread(10,target=sync_accounts)
brainless_daemon = continuous_threading.PausableThread(target=brainless)

#@app.before_first_request
def _run_on_start():
    """
    Responsible for all needed operations
    before starting the full application
    """
    db.metadata.create_all(db.engine)
    
    #sync_daemon.start()
    #brainless_daemon.start()


def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    _run_on_start()

    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
