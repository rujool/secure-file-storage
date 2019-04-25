from app import app
from flask import render_template, request
from app.models import FileDetails
from app import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']

    newFile = FileDetails(name = file.filename, data = file.read())
    db.session.add(newFile)
    db.session.commit()

    return 'Saved ' + file.filename + ' To the SQLite Database'

if __name__ == '__main__':
    app.run(debug=True)
