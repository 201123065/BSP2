
from flask import Flask, request

from usuario import Usuario

app = Flask("ejemploJunio")

usuario=Usuario()

@app.route('/metodo2',methods=['POST']) 
def h():
    parametroPython = str(request.form['nombre'])
    parametroPython2 = str(request.form['passwd'])
    return "1"

@app.route('/hola') 
def he():
    return "hola Mundo" 


# GESTION DE USUARIOS
@app.route('/crear_usuario',methods=['POST'])
def crear_usuario():
	usu = str(request.form['nombre'])
	passwd = str(request.form['passwd'])
	return usuario.agregar(usu,passwd,None,False)

@app.route('/modificar_usuario',methods=['POST'])
def modificar_usuario():
	usu = str(request.form['usuario'])
	return usuario.modificar(usu)

@app.route('/eliminar_usuario',methods=['POST'])
def eliminar_usuario():
	usu = str(request.form['usuario'])
	return usuario.eliminar(usu)




if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')