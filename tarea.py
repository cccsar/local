#Operaciones de lista:
#List insert
#List delete
#Atributos de lista: 
#prev,next,key,
#head 

#Para implementacion con 3 arreglos:
#Allocate object
#free object

class List:
	def __init__(self,nelements ): 
		# |prev,nex,key|=nelements+1 para dejar a un NaN centinela en self.next[0] que refiera al ultimo de la lista.
		self.prev=(nelements+1)*[0]
		self.next=(nelements+1)*[0]
		for i in range(1,nelements+2): self.next[i]=i-1 
		#inicializa a next como lista en donde cada elemento a partir de self.next[1] apunta a su predecesor.
		self.next[0]=NaN 
		self.key=(nelements+1)*[0]

		self.head=NaN #deberia ser x tal que x.prev=NaN
		self.free=self.next[nelements+1] #valor inicial de free, puede no funcionar por ser originalmente variable global.
		

#Como los x referenciaran indices de un arreglo, verificar que no excendan n-1.

	def list_insert(self,x):
		#Verificar que la lista no este llena
		self.next[x]=self.head
		if self.head!=NaN:
			prev[self.head]=x
		self.head=x
		self.prev[x]=NaN
	
	def list_delete(self,x): 
		#revisar bien orden de composicion.
		if self.prev[x]!=NaN:
			self.next[self.prev[x]]=self.next[x] 
		else:	
			self.head=self.next[x]

		if self.next[x]!=NaN: 
			self.prev[self.next[x]]=self		

	def allocate_object(self): 
		if free==NaN:
			print('Error!, sin espacio') 
		else: 
			x=self.free
			self.free=self.next[x]		
		return x

	def free_object(self,x): 
		self.next[x]=self.free
		self.free=x

#Dudas: 
#Las listas deberian poder definirse una vez son creadas??
#Si el argumento de list es un apuntador, en que momento se define su self.key[x]??

#consideraciones: 
#Para aniadir: list_insert(allocate_object()) aniadira el proximo elemento en la posicion indicada por el orden 
#de los elementos en next (que debe definirse en el constructor??) 

#Para eliminar: list_delete(x) ; free_object(x) una vez eliminado un elemento de la lista, se coloca el apuntador indicado
#como 'free' <- esto quiere decir que el proximo elemento a aniadir se colocara sobre ese apuntador

#Tanto el uso de list insert como la liberacion de espacio en free_object(x) nos dicen que HAY UN ORDEN DE COLOCACION PREDEFINIDO.
