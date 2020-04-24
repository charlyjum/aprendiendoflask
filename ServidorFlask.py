
from flask import Flask
app = Flask(__name__) #creamos la instancia de la clase

#usamos el decorador router para decirle que URL debe activar nuestra funcion
@app.route('/')
def hello_world():
    return 'Hello,World!'
