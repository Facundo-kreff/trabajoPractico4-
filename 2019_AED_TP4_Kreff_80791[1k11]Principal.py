#2019_AED_TP4_Kreff_80791[1k11]

import Registro


#Opcion 1
def opcion_1(v, arch):
    #Busqueda
    codig = int(input("Ingrese el N° De Codigo Del Articulo Que Decea Comprar: "))
    indice = None
    for i in range(len(v)):
        if v[i].codigo == codig:
            indice = i
    if indice == None:
        print("Producto No Encontrado")
        return
    else:
        Registro.compra(v, indice, arch)


#Opcion 2
def opcion_2(v):
    print()

#opcion 3

def mostrar_rango(v, menor, mayor):
    #Generar una nuevo vector para almacenar los datos entre el rango de precios
    recolector = []
    #recorer registro para sacar articulos que cumplan
    for i in range(len(v)):
        if v[i].precio <= mayor and v[i].precio >= menor:
            recolector.append(v[i])
    #mostrar Nuevo registro con valores pedidos
    print("\nArticulos en el Rango de Precios que se Desea Gastar:")
    Registro.mostrar(recolector)


def opcion_3(v):
    #Ordenammos registro por precio de menor a mayr
    for i in range(len(v) - 1):
        for j in range(i+1, len(v)):
            if v[i].precio > v[j].precio:
                v[i], v[j] = v[j], v[i]
    mayor, menor = [v[len(v)-1]], [v[0]]
    topemenor, topemayor = v[0].precio, v[len(v)-1].precio
    #informar los resultados minimo y maximo
    print("\nMayor precio encontrado en la búsqueda: $", topemayor)
    Registro.mostrar(mayor)
    print("\nMenor precio encontrado en la búsqueda: $", topemenor)
    Registro.mostrar(menor)
    #Definicion de valores del rango para mostrar publicaciones
    cambio = 0
    while cambio != 1 and cambio !=2:
        cambio = int(input("\nDesea Ajustar El Minimo y Maximo Que Desea Gastar(1-Si 2-No): "))
        if cambio != 1 and cambio !=2:
            print("Opcion no valida")
    #Cambio de topes
    if cambio == 1:
        #Ingreso de nuevos valores
        nuev_val_min, nuev_val_max  = None, None
        while nuev_val_max != topemayor and nuev_val_min != topemenor:
            nuev_val_min = int(input("Ingrese Monto Minimo que Desea Gastar: "))
            nuev_val_max = int(input("Ingrese Monto Maximo que Desea Gastar: "))
            if nuev_val_max <= topemayor and nuev_val_min >= topemenor:
                topemayor, topemenor  = nuev_val_max, nuev_val_min
            else:
                print("Supera topes mínimo y/o máximo de los valores encontrados")
    mostrar_rango(v, topemenor, topemayor)










#opcion 4
def opcion_4(v, favoritos):
    Registro.op_4(v, favoritos)

#opcion 5
def opcion_5(v):
    print()

#opcion 6
def menor_precio(v):
    print()



#Funcion Principal

def test():
    print("\033[4;30m"+"MERCADO LIBRE"+'\033[0;m')
    #Ingreso de Nombre del articulo
    art=input("Ingrese el Nombre Del Articulo Que Decea Buscar: ")
    n = 0
    #Ciclo para inpedir que se ponga cero resultados o numeros negativos
    while n <= 0:
        n =int(input("Ingrese la Cantida De Resultados Que Quiere: "))
        if n <= 0:
            print("No se puede poner 0(cero) resultados")
    vec = [None] * n
    archivo1 = "miscompras.dat"
    archivo2 = "favoritos.dat."
    #carga de los datos
    Registro.carga(vec,art)
    #ondenamiento registro
    Registro.ordenar(vec)
    #muestra de registro
    Registro.mostrar (vec)
    op = 0
    #Menu de opciones
    while op != 6:
        print("\nOpciones:")
        print ("1-Comprar.")
        print ("2-Mis compras.")
        print ("3-Rango de precios.")
        print ("4-Agregar favorito.")
        print ("5-Actualizar Favoritos.")
        print ("6-Salir")
        op=int(input("\nIngrese Numero De Opcion: "))
        print()

        if op == 1:
            opcion_1(vec, archivo1)
        elif op == 2:
            opcion_2(vec)
        elif op == 3:
            opcion_3(vec)
        elif op == 4:
            opcion_4(vec, archivo1)
        elif op == 5:
            opcion_5(vec)
        elif op == 6:
            print('-------Fin del programa-------')
            print ("\n    Que Tenga Buen Dia ;)")



test()
