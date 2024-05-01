import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

class Archivador:
    def __init__(self) -> None:
        self.__mat = dict()
        self.__csv = dict()

    def ver_mat(self, clave):
        return self.__mat[clave]
    
    def ver_csv(self):
        return self.__csv

    def ingresar_mat(self, archivo):
        data = sio.loadmat(archivo)
        self.__mat[sio.whosmat(archivo)[0][0]] = data[sio.whosmat(archivo)[0][0]]

    def ingresar_csv(self, archivo, clave):
        data = pd.read_csv(archivo)
        self.__csv[clave] = data
        

    def ingresar_gral(self, archivo, clave):
        if archivo.endswith(".mat"):
            self.ingresar_mat(archivo)
        elif archivo.endswith(".csv"):
            self.ingresar_csv(archivo, clave)
    
    def mostrar_columnas(self, clave):
        if clave in self.__csv:
            return list(self.__csv[clave].columns)
        else:
            fehler = "Error, clave no válida."
            return fehler

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
                print(f"Columna no válida.")
        else:
            print("Error, clave no válida.")

    def sum_columna(self, clave, columnas):
        if clave in self.__csv:
            data = self.__csv[clave]
            suma_columnas = data[columnas].sum(axis=1)
            data['Suma_Columnas'] = suma_columnas
            media = suma_columnas.mean()
            moda = suma_columnas.mode().iloc[0]
            desviacion_estandar = suma_columnas.std()
            return media, moda, desviacion_estandar
    
    def info_zeigen(self, clave):
        if clave in self.__csv:
            data = self.__csv[clave]
            print("a) Nombre de todas las columnas:")
            print(data.columns.tolist())
            nombre_columna = input("b) Ingrese el nombre de una columna numérica para hacer un scatter: ")
            self.scatter_columna(clave, nombre_columna)
            columnas_suma = [input(f"Ingrese el nombre de la columna {i+1}: ") for i in range(4)]
            media, moda, desviacion_estandar = self.sum_columna(clave, columnas_suma)
            if media is not None:
                print(f"Media: {media}")
                print(f"Moda: {moda}")
                print(f"Std: {desviacion_estandar}")
            else:
                print("Error al crear la nueva columna.")
        else:
            print("Error, clave no válida.")

class Graficador:
    def __init__(self, form=[2,3]) -> None:
        self.__fig = plt.figure()
        self.__form = form
        self.__axes = self.__fig.subplots(self.__form[0], self.__form[1])

    def graf_scatter(self, data, canal, posicion): #canal, posicion son int, tiempo es array
        axis = self.__axes.flat[posicion]
        if np.ndim(data) == 3:
            tiempo = np.linspace(0, 2, data.shape[1]*data.shape[2])
        elif np.ndim(data) == 2:
            tiempo = np.linspace(0, 2, data.shape[1])
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
        if np.ndim(data) == 3:
            tiempo = np.linspace(0, 2, data.shape[1]*data.shape[2])
        elif np.ndim(data) == 2:
            tiempo = np.linspace(0, 2, data.shape[1])
        data = data.reshape(data.shape[0],-1)
        ruido = np.random.randint(31, size=data.shape[1])
        data_ruido = data+ruido
        axis.plot(tiempo, data_ruido[canal,:])
        #tiempo = np.linspace(0, 2, len(data[canal, :]))
        #tiempo_segundos = np.arange(0, len(data[0]) / 500, 1 / 500) #frecuencia de muestreo es 500, osea 1000/2, en prereshape

#archiver = Archivador()
#archiver.ingresar_gral("P005_EP_reposo.mat", 'data')

print(sio.whosmat("P005_EP_reposo.mat"))
print(sio.whosmat("S0539.mat"))
#print(type(archiver.ver_mat(clave='data')))

#datos = archiver.ver_mat(clave='data')