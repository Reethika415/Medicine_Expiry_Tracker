import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'medicine_tracker_secret_2026')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 
        'mysql+pymysql://admin:Medicine1234!@medicine-tracker-db.cdwg0usiq6jf.ap-south-1.rds.amazonaws.com/medicine_tracker'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False