"""Daniel Lozano Simanca"""

from clases import *
import os


def main():
    archiver = Archivador()
    while True:
        menu = int(
            input(
                """Opciones:
                         \n1. Ingresar MAT
                         \n2. Ingresar CSV
                         \n3. Graficar señal
                         \n4. Mostrar información
                         \n5. Salir
                         \n"""
            )
        )
        if menu == 1:
            archivo = input("Nonmbre del archivo: ")
            if os.path.isfile(archivo):
                clave = input("Clave: ")
                archiver.ingresar_gral(archivo, clave)
                datos = archiver.ver_mat(clave)
            else:
                print("Archivo no existente.")
        elif menu == 2:
            archivo = input("Nonmbre del archivo: ")  #
            if os.path.isfile(archivo):
                clave = input("Clave: ")
                archiver.ingresar_gral(archivo, clave)
                datos = archiver.ver_csv()[clave]
            else:
                print("Archivo no existente.")
        elif menu == 3:
            grafiquer = Graficador(form=[2, 3])
            grafiquer.graf_ruido(datos, 0, posicion=4)
            grafiquer.graf_scatter(datos, 0, posicion=2)
            grafiquer.graf_sum(datos, segmento=[400, 600], posicion=3)

            plt.subplots_adjust(wspace=0.4, hspace=0.3)
            plt.show()
        elif menu == 4:
            clave = input(
                "Ingrese la clave del archivo CSV del que desea mostrar información: "
            )
            archiver.info_zeigen(clave)
        elif menu == 5:
            break
        else:
            print("Valor no válido")


if __name__ == "__main__":
    main()
