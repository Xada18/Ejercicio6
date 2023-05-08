from ClaseManejadorViajeros import ManejadorViajeros

if __name__ == '__main__':
    archivo = "viajeros.csv"
    ListaViajeros = ManejadorViajeros()
    ListaViajeros.carga(archivo)

    print("Informacion del viajero con mayor cantidad de millas acumuladas: ")
    print(f"{ListaViajeros.mayorCantidadMillas()}")
    print("")

    viajero = ListaViajeros.buscarViajero(input("Ingrese un numero de viajero: "))
    if viajero == None:
        print("No se encontro el viajero")
    else:
        cantidad = input("Ingrese cantidad de millas recorridas: ")
        viajero = viajero + int(cantidad)
        print(viajero)
    print("")
        

    otroViajero = ListaViajeros.buscarViajero(input("Ingrese un numero de viajero: "))
    if otroViajero == None:
        print("No se encontro el viajero")
    else:
        cantidad = input("Ingrese cantidad de millas a canjear: ")
        otroViajero = otroViajero - int(cantidad)
        print(otroViajero)
    print("")

