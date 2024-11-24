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
    1) Qimica       3) Fisica
    2) Ciencias        4) Otros
    """)
    tipoExperimento = input("Ingrese el tipo de experiemento: ").upper().strip()
    
    if tipoExperimento == "1":
        tipoExperimento = "Quimica"
    elif tipoExperimento == "2":
        tipoExperimento = "Bilogia"
    elif tipoExperimento == "3":
        tipoExperimento = "Fisica"
    elif tipoExperimento == "4":
        tipoExperimento = "Otro"
    else:
        print("Tipo de experimento no valido")
        
         
    resultadoExperimentoNum = input("Ingrese el resultado del experimento separados por comas: ")
    try:
        resultadoExperimento = list(map(float, resultadoExperimentoNum.split(",")))
    except  ValueError:
        print("Horas no validas")
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
        table.title = "EXPERIMENTOS"
        # Añadir los encabezados
        table.field_names = [" <== NUMERO ==> ", " <== NOMBRE ==>", " <== FECHA ==>", " <== TIPO ==>", " <== RESULTADO ==>"]
        # Añadir los datos
        for i, test in enumerate(experimento, start=1):
            table.add_row([i, test.nombreExperimento, test.fechaExperimento.strftime('%d/%m/%Y'), test.tipoExperimento, test.resultadoExperimento], divider=True)
        # Alinear los datos
        table.align = "l"
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
            nombre = result.nombreExperimento
            tipo = result.tipoExperimento
            promedio = statistics.mean(result.resultadoExperimento)
            maximo = max(result.resultadoExperimento)
            minimo = min(result.resultadoExperimento)
            table.add_row([ nombre, tipo, promedio, maximo, minimo], divider=True)
            
        print(table)
        
    else:
        # Si la lista esta vacia
        print("No hay experimentos en la lista")
        return

def compararExperimentos(experimento):
    """Funcion para comparar experimentos"""
    vizualizarExperimento(experimento)
    indices = list(map(int, input("Ingrese los dos experimentos que desea comparar separados por comas: ").split(",")))
    result_compara = []
    for index in indices:
        if (0 <= index < len(experimento)):
            promedio = statistics.mean(experimento[index - 1].resultadoExperimento)
            result_compara.append(promedio)
            #maximo = max(experimento[index - 1].resultadoExperimento)
            #minimo = min(experimento[index - 1].resultadoExperimento)
            #result_compara.append( promedio)
        else:
            print(f"El indice {index} ingresado no es valido")
   
    print(f"Experimentos comparados: {result_compara} \n")
    #for result, promedio in result_compara:
    #    print(f"Experimento {result} con promedio {promedio}")
    return

def generarInforme(experimento):
    """Funcion para generar un informe"""
    if experimento:
        # Abrir un archivo txt para escribir un informe
        with open("informe_experimentos.txt", "w") as archivo:
            #Escribir los detalle de latarea en el Informe
            
            for informe in experimento:
                archivo.write("########################################\n")
                archivo.write(f"Nombre: {informe.nombreExperimento}\n")
                archivo.write(f"Fecha: {informe.fechaExperimento.strftime('%d/%m/%Y')}\n")
                archivo.write(f"Tipo: {informe.tipoExperimento}\n")
                archivo.write(f"Resultado: {informe.resultadoExperimento}\n")
                archivo.write(f"Promedio: {statistics.mean(informe.resultadoExperimento)}\n")
                archivo.write(f"Maximo: {max(informe.resultadoExperimento)}\n")
                archivo.write(f"Minimo: {min(informe.resultadoExperimento)}\n")
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
        print("======= Menu Principal ============")
        print("======= Gestion de Experimentos =========")
        print("1. Agregar Experimento")
        print("2. Visualizar Experimentos")
        print("3. Calcular Estadisticas")
        print("4. Comprar Experimentos")
        print("5. Generar Informe")
        print("6. Salir")
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

