from nodoUser import nodoUser
from nodoJuegos import nodoJuegos
class Usuario():
	def __init__(self):
		self.raiz=None
		self.cadena=None

	def agregar(self,usuario,passwd,juego,su):
		nuevo= nodoUser(usuario,passwd,False,juego,None,None,su)
		if self.raiz==None :
			self.raiz=nuevo
			return "V"
		else:
			aux=self.raiz
			while aux!=None:
				print aux.usuario
				if usuario>aux.usuario:
					if aux.der==None:
						aux.der=nuevo
						return "V"
					aux=aux.der
				elif usuario<aux.usuario:
					if aux.izq==None:
						aux.izq=nuevo
						return "V"
					aux=aux.izq
				else:
					return "F"
			return "F"




	def eliminar(self,usuario):
		temporal=self.raiz	
		if self.raiz==None :
			return "F"
		else:
			aux=self.raiz
			padre=None
			while aux!=None:
				print aux.usuario
				if usuario>aux.usuario:
					if aux.der==None:
						return "F"
					padre=aux
					aux=aux.der
				elif usuario<aux.usuario:
					if aux.izq==None:
						return "F"
					padre=aux
					aux=aux.izq
				else:
					# cuando lo encuentra
					# si es la raiz
					if padre==None:
						if self.raiz.der!=None and self.raiz.izq!=None:
							padre=self.raiz.izq
							self.raiz=self.raiz.der
							tmp=self.raiz
							while tmp.izq!=None:
								tmp=tmp.izq
							tmp.izq=padre
						elif self.raiz.der==None and self.raiz.izq!=None:
							self.raiz=self.raiz.izq
						elif self.raiz.der!=None and self.raiz.izq==None:
							self.raiz=self.raiz.der
						else:
							self.raiz=None

					else:
						if aux.izq==None and aux.der==None:
							if padre.izq==aux:
								padre.izq=None
							else:
								padre.der=None
						elif aux.izq==None and aux.der!=None:
							if padre.izq==aux:
								padre.izq=aux.der
							else:
								padre.der=aux.der
						elif aux.izq!=None and aux.der==None:
							if padre.izq==aux:
								padre.izq=aux.izq
							else:
								padre.der=aux.izq
						elif aux.izq!=None and aux.der!=None:
							if padre.izq==aux:
								temporal= aux.izq
								padre.izq=aux.der
								while padre.izq!=None:
									padre=padre.izq
								padre.izq=temporal
							else:
								temporal= aux.izq
								padre.der=aux.der
								while padre.izq!=None:
									padre=padre.izq
								padre.izq=temporal
					return "V"
			return "F"






	def modificar(self,usuario):
		temporal=self.raiz
		while temporal.usuario!=None:
			if temporal.usuario==usuario:
				tmp=temporal
				self.eliminar(usuario)
				self.agregar(usuario,tmp.passwd,tmp.juego,tmp.su)
				return "V"
			elif temporal.usuario>usuario:
				temporal=temporal.izq
			else:
				temporal=temporal.der
		return "F"

	def login(self,usuario,passwd):
		tmp=self.raiz
		while tmp!=None:
			print tmp.usuario
			print usuario
			print "---------"
			print tmp.passwd
			print passwd
			if tmp.usuario==usuario and tmp.passwd==passwd:
				tmp.loged=True
				return "V"
			elif tmp.usuario>usuario:
				tmp=tmp.izq
			else:
				tmp=tmp.der
		return "F"

	def graficar_usuario(self):
		print "entra"
		nob=Usuario()
		temporal=self.raiz
		self.cadena=""
		resultado = self.preorden(temporal)
		self.cadena="digraph G{"+self.cadena+"}"
		print self.cadena
		return self.cadena

	def preorden(self,tmp):
		print self.cadena
		if(tmp.izq!=None):
			izquierdo=self.preorden(tmp.izq)
			self.cadena=self.cadena+tmp.usuario+"->"+izquierdo+";\n"
		if(tmp.der!=None):	
			derecho=self.preorden(tmp.der)
			self.cadena=self.cadena+tmp.usuario+"->"+derecho+";\n"
		return tmp.usuario

	def verificar_SU(self,usuario):
		tmp=self.raiz
		while tmp!=None:
			if tmp.usuario<usuario:
				if tmp.der==None:
					return "F"
				tmp=tmp.der
			elif tmp.usuario>usuario:
				if tmp.izq==None:
					return "F"
				tmp=tmp.izq
			else:
				if tmp.su==True:
					return "V"
				return "F"

		return "F"
	def cargar_partida(self,usuario,oponente,realizados,acertados,fallados,gana,recibidos):
		temporal=self.raiz
		while temporal!=None:
			if temporal.usuario<usuario:
				if temporal.der==None:
					return "F"
				temporal=temporal.der
				
			elif temporal.usuario>usuario:
				if temporal.izq==None:
					return "F"
				temporal=temporal.izq

			else:
				nuevo = nodoJuegos(oponente,realizados,acertados,fallados,gana,recibidos,None)
				if jugador.juego==None:
					jugador.juego=nuevo
				else:
					nuevo.siguiente=jugador.juego
					jugador.juego=nuevo
				return "V"
			
		return "F"















