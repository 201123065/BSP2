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
		raiz=None
		mueve=None
		mueveY=None
		base=None
		mueve=None
		while x<fila:
			while y<columna:
				while z<4:
					casilla = nodoTablero("0",None,None,None,None,None,None)
					if(self.tablero==None):
						self.tablero=casilla
						base=self.tablero
						mueve=self.tablero
						mueve=self.tablero
						mueveY=self.tablero
						base_y=self.tablero
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
							else:
								casilla.down=mueve
								mueve.up=casilla
								mueve=mueve.up
								mueve=mueve.up
								mueve.tras=mueve
								mueve.frente=mueve
						elif x==0:
							if z==0:
								mueve.der=casilla
								casilla.izq=mueve
								mueve=mueve.der
							else:
								casilla.down=mueve
								mueve.up=casilla
								mueve=mueve.up
								mueve=mueve.up
								mueve.izq=mueve
								mueve.der=mueve
						else:
							if z==0:
								mueve=base_y
								mueve=mueve.der
								mueveY=base_y
								mueve.der=casilla
								casilla.izq=mueve
								mueve=mueve.der
								base_y=mueve
							else:
								# mueve=mueve.up
								mueveY=mueveY.up
								mueve.up=casilla
								casilla.down=mueve
								mueve=mueve.up
								mueveY.der=mueve
								mueve.izq=mueveY

							mueve.frente=mueve
							mueve.tras=mueve	

					z=z+1
				z=0
				y=y+1
			mueve=base
			mueve=base
			mueveY=base
			base_y=base
			y=0
			x=x+1

		return "v"

	def ver_matriz(self):
		return self.tablero.up.valor



		