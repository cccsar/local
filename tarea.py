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

	def __init__(self,nelements): 
		#atributos de lista:
		self.prev=nelements*[0]
		for i in range(nelements-1,0,-1): self.prev[i]=i-1 #apuntadores del prev de F iniciados
		self.prev[0]=None

		self.next=nelements*[0]
		for j in range(0,nelements-1): self.next[j]=j+1 #apuntadores del next de F iniciados
		self.next[nelements-1]=None 

		self.key=nelements*[None] #La lista esta vacia
		self.head=None
		self.free=0
		

	#Operaciones de lista: 

	def list_insert(self,value):
		x=self.allocate_object() 

		self.next[x]=self.head
		if self.head!=None:
			self.prev[self.head]=x
		self.head=x
		self.prev[x]=None

		self.key[x]=value
	
	def list_delete(self,x): 
		if self.prev[x]!=None:
			self.next[self.prev[x]]=self.next[x] 
		else:	
			self.head=self.next[x]

		if self.next[x]!=None: 
			self.prev[self.next[x]]=self.prev[x]
		
		self.free_object(x) #Se anade a la lista F el elemento eliminado
				
	#Operaciones de la lista free:

	def allocate_object(self): 
		if self.free==None:
			return "No hay espacio disponible"
		else: 
			x=self.free
			self.free=self.next[x]		
			if self.free!=None:
				self.prev[self.free]=None #reacomodamiento - puede haber un error aqui
		return x

	def free_object(self,x): 
		self.next[x]=self.free
		self.prev[x]=None
		if self.next[x]!=None:
			self.prev[self.next[x]]=x #reacomodamiento
		self.free=x
		self.key[x]=None

#arreglar esta vaina:
	def list_swap(self,x,y): 
		"""
		if x==y+1:
			self.prev[y]=self.prev[x]
			self.next[x]=self.next[y]
			self.next[y]=x
			self.next[x]=y
		elif y==x+1:
			self.prev[x]=self.prev[y]
			self.next[y]=self.next[x]
			self.next[x]=y
			self.next[y]=x
		else:
		"""
		if self.next[x]!=None: self.prev[self.next[x]]=y
		if self.prev[y]!=None: self.next[self.prev[y]]=x
		if self.prev[x]!=None: self.next[self.prev[x]]=y
		if self.next[y]!=None: self.prev[self.next[y]]=x
		
		self.key[x],self.key[y]=self.key[y],self.key[x]

	def compactify_list(self): 
		if self.head==None or self.free==None: 
			return "Nada que organizar"		
		else:
			print('va a organizar algo') 
			i,j=0,len(self.key)-1
			while i<j:
				print('entro en el while')
				if str(self.key[i])!='None':
					print('entro al primero')
					i+=1
				
				if str(self.key[j])=='None':
					print('entro al segundo')
					j-=1

				if str(self.key[i])=='None' and str(self.key[j])!='None':
					print('entro en el if importante')
					self.list_swap(i,j)
					i,j=i+1,j-1
	#printing

	def __str__(self): 

		if self.head==None or self.free==None:
			return "List: \n next=%s \n key=%s \n prev=%s \n head=%s, free=%s " % (str(self.next),str(self.key),str(self.prev),str(self.head),str(self.free))
		else:
			return "List: \n next=%s \n key=%s \n prev=%s \n head=%d, free=%d " % (str(self.next),str(self.key),str(self.prev),self.head,self.free)

	__repr__=__str__

#Pruebas:
a=List(5)
print('lista inicializada')
print(a)
a.list_insert(55)
a.list_insert(3)
a.list_insert(5)
a.list_insert(7)
a.list_insert(8)
print('lista con anadidos')
print(a)
a.list_delete(0)
print('lista con el ultimo elemento eliminado') 
print(a)
a.list_delete(2)
print('lista con un elemento distinto al primero eliminado') 
print(a)
a.compactify_list()
print('lista compacta') 
print(a)

"""
print('Pruebas malandrosas')
n=int(input('INgrese el tamanio de la lista de prueba: '))
b=list(n)
for x in range(n): 
	
"""
