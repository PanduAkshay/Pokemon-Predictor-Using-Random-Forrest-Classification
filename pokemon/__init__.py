from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#replace the secret key...
app.config['SECRET_KEY'] = '331fc3b40fc1c50408b9d8841f53fc6530ad5587f4e07f7e936967d2c2953b8b'


from pokemon import routes