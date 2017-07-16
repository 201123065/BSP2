from nodoTablero import nodoTablero

class Tablero():
	def __init__(self):
		self.tablero=None
		self.fila=0
		self.columna=0

	def battlefield(self,fila,columna):
		self.fila=fila
		self.columna=columna
		self.tablero=None
		x=0
		y=0
		z=0
		base_y=None
		base_x=None
		raiz=None
		mueveX=None
		mueveY=None
		base=None
		mueve=None
		fan=None
		while x<fila:
			while y<columna:
				while z<4:
					casilla = nodoTablero("0",None,None,None,None,None,None)
					if(self.tablero==None):
						self.tablero=casilla
						base=self.tablero
						mueve=self.tablero
						mueveX=self.tablero
						mueveY=self.tablero
						base_y=self.tablero
						base_x=self.tablero
						fan=self.tablero
					else:
						if y==0 and x==0:
							mueve.up=casilla
							casilla.down=mueve
							mueve=mueve.up

						elif y==0:
							if z==0:
								mueve.frente=casilla
								casilla.tras=mueve
								mueve=mueve.frente
								base=mueve
								mueveY=base
								base_y=base
							else:
								casilla.down=mueve
								mueve.up=casilla
								mueveX=mueveX.up
								mueve=mueve.up
								mueve.tras=mueveX
								mueveX.frente=mueve
						elif x==0:
							if z==0:
								mueve=base_x
								mueve.der=casilla
								casilla.izq=mueve
								mueve=mueve.der
								base_x=mueve
							else:
								casilla.down=mueve
								mueve.up=casilla
								mueve=mueve.up
								mueveX=mueveX.up
								mueve.izq=mueveX
								mueveX.der=mueve
						else:
							if z==0:
								mueve=base_y
								mueveY=base_y
								mueveX=base_x.der
								base_x=base_x.der
								mueveY=base_y
								mueve.der=casilla
								casilla.izq=mueve
								mueve=mueve.der
								base_y=mueve
							else:
								mueveX=mueveX.up
								mueveY=mueveY.up
								mueve.up=casilla
								casilla.down=mueve
								mueve=mueve.up
								mueveY.der=mueve
								mueve.izq=mueveY

							mueveX.frente=mueve
							mueve.tras=mueveX	

					z=z+1
				z=0
				y=y+1
			mueveX=base
			mueveY=base
			base_y=base
			base_x=base
			mueve=base
			y=0
			x=x+1

		return "v"

	def ver_matriz(self):
		cadena=""
		x=0
		y=0
		z=0
		tmp=self.tablero
		while x<self.fila:
			while y<self.columna:
				while z<4:
					
					z=z+1
				z=0
				y=y+1
			y=0
			x=x+1
			cadena=cadena+"\n"
		return cadena
		



		