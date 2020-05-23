"""
Brainless launcher
"""

from flask import render_template
from configuration import app, db

# Create a URL route in our application for "/"
@app.route('/')

def startup():
    """
    Responsible for all needed operations
    before starting the full applications
    """
    db.metadata.create_all(db.engine)
    db.engine.connect().execute('PRAGMA foreign_keys=ON')

def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    startup()
    app.run(host='0.0.0.0', port=5000, debug=True)