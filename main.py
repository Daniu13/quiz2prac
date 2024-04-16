import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io as sio

class Archivador:
    def __init__(self) -> None:
        self.__mat = dict()
        self.__csv = dict()

    def ver_mat(self):
        return self.__mat
    
    def ver_csv(self):
        return self.__csv

    def ingresar_mat(self, archivo, clave):
        data = sio.loadmat(archivo)
        self.__mat[clave] = data["data"]

    def ingresar_csv(self, archivo, clave):
        data = pd.read_csv(archivo)
        self.__csv[clave] = data

    def ingresar_gral(self, archivo, clave):
        if archivo.endswith(".mat"):
            self.ingresar_mat(archivo, clave)
        elif archivo.endswith(".csv"):
            self.ingresar_csv(archivo, clave)
    
    def mostrar_columnas(self, clave):
        if clave in self.__csv:
            return list(self.__csv[clave].columns)
        else:
            return "La clave no corresponde a un archivo CSV."

    def scatter_columna(self, clave, nombre_columna):
        if clave in self.__csv:
            data = self.__csv[clave]
            if nombre_columna in data.columns and pd.api.types.is_numeric_dtype(data[nombre_columna]):
                plt.scatter(data.index, data[nombre_columna])
                plt.xlabel('Índice')
                plt.ylabel(nombre_columna)
                plt.title(f'Scatter Plot de la columna {nombre_columna}')
                plt.show()
            else:
                print(f"La columna '{nombre_columna}' no es numérica o no existe en el archivo CSV.")
        else:
            print("La clave no corresponde a un archivo CSV.")

class Graficador:
    def __init__(self, form=[2,3]) -> None:
        self.__fig = plt.figure()
        self.__form = form
        self.__axes = self.__fig.subplots(self.__form[0], self.__form[1])

    def graf_scatter(self, data, canal, posicion): #canal, posicion son int, tiempo es array
        axis = self.__axes.flat[posicion]
        tiempo = np.arange(348000)
        data = data.reshape(data.shape[0],-1)
        axis.scatter(tiempo, data[canal,:])
        
    def graf_sum(self, data, segmento, posicion): #Segmento es iterable, segmento[1] es inclusivo
        axis = self.__axes.flat[posicion]
        tiempo = np.arange(segmento[0], segmento[1]+1)
        data = data.reshape(data.shape[0],-1)
        suma = np.sum(data[:,segmento[0]:segmento[1]+1], axis=0)
        axis.plot(tiempo, suma)

    def graf_ruido(self, data, canal, posicion):
        axis = self.__axes.flat[posicion]
        #tiempo = np.arange(348000)
        tiempo = np.linspace(0, 2, 348000)
        #tiempo_segundos = np.arange(0, len(data[0]) / 500, 1 / 500) #frecuencia de muestreo es 500, osea 1000/2, en prereshape
        data = data.reshape(data.shape[0],-1)
        ruido = np.random.randint(31, size=348000)
        data_ruido = data+ruido
        axis.plot(tiempo, data_ruido[canal,:])

archiver = Archivador()
archiver.ingresar_gral("P005_EP_reposo.mat",1111)
print(archiver.ver_mat())
datos = archiver.ver_mat()[1111]
print(np.shape(datos))
grafiquer = Graficador(form=[2,3])
grafiquer.graf_ruido(datos, 0, posicion=4)
grafiquer.graf_scatter(datos, 0, posicion=2)
grafiquer.graf_sum(datos, segmento=[400,600], posicion=3)

plt.subplots_adjust(wspace=0.4, hspace=0.3)
plt.show()




# def cargar(archivo):
#     if archivo.endswith(".mat"):
#         data = sio.loadmat(archivo)
#     elif archivo.endswith(".csv"):
#         data = pd.read_csv(archivo)
#     return data

# datos = cargar("P005_EP_reposo.mat")
# #datos = cargar("S0539.mat")
# print(type(datos))
# #print(datos)
# print(sio.whosmat("P005_EP_reposo.mat"))
# print(datos["data"])
# print(np.shape(datos["data"]))
#Data es un array (8,2000,174)

def main():
    archiver = Archivador()
    grafiquer = Graficador(form=[2,3])
    while True:
        menu = int(input("""Opciones:
                         \n1. Ingresar MAT
                         \n2. Ingresar CSV
                         \n3. Graficar señal
                         \n4. Mostrar información
                         \n5. Salir"""))
        if menu == 1:
            archivo = input("Nonmbre del archivo: ") #P005_EP_reposo.mat
            clave = int(input("Clave(Integer): ")) #1111
            archiver.ingresar_gral(archivo, clave)
            datos = archiver.ver_mat()[clave]
        elif menu == 2:
            archivo = input("Nonmbre del archivo: ") #
            clave = int(input("Clave(Integer): ")) #
            archiver.ingresar_gral(archivo, clave)
            datos = archiver.ver_csv()[clave]
        elif menu == 3:
            grafiquer.graf_ruido(datos, 0, posicion=4)
            grafiquer.graf_scatter(datos, 0, posicion=2)
            grafiquer.graf_sum(datos, segmento=[400,600], posicion=3)

            plt.subplots_adjust(wspace=0.4, hspace=0.3)
            plt.show()
        elif menu == 4:
            pass
        elif menu == 5:
            break
        else:
            print("Valor no válido")

#if __name__ == '__main__':
#    main()