import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'medicine_tracker_secret_2026')
    uri = os.environ.get('DATABASE_URL', 'postgresql://medicine_tracker_db_0jne_user:VWdUxZYKym9478nW27ibzHvXxhvlIEgz@dpg-d880ed0js32c73ekq050-a/medicine_tracker_db_0jne')
    # Fix for SQLAlchemy compatibility
    if uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')