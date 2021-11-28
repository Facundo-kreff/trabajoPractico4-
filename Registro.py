#2019_AED_TP4_Kreff_80791[1k11]
#Registros

import time
import pickle
import os.path
import random

#Creacion De Registro Articulo

class Articulo():
    def __init__(self, busq, cod, precio, ubic, estad, cant, punt):
        self.producto = busq
        self.codigo = cod
        self.precio = precio
        self.ubicacion = ubic
        self.estado =  estad
        self.cantidad = cant
        self.puntuacion = punt

#Creacion De Registro Compras
class Compras():
    def __init__(self, codig, canti, costo, envio, total_pag, fecha, totalfin):
        self.codig = codig
        self.cantidad = canti
        self.costo = costo
        self.envio = envio
        self.pagar = total_pag
        self.fecha = fecha
        self.toral_con_envio = totalfin


#Funcion De Carga De Datos En Registro Articulos
def carga(v, art):
    for i in range(len(v)):
        cod = random.randint(00000,99999)
        precio = float(random.randint(100,10000))
        ubi= random.choice(("Buenos Aires","Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos"
                                        , "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén"
                                        , "Río Negro", "Salta", "San Juan", "San Luis", "Santa Cruz", "Santa Fe"
                                        , "Santiago del Estero", "Tierra del Fuego", "Tucumán"))
        estad = random.choice(("Nuevo","Usado"))
        cant = random.randint(1,500)
        punt = random.choice(("1- Mala", "2- Normal", "3- Buena","4- Muy Buena", "5- Exelente"))
        v[i] = Articulo(art, cod, precio, ubi, estad, cant, punt)

#Funcion para ordenar el arreglo de registro Articulos
def ordenar(v):
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

#Funcion Para mostrar Registro Articulos
def mostrar(v):
    for i in range(len(v)):
        print ("\033[1;34m"+"\n------------------------------")
        print ("Producto: ", v[i].producto)
        print ("Codigo De Publicacion: ", v[i].codigo)
        print ("Precio: $", v[i].precio)
        print ("Ubicacion: ", v[i].ubicacion)
        print ("Estado: ", v[i].estado)
        print ("Cantidad Disponible: ", v[i].cantidad)
        print ("Puntuacion Del Vendedor: ", v[i].puntuacion)
        print ("------------------------------"+'\033[0;m')



#Funcion Mostrar Registro Compras
def toString(compra):
    print("\033[1;34m"+"\n-----------------------------------------------")
    print('Compra #'+ str(compra.codig), " - ", str(compra.fecha))
    print("Resumen de Compra")
    print( 'Producto     $ '+ str(compra.pagar) + " (" + str(compra.cantidad) + " X " + " $" + str(compra.costo) + ")")
    if compra.envio != 0:
        print( "Cargo de Envio    $ " + str(compra.envio))
    else:
        print("Retira en Sucursal")
    print("Tu Pago          $ " + str(compra.toral_con_envio))
    print("-----------------------------------------------"+'\033[0;m')

#Funcion Compra de registro Compras
def compra(v, ind, arch):
    n = int(input("Ingrese Cantidad De Articulos Que Decea Comprar: "))
    #Comprobacion de Stock
    if v[ind].cantidad >= n:
        #Resta de la cantidad comprada
        v[ind].cantidad -= n
        cargoenvio = 0
        op = 0
        while op <= 0 or op > 2:
            #Consulta si envio a domicilio
            print("\nForma de Entrega:")
            print("1.Envío a domicilio (costo 10% de la compra)")
            print("2.Retira en Sucursal")
            op = int(input("Seleccione Opcione: "))
            if op == 1:
                #Suma del 10% por envio
                cargoenvio = v[ind].precio * 0.1
            elif op == 2:
                cargoenvio = 0
        print("Compra Exitosa")
        #Abrir archivo
        m = open(arch, 'ab')
        cod = v[ind].codigo
        can = n
        cos = v[ind].precio
        env = cargoenvio
        tot = (v[ind].precio * n)
        fec = time.strftime("%d/%m/%Y")
        totenv = (v[ind].precio * n) + int(cargoenvio)
        comp = Compras(cod, can, cos, env, tot, fec, totenv)
        pickle.dump(comp, m)
        m.flush()
        toString(comp)
        #Cerrar arhivo
        m.close()
    else:
        print("\nNo Se Pudo Ralizar La Compra. No Hay Cantidad Suficiente En Stock")
        return


#Opcion 4
def mostrar1(v):
        print("\033[1;34m"+"\n------------------------------")
        print("Producto: ", v.producto)
        print("Codigo de publicación: ", v.codigo)
        print("Precio: $", v.precio)
        print("Ubicacion: ", v.ubicacion)
        print("Estado: ", v.estado)
        print("Cantidad disponible: ", v.cantidad)
        print("Puntuacion del vendedor: ", v.puntuacion)
        print("------------------------------"+'\033[0;m')



def add_in_order(favoritos, x):
    n = len(favoritos)
    pos = n
    for i in range(n):
        if x.codigo < favoritos[i].codigo:
            if x.codigo == favoritos[i].codigo:
                favoritos[i].activo = False
            pos = i
            break

    favoritos[pos:pos] = [x]



def buscar(v, x, favoritos):
    n = len(v)
    for i in range(n):
        if v[i].codigo == x:
            print("Publicación encontrada:")
            add_in_order(favoritos, v[i])

            return favoritos

    print("Publicación no encontrada.")
    print()



def op_4(v, favoritos):
    x = int(input("Ingresar código de publicación que deseé buscar: "))
    buscar(v, x, favoritos)
    for i in range(len(favoritos)):
        if favoritos[i].activo:
            mostrar1(favoritos[i])


