import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'medicine_tracker_secret_2026')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
        'mysql+pymysql://medicine_tracker_betweenhit:1844c5f4adeba18ae046aba080576eeda068aa93@g9vzfc.h.filess.io:3306/medicine_tracker_betweenhit'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')