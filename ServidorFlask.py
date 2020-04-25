
from flask import Flask, render_template

app = Flask(__name__) #creamos la instancia de la clase

#usamos el decorador router para decirle que URL debe activar nuestra funcion
@app.route('/')
def index():
    return 'Pagina Principal'

@app.route('/hello') #Use el decorador route para vincular una función a una URL
def hello():
    return render_template('hello.html')

#Una aplicacion web siempre debe de estar escuchando peticiones, se hace asi
if __name__ == '__main__': #se hace una validacion para comprobar si
                           #se esta en el archivo principal para ver si es el
                           #archivo de ejecucion y no un modulo
    app.run(host="127.168.0.1", port=9566)
                        #indica que la aplicacion estara en prueba y requiero que se
                        #reinicie cada vez que modifique algo.
