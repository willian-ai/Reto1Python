from datetime import datetime
import statistics
from prettytable import PrettyTable



class Experimento:
    """Funcion para crear un experimento """
    def __init__(self, nombreExperimento, fechaExperimento, tipoExperimento, resultadoExperimento):
        # Atributos
        self.nombreExperimento = nombreExperimento
        self.fechaExperimento = fechaExperimento
        self.tipoExperimento = tipoExperimento
        self.resultadoExperimento = resultadoExperimento
    


def agregarExperimento(experimento):
    """
    Funcion para agregar un experimento
    """
    # Pedir los datos
    nombreExperimento = input("Ingrese el nombre del experimento: ").upper().strip()
    fechaExperimentoTemp = input('Ingrese la fecha del experimento (DD/MM/YYYY): ')
    try:
        fechaExperimento = datetime.strptime(fechaExperimentoTemp, "%d/%m/%Y")
    except ValueError:
        print("Fecha ingresada para el experimento, No es valida. ")
    print("""
    1) QUIMICA 
    2) BIOLOGIA    
    3) FISICA
    4) OTROS
    """)
    tipoExperimento = input("Ingrese el tipo de experiemento: ").strip().upper()
    # Validar
    if tipoExperimento == "1":
        tipoExperimento = "QUIMICA"
    elif tipoExperimento == "2":
        tipoExperimento = "BIOLOGIA"
    elif tipoExperimento == "3":
        tipoExperimento = "FISICA"
    elif tipoExperimento == "4":
        tipoExperimento = "OTROS"
    else:
        print("Tipo de experimento no valido")
        
         
    resultadoExperimentoNum = input("Ingrese el resultado del experimento separados por comas: ")
    try:
        resultadoExperimento = list(map(float, resultadoExperimentoNum.split(",")))
    except  ValueError:
        print("Datos no validas")
        return
    # Crear el objeto
    prueba = Experimento(nombreExperimento, fechaExperimento, tipoExperimento, resultadoExperimento)
    # Agregar el objeto
    experimento.append(prueba)
    # imprimir mensaje al realizar con exito agregar el experimento
    print("Experimento agregado con exito")


def vizualizarExperimento(experimento):
    """Funcion para vizualizar los experimentos"""
    # Si la lista no esta vacia
    if experimento:
        # Crear la tabla
        table = PrettyTable(border=True, header=True, padding_width=5)
      # Añadir los encabezados
        table.title = " EXPERIMENTOS CREADOS "
        # Añadir los encabezados
        table.field_names = [" <== NUMERO ==> ", " <== NOMBRE ==>", " <== FECHA ==>", " <== TIPO ==>", " <== RESULTADO ==>"]
        # Añadir los datos
        for i, test in enumerate(experimento, start=1):
            table.add_row([i, test.nombreExperimento.upper(), test.fechaExperimento.strftime('%d/%m/%Y'), test.tipoExperimento.upper(), test.resultadoExperimento], divider=True)
        # Alinear los datos
        table.align = "c"
        print(table)
       
    else:
        # Si la lista esta vacia
        print("No hay experimentos en la lista")
   
        

def calcularEstadistica(experimento):
    """ Funcion para calcular estadisticas """
    # Si la lista no esta vacia
    if  experimento: 
        table = PrettyTable(border=True, header=True, padding_width=5)
        table.field_names = ["<== NOMBRE ==>", "<== TIPO ==>","<== PROMEDIO ==>", "<== MAXIMO ==>", "<== MINIMO ==>"]
        # Añadir los datos
        for result in experimento:
            nombre = result.nombreExperimento.upper()
            tipo = result.tipoExperimento.upper()
            promedio = statistics.mean(result.resultadoExperimento)
            maximo = max(result.resultadoExperimento)
            minimo = min(result.resultadoExperimento)
            table.add_row([ nombre, tipo, promedio, maximo, minimo], divider=True)
        table.align = "c"    
        print(table)
        
    else:
        # Si la lista esta vacia
        print("No hay experimentos en la lista")
        return

def compararExperimentos(experimento):
    """Funcion para comparar experimentos"""
    # Mostrar los experimentos
    vizualizarExperimento(experimento)
    # Pedir los indices
    indices = list(map(int, input("Ingrese los dos experimentos que desea comparar separados por comas: ").split(",")))     
    # Comparar
    result_compara = []
    # Crear la tabla
    table = PrettyTable(border=True, header=True, padding_width=5)
    # Titulo de la tabla
    table.title = "EXPERIMENTOS COMPARADOS"
    # Añadir los encabezados
    table.field_names = ["<== NOMBRE ==>", "<== TIPO ==>","<== PROMEDIO ==>", "<== MAXIMO ==>", "<== MINIMO ==>"]
    # Añadir los datos
    for index in indices:
        if (1 <= index < len(experimento)+1):
            nombre = experimento[index - 1].nombreExperimento.upper()
            tipo = experimento[index - 1].tipoExperimento.upper()
            promedio = statistics.mean(experimento[index - 1].resultadoExperimento)
            maximo = max(experimento[index - 1].resultadoExperimento)
            minimo = min(experimento[index - 1].resultadoExperimento)
            result_compara.append(experimento[index - 1].nombreExperimento)
            result_compara.append(experimento[index - 1].tipoExperimento)
            result_compara.append(nombre)
            result_compara.append(tipo)
            result_compara.append(promedio)
            result_compara.append(maximo)
            result_compara.append(minimo)
            # Añadir los datos a la tabla a mostrar
            table.add_row([nombre, tipo, promedio, maximo, minimo], divider=True)
            
        else:
            # Si el indice ingresado no es valido
            print(f"El indice {index} ingresado no es valido")
    table.align = "c"
    print(table)
    return result_compara
def generarInforme(experimento):
    """Funcion para generar un informe"""
    if experimento:
        # Abrir un archivo txt para escribir un informe
        with open("informe_experimentos.txt", "w") as archivo:
            #Escribir los detalle de latarea en el Informe
            
            for informe in experimento:
                archivo.write("########################################\n")
                archivo.write(f"NOMBRE: {informe.nombreExperimento.upper()}\n")
                archivo.write(f"FECHA: {informe.fechaExperimento.strftime('%d/%m/%Y')}\n")
                archivo.write(f"TIPO: {informe.tipoExperimento.upper()}\n")
                archivo.write(f"RESULTADOS: {informe.resultadoExperimento}\n")
                archivo.write(f"PROMEDIO: {statistics.mean(informe.resultadoExperimento)}\n")
                archivo.write(f"MAXIMO: {max(informe.resultadoExperimento)}\n")
                archivo.write(f"MINIMO: {min(informe.resultadoExperimento)}\n")
                archivo.write("########################################\n")
                
        print("Informe generado con exito")
    else:
        print("No hay experimentos en la lista")
        return
    


def Menu():
    
    listaExperimento = [

        Experimento("Experimento 1", datetime.strptime("12/11/2024", "%d/%m/%Y"), "Química", [5, 3, 4, 5, 6, 4]),
        Experimento("Experimento 2", datetime.strptime("22/11/2024", "%d/%m/%Y"), "Física", [7, 8, 6, 9, 5]),
        Experimento("Experimento 3", datetime.strptime("03/10/2024", "%d/%m/%Y"), "Biologia", [17, 28, 36, 19, 25]),
        Experimento("Experimento 4", datetime.strptime("28/09/2024", "%d/%m/%Y"), "Biologia", [37, 18, 16, 19, 15]),

    ]
    while True:
        # Mostrar el menu
        print("=========== MENU PRINCIPAL ==============")
        print("======= GESTION DE EXPERIMENTOS =========")
        print("1. AGREGAR EXPERIMENTO")
        print("2. VIZUALIZAR EXPERIMENTOS")
        print("3. CALCULAR ESTADISTICA")
        print("4. COMPARAR EXPERIMENTOS")
        print("5. GENERAR INFORME")
        print("6. SALIR")
        print("=====================================")
        # Pedir la opcion
        opcion = int(input("Ingrese una opcion: "))
        # Ejecutar la opcion
        if opcion == 1:
            agregarExperimento(listaExperimento)
        elif opcion == 2:
            vizualizarExperimento(listaExperimento)
        elif opcion == 3:
            calcularEstadistica(listaExperimento)
        elif opcion == 4:
            compararExperimentos(listaExperimento)
        elif opcion == 5:
            generarInforme(listaExperimento)
        elif opcion == 6:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida")
            
Menu()

