from app import app
from flask import render_template, request
from flask import send_file
from io import BytesIO
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


@app.route('/download')
def download():
    fileData = FileDetails.query.filter_by(id=1).first()    
    return send_file(BytesIO(fileData.data), attachment_filename='flask.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
