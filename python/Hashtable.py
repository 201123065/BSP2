from NodoHT import NodoHT
class Hashtable():
	def __init__(self):
		# tabla ht
		self.tabla=None
		# casillas ocupadas
		self.ocupadas=0
		# tamaño
		self.tam=0

	# ESTE METODO ES PARA CREAR EL HT
	def crearHT(self):
		# crear desde cero la HT
		# si no existe la tabla
		if self.tabla==None:
			tam=0
			tmp=None
			# tabla inicial es de 47
			while tam<47:
				# si el valor es 0, asigna la nueva tabla
				if tam==0:
					self.tabla=NodoHT(None,None)
					# tambien asigna el valor a temporal
					tmp=self.tabla
				else:
					# asigna el nuevo nodo al siguiente del temporal
					tmp.siguiente = NodoHT(None,None)
					# se desplaza temporal a la siguiente posicion
					# o sea: una lista
					tmp=tmp.siguiente
				# aumenta para salir del bucle
				tam=tam+1
			return "v"
		# SI ya existe una ht, 
		else:
			 # para que se mantenga la proporcion al 30% si se excede
			casilla=self.ocupadas/0.3
			# if por seguridad nada mas, no se si sirva, pero pela
			if(casilla>self.tam):
			# redondeo por si viene con decimales(casi seguro)
				self.tam=int(round(casilla))

			casilla=0
			temporal=self.tabla
			
			#ciclo para asignar 
			while casilla<self.tam:
				# este if es para darle copy paste
				# al nodo anterior
				if temporal.siguiente==None:
					# aca el copy-paste
					temporal.siguiente=NodoHT(None,None)
				# se desplaza el temporal al siguiente
				temporal=temporal.siguiente
				# suma la casilla para romper el while
				casilla=casilla+1
			# se concluye la creacion del ht
			return "v"
	#METODO para cargar el usuario
	def cargarUsuario(self,usuario):
		valor=0
		val_ascii=""
		# se convierte la cadena en valor ascii
		while valor<len(usuario):
			val_ascii=val_ascii+ord(usuario[valor])

		# se convierte lo obtenido en entero
		op=float(val_ascii)
		# se eleva al cuadrado(metodo propuesto)
		op=op*op
		val_ascii=str(op)
		id_n=len(val_ascii)
		if id_n%2==0:
			# quiere decir que es par
			val_ascii=val_ascii[id_n]+val_ascii[id_n+1]
		else:
			# quiere decir que es impar
			val_ascii=val_ascii[id_n-1]+val_ascii[id_n]

		#obtiene el valor temporal 
		tmp=self.tabla

		# si es menor el indice al de la ht, quiere decir que puede caber en el array
		if self.tam>int(val_ascii):
			# envia a metodo asignaIndex
			return self.asignarIndex(int(val_ascii),usuario)
		# quiere decir que el indice es mayor al de la ht,
		else:
			# primero, agrega una casilla al tam, para la redimension
			self.tam=int(val_ascii)+1
			# luego trazas nuevamente tu HT
			self.crearHT()
			# y ya despues, podes asignar el indice
			return self.asignarIndex(int(val_ascii),usuario)

	def asignarIndex(self,valor,usuario):
		i=0
		tmp=self.tabla
		# busca la casilla donde queres insertarlo
		while i<valor:
			tmp=tmp.siguiente
			i=i+1
		# si esta vacia la casilla, lo ingresas aca
		if tmp.usuario==None:
			tmp.usuario=usuario
			return "v"
		# si esta ocupada, y es por el mismo usuario, retornas falso
		# o en mi caso una f, eso no importa la verdad
		elif tmp.usuario==usuario:
			return "f"
		else:
			#colision
			# mientras existan nodos siguientes
			while tmp.siguiente!=None:
				# si el sigiente nodo de tmp esta vacio, lo asignas aca
				if tmp.siguiente.usuario==None:
					tmp.siguiente.usuario=usuario:
					# y rompes el ciclo con el return
					return "v"
				# si el siguiente esta ocupado por vos mismo
				# rompes con return f
				elif tmp.siguiente.usuario==usuario:
					return "f"
				else:
					# el siguiente no esta ocupado
					# y existe, entonces tmp ahora sera el siguiente de tmp
					tmp=tmp.siguiente
			# si llego hasta aca quiere decir que se te acabaron los indices
			# a volver a hacer la ht
			# le sumas 1 al tamaño
			self.tam=self.tam+1
			# añadis el siguiente de tmp con el usuario de una vez
			tmp.siguiente=NodoHT(usuario,None)
			# y decis que ocupaste una casilla mas
			self.ocupadas=self.ocupadas+1
			# fin :v
			return "v"















