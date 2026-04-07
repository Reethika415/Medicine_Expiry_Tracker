class Config:
    SECRET_KEY = 'medicine_tracker_secret_key'
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://root:1234@localhost/medicine_tracker'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False