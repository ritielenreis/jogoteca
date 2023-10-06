import os
SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='#Portugal2021',
        servidor='127.0.0.1:13306',
        database='jogoteca'
    )


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
