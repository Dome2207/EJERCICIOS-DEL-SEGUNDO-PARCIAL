class Texto:
    def __init__(self,nombreArchivo):
        self.archivo = nombreArchivo
    
    def leer(self):
         with open(self.archivo, 'r', encoding="UTF-8") as file:
            for linea in file:
                print(linea[:-1])

    def escribir(self,datos,modo):
        # nombres = ['Fernanda', 'Lola', 'Esperanza', 'Esther', 'Lucas']
        with open(self.archivo, modo, encoding="UTF-8") as file:
            for dato in datos:
                file.write(dato+"\n")
                # estudiantes.write('\n')

arch1 = Texto("estudiantes.txt")
arch1.escribir(["Marcos Vera","Doménica Pineda", "Yady Bohórquez", "Erick Vera","Miguel Vera"],"a")
arch1.leer()