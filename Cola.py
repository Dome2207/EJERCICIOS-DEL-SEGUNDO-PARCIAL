class Cola:
    def __init__(self):
        self.items=[]
        
    #AÑADE ELEMENTOS A LA COLA POR LA IZQUIERDA
    def encolar(self,x): 
        self.items.append(x)
        
    #MUESTRA COLA
    def mostrar_cola(self):
        print(self.items)
        
    #DEVUELVE ELEMENTO DE LA COLA POR LA DERECHA
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    #VERIFICA SI LA COLA ESTA VACIA
    def es_vacia(self):
            return self.items == []    

q = Cola()
q.es_vacia()  
True
q.mostrar_cola()
print("AÑADIR ELEMENTOS.")
q.encolar(1)
q.encolar(2)
q.encolar(5)
q.es_vacia()
False
q.mostrar_cola()
print("EXTRAEMOS ELEMENTO.")
q.desencolar()
q.desencolar()
q.mostrar_cola()
print("AÑADIMOS NUEVO ELEMENTO.")
q.encolar(8)
q.mostrar_cola()
print("EXTRAEMOS ELEMENTOS.")
q.desencolar()     
q.desencolar()
q.es_vacia()
q.mostrar_cola()
q.desencolar()
    