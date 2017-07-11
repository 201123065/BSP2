
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

@app.route('/login',methods=['POST'])
def login_usuario():
	usu = str(request.form['nombre'])
	passwd = str(request.form['passwd'])
	return usuario.login(usu,passwd)

@app.route('/abb_user',methods=['POST'])
def abb_user():
	return usuario.graficar_usuario()

@app.route('/partida',methods=['POST'])
def partida():
	us=str(request.form['usuario']   )
	op=str(request.form['oponente']  )
	re=str(request.form['realizados'])
	ac=str(request.form['acertados'] )
	fa=str(request.form['fallados']  )
	ga=str(request.form['gana']      )
	re=str(request.form['recibidos'] )
	return usuario.cargar_partida(us,op,re,ac,fa,ga,re)



# GESTION DE ESCENARIO
@



if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')