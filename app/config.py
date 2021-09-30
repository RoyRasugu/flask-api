import os


class Development:
    DEBUG = True
    TESTING = False
    DB_NAME=os.environ.get('DB_NAME')
    DB_HOST =os.environ.get('DB_HOST')
    DB_PASSWORD=os.environ.get('DB_PASSWORD')
    DB_USER=os.environ.get('DB_USER')


app_config = {
    'development': Development
}
