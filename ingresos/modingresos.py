import sqlite3
from datetime import date

#Función para registrar ventas
def ventas():
    print("\nREGISTRO DE VENTA")

    producto = str(input("\nIngrese el nombre del producto: "))

    precio = True
    while precio == True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("El precio tiene que ser mayor que 0")
                precio = True
        except Exception:
            print("El precio tiene que ser un valor numérico")

    cantidad = True
    while cantidad == True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                cantidad = True
        except Exception:
            print("La cantidad debe ser un valor numérico")

    importeTotal = float(precio*cantidad)
    fecha = str(date.today())

    #Conexión a base de dato y registro de información de ventas
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacion = f"INSERT INTO registroVentas (producto, precio, cantidad, importeVenta, fecha) VALUES ('{producto}', {precio}, {cantidad}, {importeTotal}, '{fecha}')"
    cursor.execute(informacion)

    conn.commit()
    conn.close()

    print("\n¡Se ha registrado una venta exitosamente!")
    print(f"\n**** Datos de la venta ****\n\nProducto: {producto}\nPrecio unitario: ${precio}\nCantidad vendida: {cantidad}\nImporte total: ${importeTotal}\n\nFecha de venta: {fecha}")

    #Nuevo registro de ventas
    nuevoRegistro = True

    while nuevoRegistro == True:
        nuevoRegistro = str(input("\n¿Desea hacer otro regitro?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if nuevoRegistro == "y" or nuevoRegistro == "Y":
            ventas()
        elif nuevoRegistro == "n" or nuevoRegistro == "N":
            print("Saliendo...")
            return registrarIngresos()
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            nuevoRegistro = True

#Función para registrar ingresos de capital
def capital():
    print("\nREGISTRO DE INGRESO DE CAPITAL")

    origenCapital = str(input("\nIngrese de dónde obtuvo su capital: "))
    
    monto = True
    while monto == True:
        try:
            monto = float(input("Ingrese el monto de capital: "))
            if monto <= 0:
                print("El monto tiene que ser mayor a 0")
                monto = True
        except Exception:
            print("El monto tiene que ser un valor numérico")    
    
    fecha = str(date.today())

    #Conexión a la base de datos y registro de información de ingreso de capital
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacion = f"INSERT INTO registroCapital (concepto, monto, fecha) VALUES ('{origenCapital}', {monto}, '{fecha}')"
    cursor.execute(informacion)

    conn.commit()
    conn.close()

    print("\n¡Se ha registrado un ingreso de capital exitosamente!")

    #Nuevo registro de ingreso de capital
    nuevoRegistro = True

    while nuevoRegistro == True:
        nuevoRegistro = str(input("\n¿Desea hacer otro regitro?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if nuevoRegistro == "y" or nuevoRegistro == "Y":
            capital()
        elif nuevoRegistro == "n" or nuevoRegistro == "N":
            print("Saliendo...")
            return registrarIngresos()
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            nuevoRegistro = True

#Función para registrar otros ingresos
def otrosIngresos():
    print("\nREGISTRO DE OTROS INGRESOS")

    concepto = str(input("\nIngrese el concepto del ingreso: "))
    
    monto = True
    while monto == True:
        try:
            monto = float(input("Ingrese el monto del ingreso: "))
            if monto <= 0:
                print("El monto tiene que ser mayor a 0")
                monto = True
        except Exception:
            print("El monto tiene que ser un valor numérico")

    fecha = str(date.today())

    #Conexión a la base de datos y registro de otros ingresos
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacion = f"INSERT INTO registroOtrosingresos (concepto, monto, fecha) VALUES ('{concepto}', {monto}, '{fecha}')"
    cursor.execute(informacion)

    conn.commit()
    conn.close()

    #Nuevo registro de otros ingresos
    nuevoRegistro = True

    while nuevoRegistro == True:
        nuevoRegistro = str(input("\n¿Desea hacer otro regitro?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if nuevoRegistro == "y" or nuevoRegistro == "Y":
            otrosIngresos()
        elif nuevoRegistro == "n" or nuevoRegistro == "N":
            print("Saliendo...")
            return registrarIngresos()
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            nuevoRegistro = True

#Menú de registro de ingresos
def registrarIngresos():
    
    registro = True

    while registro == True:
        registro = str(input("\nElija una opción para realizar un registro\n\na) Registrar una venta\nb) Registrar ingreso de capital\nc) Registrar otro tipo de ingreso\nd) Salir\n\nIngrese una opción aquí: "))

        if registro == "a" or registro == "A":
            print("Preparando registro de venta...")
            ventas()
        elif registro == "b" or registro == "B":
            print("Preparando registro de capital...")
            capital()
        elif registro == "c" or registro == "C":
            otrosIngresos()
        elif registro == "d" or registro == "D":
            print("Saliendo...")
            break
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            registro = True