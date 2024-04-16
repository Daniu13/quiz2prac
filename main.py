import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io as sio

class Archivador:
    def __init__(self) -> None:
        self.__mat = dict()
        self.__csv = dict()

    def ingresar_mat(self, archivo, clave):
        data = sio.loadmat(archivo)
        self.__mat[clave] = data

    def ingresar_csv(self, archivo, clave):
        data = pd.read_csv(archivo)
        self.__csv[clave] = data

    def ingresar_gral(self, archivo, clave):
        if archivo.endswith(".mat"):
            self.ingresar_mat(archivo, clave)
        elif archivo.endswith(".csv"):
            self.ingresar_csv(archivo, clave)


def cargar(archivo):
    if archivo.endswith(".mat"):
        data = sio.loadmat(archivo)
    elif archivo.endswith(".csv"):
        data = pd.read_csv(archivo)
    return data

datos = cargar("S0539.mat")
print(type(datos))
print(datos)

def main():
    while True:
        menu = int(input("""Opciones:
                         \n1. Ingresar MAT
                         \n2. Ingresar CSV
                         \n3. Graficar señal
                         \n4. Mostrar información
                         \n5. Salir"""))

#if __name__ == '__main__':
#    main()