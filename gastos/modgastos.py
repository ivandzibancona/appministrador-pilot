from datetime import date
import sqlite3

#Función para registrar compras 
def compras():
    print("\nREGISTRO DE COMPRAS")

    concepto = str(input("\nIngrese el concepto de la compra: "))

    costo = True
    while costo == True:
        try:
            costo = float(input("Ingrese el costo por unidad comprada: "))
            if costo <= 0:
                print("El costo tiene que ser mayor a 0")
                costo = True
        except Exception:
            print("El costo de la compra debe ser un valor numérico")
    
    cantidad = True
    while cantidad == True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos comprados: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                cantidad = True
        except Exception:
            print("La cantidad debe ser un valor numérico")

    costoCompra = float(costo*cantidad)
    fecha = str(date.today())    

    #Conexión a la base de datos y registro de compras
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacion = f"INSERT INTO registroCompras (producto, costo, cantidad, costoCompra, fecha) VALUES ('{concepto}', {costo}, {cantidad}, {costoCompra}, '{fecha}')"
    cursor.execute(informacion)

    conn.commit()
    conn.close()

    print("\n¡Se ha registrado una compra correctamente!")

    #Registro de una nueva compra
    nuevoRegistro = True

    while nuevoRegistro == True:
        nuevoRegistro = str(input("\n¿Desea hacer otro regitro?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if nuevoRegistro == "y" or nuevoRegistro == "Y":
            compras()
        elif nuevoRegistro == "n" or nuevoRegistro == "N":
            print("Saliendo...")
            return registrarGastos()
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            nuevoRegistro = True

#Función para registrar pago de servicios
def servicios():
    print("\nREGISTRO DE PAGO DE SERVICIOS")

    concepto = str(input("\nIngrese el concepto del servicio: "))

    monto = True
    while monto == True:
        try:
            monto = float(input("Ingrese el costo del servicio: "))
            if monto <= 0:
                print("El monto debe ser mayor a 0")
                monto = True
        except Exception:
            print("El monto debe ser un valor numérico")

    fecha = date.today()    

    #Conexión a la base de datos y registro de pago de servicios
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacion = f"INSERT INTO registroServicios (concepto, costo, fecha) VALUES ('{concepto}', {monto}, '{fecha}')"
    cursor.execute(informacion)

    conn.commit()
    conn.close()
    
    print("\nSe ha registrado un pago de servicio correctamente.")

    #Registrar nuevo pago de servicios
    nuevoRegistro = True

    while nuevoRegistro == True:
        nuevoRegistro = str(input("\n¿Desea hacer otro regitro?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if nuevoRegistro == "y" or nuevoRegistro == "Y":
            servicios()
        elif nuevoRegistro == "n" or nuevoRegistro == "N":
            print("Saliendo...")
            return registrarGastos()
        else:
            print("\nNo es una opción válida. Vuelva a intentarlo.")
            nuevoRegistro = True

#Función para registrar sueldos y salario
def sueldos():
    print("\nREGISTRO DE SUELDOS Y SALARIOS")

    nombreEmpleado = str(input("\nIngrese el nombre del empleado: "))
    apellidoEmpleado = str(input("Ingrese el apellido del empleado: "))

    sueldo = True
    while sueldo == True:
        try:
            sueldo = float(input("Ingrese el sueldo del empleado: "))
            if sueldo <= 0:
                print("El sueldo debe ser mayor a 0")
                sueldo = True
        except Exception:
            print("El sueldo debe ser un valor numérico")
    
    fecha = str(date.today())    

    #Conexión a la base de datos y registro de sueldos y salarios
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacion = f"INSERT INTO registroSueldos (nombreEmpleado, apellidoEmpleado, sueldo, fecha) VALUES ('{nombreEmpleado}', '{apellidoEmpleado}', {sueldo}, '{fecha}')"
    cursor.execute(informacion)

    conn.commit()
    conn.close()

    print("\n¡Se ha registrado un pago de sueldos y salarios exitosamente!")

    #Registrar nuevo pago de sueldos y salarios
    nuevoRegistro = True

    while nuevoRegistro == True:
        nuevoRegistro = str(input("\n¿Desea hacer otro regitro?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if nuevoRegistro == "y" or nuevoRegistro == "Y":
            sueldos()
        elif nuevoRegistro == "n" or nuevoRegistro == "N":
            print("Saliendo...")
            return registrarGastos()
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            nuevoRegistro = True

#Función para registrar intereses e impuestos
def impuestos():
    print("\nREGISTRO DE PAGO DE INTERESES E IMPUESTOS")

    concepto = str(input("\nIngrese el concepto del pago: "))

    monto = True
    while monto == True:
        try:
            monto = float(input("Ingrese el monto del pago: "))
            if monto <= 0:
                print("El monto debe ser mayor a 0")
                monto = True
        except Exception:
            print("El monto debe ser un valor numérico")
    
    fecha = date.today()    

    #Conexión a la base de datos y registro de intereses e impuestos
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacion = f"INSERT INTO registroImpuestos (conepto, monto, fecha) VALUES ('{concepto}', {monto}, '{fecha}')"
    cursor.execute(informacion)

    conn.commit()
    conn.close()

    print(f"¡Se ha registrado un pago de {concepto} correctamente!")

    #Registrar nuevo pago de interese e impuestos
    nuevoRegistro = True

    while nuevoRegistro == True:
        nuevoRegistro = str(input("\n¿Desea hacer otro regitro?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if nuevoRegistro == "y" or nuevoRegistro == "Y":
            impuestos()
        elif nuevoRegistro == "n" or nuevoRegistro == "N":
            print("Saliendo...")
            return registrarGastos()
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            nuevoRegistro = True

#Función para registrar costos de venta
def costoVentas():
    print("\nREGISTRO DE COSTOS DE VENTA")

    concepto = str(input("\nIngrese el concepto del costo de venta: "))

    monto = True
    while monto == True:
        try:
            monto = float(input("Ingrese el monto del costo de venta: "))
            if monto <= 0:
                print("El monto debe ser mayor a 0")
                monto = True
        except Exception:
            print("El monto debe ser un valor numérico")

    fecha = date.today()    

    #Conectar a base de datos y almacenar información de costos de venta
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacion = f"INSERT INTO registroCostoventas (concepto, monto, fecha) VALUES ('{concepto}', {monto}, '{fecha}')"
    cursor.execute(informacion)

    conn.commit()
    conn.close()

    print("\n¡Se ha registrado el pago de costos de venta exitosamente!")

    #Registrar nuevo costo de venta
    nuevoRegistro = True

    while nuevoRegistro == True:
        nuevoRegistro = str(input("\n¿Desea hacer otro regitro?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if nuevoRegistro == "y" or nuevoRegistro == "Y":
            costoVentas()
        elif nuevoRegistro == "n" or nuevoRegistro == "N":
            print("Saliendo...")
            return registrarGastos()
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            nuevoRegistro = True

#Función para registro de otros gastos
def otrosGastos():
    print("\nREGISTRO DE OTROS GASTOS")

    concepto = str(input("\nIngrese el concepto de otro gastos: "))

    monto = True
    while monto == True:
        try:
            monto = float(input("Ingrese el costo de otros gastos: "))
            if monto <= 0:
                print("El monto debe ser mayor a 0")
                monto = True
        except Exception:
            print("El monto debe ser un valor numérico")
    
    fecha = date.today()

    #Conexión a la base de datos y almacenar otros gastos
    conn = sqlite3.connect("miNegocio.db")
    cursor = conn.cursor()

    informacion = f"INSERT INTO registroOtrosgastos (concepto, monto, fecha) VALUES ('{concepto}', {monto}, '{fecha}')"
    cursor.execute(informacion)

    conn.commit()
    conn.close()

    print("\n¡Se ha registrado el pago de otros gastos exitosamente!")

    #Nuevo registro de otros gastos
    nuevoRegistro = True

    while nuevoRegistro == True:
        nuevoRegistro = str(input("\n¿Desea hacer otro regitro?\n\nSi = Y\nNo = N\n\nIngrese una opción aquí: "))

        if nuevoRegistro == "y" or nuevoRegistro == "Y":
            otrosGastos()
        elif nuevoRegistro == "n" or nuevoRegistro == "N":
            print("Saliendo...")
            return registrarGastos()
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            nuevoRegistro = True

#Menú para el registro gastos
def registrarGastos():
    
    registro = True

    while registro == True:
        registro = str(input("\nElija una opción para realizar un registro:\n\na) Registrar una compra\nb) Registrar pago de un servicio\nc) Registrar pago de sueldos y salarios\nd) Registrar pago de impuestos e intereses\ne) Registrar costos de venta\nf) Registrar otros gastos\ng) Salir\n\nIngrese una opción aquí: "))

        if registro == "a" or registro == "A":
            print("Preparando registro de compras...")
            compras()        
        elif registro == "b" or registro == "B":
            print("Preparando regitros de pago de servicios...")
            servicios()        
        elif registro == "c" or registro == "C":
            print("Preparando regitros de pago de sueldos y salarios...")
            sueldos()
        elif registro == "d" or registro == "D":
            print("Preparando regitros de pago de impuestos e intereses...")
            impuestos()        
        elif registro == "e" or registro == "E":
            print("Preparando regitros de pago de costos de venta")
            costoVentas()        
        elif registro == "f" or registro == "F":
            print("Preparando regitros de pago de otros gastos...")
            otrosGastos()
        elif registro == "g" or registro == "G":
            print("Saliendo...")
            break        
        else:
            print("No es una opción válida. Vuelva a intentarlo.")
            registro = True