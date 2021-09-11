class Lista:
    def __init__(self,listas):
        self.__lista=listas
    
    @property
    def lista(self):  # getproperty
        # if self.__lista != None:
        return self.__lista
        # else: print("Ingrese la lista")
    
#busca un valor en la lista; retorna la posicion si lo encuentra y sino lo encuentra retorna -1    
    def busquedaLineal(self,buscado):
        # print("Busqueda Lineal",buscado)
        pos=0
        enc=False
        # Recorre la lista hasta que la posicio sea igual a la longitud o enc sea verdadero 
        while pos < len(self.__lista) and enc==False :
            if self.__lista[pos]["nombre"] == buscado:
                # asigna true a enc 
                enc=True
            else:
                pos = pos +1
                
        if enc: return pos
        else: return -1                
    
    def quicksort(self):
        pass
        
    def ordenar(self,orden):
        orden = orden.lower()
        if orden == "asc": 
           for pos in range(0,len(self.__lista)):
               for sig in range(pos+1,len(self.__lista)):
                  if self.__lista[pos]["nombre"] > self.__lista[sig]["nombre"]:
                    aux = self.__lista[pos]
                    self.__lista[pos]=self.lista[sig]
                    self.__lista[sig]=aux
        else:   
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                  if self.__lista[pos]["nombre"] < self.__lista[sig]["nombre"]:
                    aux = self.__lista[pos]
                    self.__lista[pos]=self.lista[sig]
                    self.__lista[sig]=aux         
                    
    
    def busquedaBinaria(self, buscado):
        self.ordenar("asc")
        fin = len(self.lista)-1 
        inicio = 0
        enc = False
        while inicio <= fin and enc == False:
            medio = (inicio+fin)//2
            if self.lista[medio]["nombre"] == buscado: enc= True
            elif self.lista[medio]["nombre"] < buscado: inicio = medio+1
            else: fin = medio-1
        if enc: return medio 
        else: return -1    

notas=[{"nombre":"Danny","n1":20,"n2":40},
       {"nombre":"Daniel","n1":30,"n2":50},
       {"nombre":"Dayana","n1":40,"n2":50},
       {"nombre":"Erick","n1":50,"n2":40},
       {"nombre":"Romina","n1":55,"n2":40},
       {"nombre":"Yady","n1":60,"n2":40}
]

bus = Lista(notas)
# bus.lista=[3,5]
print(bus.lista) 
posicion = bus.busquedaBinaria("moises") 
if posicion != -1:
    # print(bus.lista[3])
    print(bus.lista[posicion])  
else:
    print("Nombre no se encuentra en la lista")  
# bus.ordenar("asc")    
# print(bus.lista)
