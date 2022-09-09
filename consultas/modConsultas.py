import sqlite3

#Función para consultar los ingresos registrados en la base de datos.
def consultaIngresos():
    print("\nCONSULTA DE INGRESOS")

    consulta = True

    while consulta == True:
        consulta = str(input("\nElija un tipo de consulta\n\na) Consultar ingresos por fecha\nb) Consultar ingresos por concepto\n\nIngrese una opción aquí: "))

        if consulta == "a" or consulta == "A":
            print("Preparando consulta por fecha...")

            #Ingresar datos de consulta por fecha
            print("\nIngrese la fecha inicial de su consulta.")
            diaInicio = str(input("\nIngrese el día a dos dígitos: "))
            mesInicio = str(input("Ingrese el mes a dos dígitos: "))
            anioInicio = str(input("Ingrese el año a cuatro dígios: "))
            fechaInicial = str(f"{anioInicio}-{mesInicio}-{diaInicio}")
            
            print("\nIngrese la fecha final de su consulta.")
            diaFinal = str(input("\nIngrese el día a dos dígitos: "))
            mesFinal = str(input("Ingrese el mes a dos dígitos: "))
            anioFinal = str(input("Ingrese el año a cuatro dígios: "))
            fechaFinal = str(f"{anioFinal}-{mesFinal}-{diaFinal}")

            #Conexión a la base de datos y consulta de ingresos por fecha
            conn = sqlite3.connect("miNegocio.db")
            cursor = conn.cursor()

            informacion = f"SELECT * FROM registroVentas WHERE fecha BETWEEN '{fechaInicial}' AND '{fechaFinal}'"
            cursor.execute(informacion)
            resultados = cursor.fetchall()            

            conn.commit()
            conn.close()

            #Mostrar los resultados de la búsqueda en la base de datos
            print("\nResultados de la búsqueda:")
            for resultado in resultados:
                print("\nID | Producto | Precio | Cantidad | Importe | Fecha")
                print(resultado)

            #Realizar una nueva consulta de ingresos
            otraConsulta = True

            while otraConsulta == True:
                otraConsulta = str(input("\n¿Desea hacer otra consulta?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

                if otraConsulta == "y" or otraConsulta == "Y":
                    print("Preparando otra consulta...")
                    consulta = True
                elif otraConsulta == "n" or otraConsulta =="N":
                    print("Saliendo...")
                    return menuConsultas()
                else:
                    print("No es una opción válida. Vuelva a intentarlo.")
                    otraConsulta = True
                
        elif consulta == "b" or consulta == "B":
            print("Preparando consulta por concepto...")

            consultaConcepto = str(input("\nIngrese el concepto de la consulta:  "))

            #Conexión a la base de datos y consulta de ingresos por concepto
            conn = sqlite3.connect("miNegocio.db")
            cursor = conn.cursor()

            informacion = f"SELECT * FROM registroVentas WHERE producto LIKE '%{consultaConcepto}'"
            cursor.execute(informacion)
            resultados = cursor.fetchall()            

            conn.commit()
            conn.close()

            #Mostrar los resultados de la búsqueda en la base de datos
            print("\nResultados de la búsqueda:")
            for resultado in resultados:
                print("\nID | Producto | Precio | Cantidad | Importe | Fecha")
                print(resultado)

            #Realizar una nueva consulta de ingresos
            otraConsulta = True

            while otraConsulta == True:
                otraConsulta = str(input("\n¿Desea hacer otra consulta?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

                if otraConsulta == "y" or otraConsulta == "Y":
                    print("Preparando otra consulta...")
                    return consultaIngresos()
                elif otraConsulta == "n" or otraConsulta =="N":
                    print("Saliendo...")
                    return menuConsultas()
                else:
                    print("No es una opción válida. Vuelva a intentarlo.")
                    otraConsulta = True

        else:
            print("No es una opción válida. Vuleva a intentarlo.")
            consulta = True

def consultaGastos():
    print("\nCONSULTA DE GASTOS")

    consulta = True

    while consulta == True:
        consulta = str(input("\nElija un tipo de consulta\n\na) Consultar gastos por fecha\nb) Consultar gastos por concepto\n\nIngrese una opción aquí: "))

        if consulta == "a" or consulta == "A":
            print("Preparando consulta por fecha...")

            #Ingresar datos de consulta por fecha
            print("\nIngrese la fecha inicial de su consulta.")
            diaInicio = str(input("\nIngrese el día a dos dígitos: "))
            mesInicio = str(input("Ingrese el mes a dos dígitos: "))
            anioInicio = str(input("Ingrese el año a cuatro dígios: "))
            fechaInicial = str(f"{anioInicio}-{mesInicio}-{diaInicio}")
            
            print("\nIngrese la fecha final de su consulta.")
            diaFinal = str(input("\nIngrese el día a dos dígitos: "))
            mesFinal = str(input("Ingrese el mes a dos dígitos: "))
            anioFinal = str(input("Ingrese el año a cuatro dígios: "))
            fechaFinal = str(f"{anioFinal}-{mesFinal}-{diaFinal}")

            #Conexión a la base de datos y consulta de ingresos por fecha
            conn = sqlite3.connect("miNegocio.db")
            cursor = conn.cursor()

            informacion = f"SELECT * FROM registroCompras WHERE fecha BETWEEN '{fechaInicial}' AND '{fechaFinal}'"
            cursor.execute(informacion)
            resultados = cursor.fetchall()            

            conn.commit()
            conn.close()

            #Mostrar los resultados de la búsqueda en la base de datos
            print("\nResultados de la búsqueda:")
            for resultado in resultados:
                print("\nID | Producto | Precio | Cantidad | Importe | Fecha")
                print(resultado)

            #Realizar una nueva consulta de gastos
            otraConsulta = True

            while otraConsulta == True:
                otraConsulta = str(input("\n¿Desea hacer otra consulta?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

                if otraConsulta == "y" or otraConsulta == "Y":
                    print("Preparando otra consulta...")
                    return consultaGastos()
                elif otraConsulta == "n" or otraConsulta =="N":
                    print("Saliendo...")
                    return menuConsultas()
                else:
                    print("No es una opción válida. Vuelva a intentarlo.")
                    otraConsulta = True

        elif consulta == "b" or consulta == "B":
            print("Preparando consulta por concepto...")
            consultaConcepto = str(input("\nIngrese el concepto de la consulta:  "))

            #Conexión a la base de datos y consulta de ingresos por concepto
            conn = sqlite3.connect("miNegocio.db")
            cursor = conn.cursor()

            informacion = f"SELECT * FROM registroCompras WHERE producto LIKE '%{consultaConcepto}'"
            cursor.execute(informacion)
            resultados = cursor.fetchall()            

            conn.commit()
            conn.close()

            #Mostrar los resultados de la búsqueda en la base de datos
            print("\nResultados de la búsqueda:")
            for resultado in resultados:
                print("\nID | Producto | Precio | Cantidad | Importe | Fecha")
                print(resultado)

            otraConsulta = True

            while otraConsulta == True:
                otraConsulta = str(input("\n¿Desea hacer otra consulta?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

                if otraConsulta == "y" or otraConsulta == "Y":
                    print("Preparando otra consulta...")
                    consulta = True
                elif otraConsulta == "n" or otraConsulta =="N":
                    print("Saliendo...")
                    return menuConsultas()
                else:
                    print("No es una opción válida. Vuelva a intentarlo.")
                    otraConsulta = True

        else:
            print("No es una opción válida. Vuleva a intentarlo.")
            consulta = True

def consultaBalance():
    print("\nCONSULTA DEL BALANCE")

    #Ingresar datos de consulta por fecha
    print("\nIngrese la fecha inicial de su consulta.")
    diaInicio = str(input("\nIngrese el día a dos dígitos: "))
    mesInicio = str(input("Ingrese el mes a dos dígitos: "))
    anioInicio = str(input("Ingrese el año a cuatro dígios: "))
    fechaInicial = str(f"{anioInicio}-{mesInicio}-{diaInicio}")
            
    print("\nIngrese la fecha final de su consulta.")
    diaFinal = str(input("\nIngrese el día a dos dígitos: "))
    mesFinal = str(input("Ingrese el mes a dos dígitos: "))
    anioFinal = str(input("Ingrese el año a cuatro dígios: "))
    fechaFinal = str(f"{anioFinal}-{mesFinal}-{diaFinal}")

    #Conexión a la base de datos y consulta de ingresos y gastos por fecha
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacionVentas = f"SELECT importeVenta FROM registroVentas WHERE fecha BETWEEN '{fechaInicial}' AND '{fechaFinal}'"
    cursor.execute(informacionVentas)
    resultadoVentas = cursor.fetchall()

    informacionCompras = f"SELECT costoCompra FROM registroCompras WHERE fecha BETWEEN '{fechaInicial}' AND '{fechaFinal}'"
    cursor.execute(informacionCompras)
    resultadoCompras = cursor.fetchall()

    conn.commit()
    conn.close()

    #Calcular el total de las ventas y compras de la consulta

    #Calculo de total de ventas
    listaVentas = resultadoVentas[:]
    newListaVentas = []
    numVentas = len(listaVentas)

    for importe in range(numVentas):
        newListaVentas.append(listaVentas[importe][0])
        sumaVentas = sum(newListaVentas)

    #Calculo de total de compras
    listaCompras = resultadoCompras[:]
    newListaCompras = []
    numCompras = len(listaCompras)

    for costo in range(numCompras):
        newListaCompras.append(listaCompras[costo][0])
        sumaCompras = sum(newListaCompras)

    try:
        print(f"\nTotal de Ventas: ${sumaVentas} || Total de Compras: ${sumaCompras}\nBalance Final: ${sumaVentas-sumaCompras}")

    except Exception:
        print("\n¡No se encontró ningún resultado!")

    #Nueva consulta de balnce
    otraConsulta = True

    while otraConsulta == True:
        otraConsulta = str(input("\n¿Desea hacer otra consulta?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if otraConsulta == "y" or otraConsulta == "Y":
            print("Preparando otra consulta...")
            return consultaBalance()
        elif otraConsulta == "n" or otraConsulta =="N":
            print("Saliendo...")
            return menuConsultas()
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            otraConsulta = True

def menuConsultas():
    consultar = True

    while consultar == True:
        consultar = str(input("\nElija una opción para hacer una consulta:\n\na) Consultar ingresos\nb) Consultar gastos\nc) Consultar balance\nd) Salir\n\nIngrese una opción aquí: "))

        if consultar == "a" or consultar == "A":
            print("Preparando consulta de ingresos...")
            consultaIngresos()
        elif consultar == "b" or consultar == "B":
            print("Preparando consulta de gastos...")
            consultaGastos()
        elif consultar == "c" or consultar == "C":
            print("Preparando consulta de balance...")
            consultaBalance()
        elif consultar == "d" or consultar == "D":
            print("Saliendo...")
            break
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            consultar = True