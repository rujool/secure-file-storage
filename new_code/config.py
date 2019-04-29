import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPLOAD_FOLDER = 'uploaded_files'
	ALLOWED_EXTENSIONS = ['txt','pdf','png','jpg','doc','docx','ppt','pptx','xls','xlsx','csv']
	MAX_FILE_SIZE = 50000000	# 50 MB