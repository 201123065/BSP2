
from flask import Flask, request

from usuario import Usuario
from Tablero import Tablero
app = Flask("ejemploJunio")

usuario=Usuario()

battlefield=Tablero()
# GESTION DE USUARIOS


@app.route('/v_s_u',methods=['POST'])
def v_s_u():
	usu = str(request.form['usuario'])
	return usuario.verificar_SU(usu)


@app.route('/crear_usuario',methods=['POST'])
def crear_usuario():
	usu = str(request.form['nombre'])
	passwd = str(request.form['passwd'])
	return usuario.agregar(usu,passwd,None,False)

@app.route('/super_user')
def superuser():
	return usuario.agregar("admin","admin",None,True)

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


@app.route('/prueba')
def prueba():
	battlefield.battlefield(2,2)
	return battlefield.ver_matriz()


# GESTION DE NAVES
@app.route('/naves_csv',methods=['POST'])
def drr():
	return "true";

@app.route('/cargar_nave',methods=['POST'])
def cargar_naves():
	jugador=str(request.form['jugador']   )
	columna=str(request.form['columna']   )
	fila=str(request.form['fila']   	  )
	nivel=str(request.form['nivel']  	  )
	modo=str(request.form['modo']   	  )
	direccion=str(request.form['direccion']   )
	return "true"






if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')