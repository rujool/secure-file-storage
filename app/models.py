from app import db

class FileDetails(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<File {}>'.format(self.name)  