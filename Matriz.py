import os
class Matriz:
    def __init__(self,matriz,fila,col):
        self.matriz = matriz 
        self.fila=fila 
        self.col = col 
    
    def ingresar(self):
        self.matriz = []
        for fila in range(self.fila):
            columnas=[]
            os.system("cls")
            for col in range(self.col):
                valor = int(input("Fila[{}] Col[{}]: ".format(fila,col)))
                columnas.append(valor)
            self.matriz.append(columnas)    
    
    # def presentar(self):
    #     for fila in range (len(numeros)):
    #         columna = numeros[fila]
    #         for col in range(len(columna)):
    #             # print(columna[col],end=" ")
    #             # print(numeros[fila][col],end=" ")
    #             print(columna[col],end=" ")
    #             print() 
         
    def presentar(self):    
        # os.system("cls")  
        print("____________")    
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end=" ")
            print()
        print("____________")
        
    def buscar(self,valor):
         enc = {}
         for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col] == valor:
                    enc["fila"]= fila
                    enc["col"]=col
                    break
            if enc: break 
         return enc       
     
    def buscarW(self,valor):
         enc = {}
         fila=0
         band=True
         while fila < len(self.matriz)and band:
            col=0
            while col < len(self.matriz[fila]) and band: 
                if self.matriz[fila][col] == valor:
                    enc["fila"]= fila
                    enc["col"]=col
                    band=False 
                else: col += 1
            fila += 1
         return enc  
    
    def sumar(self,matriz2):
        matrizSuma = []
        for fila in range(self.fila):
            columnas=[]
            for col in range(self.col):
                valor = self.matriz[fila][col] + matriz2[fila][col]
                columnas.append(valor)
            matrizSuma.append(columnas)  
        # self.matriz = matrizSuma 
        return matrizSuma  
         

numeros = []
# numeros = [[22,44,55],[10,20,30],[15,10,15]]                
# numeros = [[10,20,30],[60,80,40],[25,35,55]] 
mat1 = Matriz(numeros,2,2)
mat2 = Matriz([],2,2) 
mat1.ingresar()
mat2.ingresar()
mat1.presentar()
mat2.presentar()
x = mat1.sumar(mat2.matriz)
mat1.matriz = mat1.sumar(mat2.matriz)
mat2.matriz = mat1.sumar(mat2.matriz)
mat1.presentar()
# mat.ingresar()
# print(mat.buscar(8))
# mat.presentar()  
# resp = mat.buscarW(20) 
# if resp: print("El valor se encuentra en las siguientes coordenadas",resp)
# else: print("No existe el valor en la matriz")                    