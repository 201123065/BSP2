from nodoMatriz import nodoMatriz

class Tablero():
	def __init__(self):
		self.tablero=None
		self.fila=0
		self.columna=0

	def crear(self,x,y):
		self.fila=x
		self.columna=y
		fila=0
		columna=0
		mueve=None
		temporal=None
		inicio=None
		previo=None
		up_left=None
		while fila<x:
			while columna<y:
				if self.tablero==None:
					self.tablero=nodoMatriz(0,None,None,None,None,None,None)
					temporal=self.tablero
					mueve=self.tablero
					inicio=self.tablero
					abajo=self.tablero
					# UP_DOWN
					for x in range (0,3):
						sube=nodoMatriz(0,None,None,None,None,None,None)
						abajo.up=sube
						sube.down=abajo
						abajo=abajo.up
				elif fila==0:
					#UP_DOWN... FORWARD_BACK
					abajo=nodoMatriz(0,None,None,None,None,None,None)
					abajo.back=mueve
					mueve.forward=abajo
					tmp=mueve
					mueve=abajo
					for x in range(0,3):
						sube=nodoMatriz(0,None,None,None,None,None,None)
						abajo.up=sube
						sube.down=abajo
						abajo=abajo.up
						tmp=tmp.up
						tmp.forward=abajo
						abajo.back=tmp
				else:
					abajo=nodoMatriz(0,None,None,None,None,None,None)
					abajo.left=temporal
					temporal.right=abajo
					up_left=temporal
					if columna==0:
					# UP_DOWN...LEFT_RIGHT
						previo=abajo
						for x in range (0,3):
							up_left=up_left.up
							sube=nodoMatriz(0,None,None,None,None,None,None)
							abajo.up=sube
							sube.down=abajo
							abajo=abajo.up
							abajo.left=up_left
							up_left.right=abajo
					else:
						# UP_DOWN...LEFT_RIGHT...FORWARD_BACK
						prv=previo
						previo=previo.forward
						for x in range (0,3):
							up_left=up_left.up
							sube=nodoMatriz(0,None,None,None,None,None,None)
							abajo.up=sube
							sube.down=abajo
							abajo=abajo.up
							abajo.left=up_left
							up_left.right=abajo
							prv.forward=abajo
							abajo.back=prv

					temporal=temporal.forward
				columna=columna+1
			columna=0
			temporal=inicio
			inicio=inicio.right
			fila=fila+1
		return "v"

	def verTablero(self):
		if self.tablero.right!=None:
			if self.tablero.forward!=None:
				# quiere decir que no es un misero arreglo de 1x1x4
				fila=self.tablero.right
				columna=fila
				cadena=""
				x=0
				y=0
				while fila:
					while columna:
						for z in range(0,3):
							cadena=cadena+"\""
						columna=columna.forward
					fila=fila.right
					columna=fila
					columna=columna+1
					y=x
					x=x.right
			else:
				# es un arreglode nx1x4(practicamente una matriz)
		else:
			if self.tablero.forward!=None:
				# es una matriz
			else:
				# es un inche vector




				if(fila==0)
		while fila<self.fila:
			while columna<self.columna:
				if fila==0:
					if columna==0:
						for x in xrange(0,3):
							# UP_DOWN
							cadena=cadena+"\""+fila","+columna+","+str(int(x+1))+"_"+tmp.up.ocupado+"\"->\""+fila","+columna+","+x+"_"tmp+"\";\n"
							cadena=cadena+"\""+fila","+columna+","+x+"_"+tmp+"\"->\""+fila","+columna+","+str(int(x+1))+"_"tmp.up.ocupado+"\";\n"
					else:
						# LEFT_RIGHT
						cadena=cadena+"\""+fila","+columna+","+str(int(x+1))+"_"+tmp.up.ocupado+"\"->\""+fila","+columna+","+x+"_"tmp+"\";\n"
						cadena=cadena+"\""+fila","+columna+","+x+"_"+tmp+"\"->\""+fila","+columna+","+str(int(x+1))+"_"tmp.up.ocupado+"\";\n"
						for x in xrange(0,3):
							# UP_DOWN
							cadena=cadena+"\""+fila","+columna+","+str(int(x+1))+"_"+tmp.up.ocupado+"\"->\""+fila","+columna+","+x+"_"tmp+"\";\n"
							cadena=cadena+"\""+fila","+columna+","+x+"_"+tmp+"\"->\""+fila","+columna+","+str(int(x+1))+"_"tmp.up.ocupado+"\";\n"
							# FORWARD_BACK
							cadena=cadena+"\""+fila","+columna+","+str(int(x+1))+"_"+tmp.up.ocupado+"\"->\""+fila","+columna+","+x+"_"tmp+"\";\n"
							cadena=cadena+"\""+fila","+columna+","+x+"_"+tmp+"\"->\""+fila","+columna+","+str(int(x+1))+"_"tmp.up.ocupado+"\";\n"
				elif columna==0:


				columna=columna+1
				tmp=tmp.forward
			columna=0
			tmp
			fila=fila+1
		while :
			pass

	def cargar_nave(self,fila,columna,nivel,modo,direccion):
		return "true"

		