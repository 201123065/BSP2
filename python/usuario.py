from nodoUser import nodoUser

class Usuario():
	def __init__(self):
		self.raiz=None
		self.cadena=None

	def agregar(self,usuario,passwd,juego,su):
		nuevo= nodoUser(usuario,passwd,False,juego,None,None,su)
		if(self.raiz==None):
			self.raiz=nuevo
			return "V"
		else:
			temporal=self.raiz
			while temporal!=None :
				print temporal.usuario
				if temporal.usuario>usuario:
					if temporal.izq==None:
						temporal.izq=nuevo
						return "V"
					temporal=temporal.izq
				elif temporal.usuario<usuario:
					if temporal.der==None:
						temporal.der=nuevo
						return "V"
					temporal=temporal.der
				elif temporal.usuario==usuario:
					return "F"
			temporal=nuevo
		return "F"
	def eliminar(self,usuario):
		temporal=self.raiz	
		if self.raiz==None :
			return "F"
		else:
			# si es la raiz
			if temporal.usuario==usuario:
				if temporal.izq==None and temporal.der==None:
					self.raiz=None
					return "V"
				elif temporal.izq==None and temporal.der!=None:
					self.raiz=self.raiz.der
					return "V"
				elif temporal.izq!=None and temporal.der==None:
					self.raiz=self.raiz.izq
					return "V"
				else:
					temporal=self.raiz.izq
					self.raiz=self.raiz.der
					tmp=self.raiz
					while tmp.izq!=None:
						tmp=tmp.izq
					tmp.izq=temporal
					return "V"
			# si no es la raiz
			else:
				previo = temporal
				if temporal.usuario<usuario:
					if temporal.der==None:
						return "F"
					temporal=temporal.der
				elif temporal.usuario>usuario:
					if temporal.izq==None:
						return "F"
					temporal=temporal.izq
				while temporal!=None:
					if temporal.usuario<usuario:
						if temporal.der==None:
							return "F"
						previo=temporal
						temporal=temporal.der
					elif temporal.usuario>usuario:
						if temporal.izq==None:
							return "F"
						previo=temporal
						temporal=temporal.izq
					else:
						if previo.izq==temporal:
							if temporal.izq==None and temporal.der==None:
								previo.izq=None
								return "V"
							elif temporal.izq==None and temporal.der!=None:
								previo.izq==temporal.der
								return "V"
							elif temporal.izq!=None and temporal.der==None:
								previo.izq==temporal.izq
								return "V"
							else:
								t2=temporal.izq
								previo.izq=temporal.der
								while previo.izq!=None:
									previo=previo.izq
								previo.izq=t2
								return "V"
						else:
							if temporal.izq==None and temporal.der==None:
								previo.der=None
								return "V"
							elif temporal.izq==None and temporal.der!=None:
								previo.der==temporal.der
								return "V"
							elif temporal.izq!=None and temporal.der==None:
								previo.der==temporal.izq
								return "V"
							else:
								t2=temporal.izq
								previo.der=temporal.der
								while previo.izq!=None:
									previo=previo.izq
								previo.izq=t2
								return "V"


				return "F"

	def modificar(self,usuario):
		temporal=self.raiz
		while temporal.usuario!=None:
			if temporal.usuario==usuario:
				tmp=temporal
				eliminar(usuario)
				agregar(usuario,tmp.passwd,tmp.juego,tmp.su)
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
		temporal=self.raiz
		self.cadena=""
		return preden(tmp)

	def preorden(tmp):
		print "tambien aca"
		if(tmp.izq!=None):
			self.cadena=self.cadena+tmp.usuario+"->"+preorden(tmp.izq)+";\n"
		if(tmp.der!=None):	
			self.cadena=self.cadena+tmp.usuario+"->"+preorden(tmp.der)+";\n"
		return tmp.usuario














