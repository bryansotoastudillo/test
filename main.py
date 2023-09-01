import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  message = os.environ['MENSAJE']
  print('hola mundo')
  return f'<h1>{message} . Saludos</h1>'


ip = os.environ.get('IP', '0.0.0.0')
port = os.environ.get('PUERTO', '81')

app.run(host=ip, port=port)
