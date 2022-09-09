from ingresos import modingresos
from gastos import modgastos
from consultas import modConsultas

print("BIENVENIDO A APPMINISTRADOR")

print("Appministrador es una aplicación de gestión de recursos para emprendedores, micro y pequeñas empresas. Es una herramienta muy intuitiva y no se requiere de conocimientos técnicos en informática o administración para poder usarla.")

def main():
    seleccionar = True

    while seleccionar == True:
        seleccionar = str(input("\nMenú de opciones:\n\na) Registrar Ingresos\nb) Registrar Costos y Gastos\nc) Consultas\nd) Salir\n\nIngrese una opción aquí: "))

        if seleccionar == "a" or seleccionar == "A":
            print("Preparando registro de ingresos...")
            modingresos.registrarIngresos()
            return main()
        elif seleccionar == "b" or seleccionar == "B":
            print("Preparando registro de costos y gastos...")
            modgastos.registrarGastos()
            return main()
        elif seleccionar == "c" or seleccionar == "C":
            print("Preparando consultas...")
            modConsultas.menuConsultas()
            return main()
        elif seleccionar == "d" or seleccionar == "D":
            print("Saliendo del programa...")
            exit()
        else:
            print("No es una opción válida. Intente nuevamente.")
            seleccionar = True

main()
