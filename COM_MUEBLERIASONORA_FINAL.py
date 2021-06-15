def menu_principal(): # Función de origen que lleva a las otras funciones.
    """Función que crea al menú principal del cual se llama el resto
       de las funciones."""
    print("¡Bienvenido a Mueblería Sonora!\n")
    print("¿Qué desea hacer?")
    print("1) Registrar una venta.") 
    print("2) Consultar datos del inventario.")
    print("3) Registrar productos y llegada de artículos al almacén.")
    print("4) Consultar datos de las ventas.")
    print("5) Mostrar reportes de ventas por vendedor o por artículo.")
    print("6) Agregar vendedores.")
    print("7) Salir")    

    while True: # Ciclo infinito para asegurar que se cumpla lo pedido. 
        try: # Intenta convertir el input a integer.
            resp=int(input("Favor de ingresar la opción correspondiente:"))
            if resp >= 1 and resp <= 7:
                break # Si la resp es un numero entre 1 y 7, sale del ciclo.
            """Si sale del ciclo, la variable resp se
            queda con su ultimo valor otorgado."""
            if resp < 1 or resp > 7: 
                print("Respuesta Inválida")
                print()
        except: # Si no pudo convertir a int la resp, repite el ciclo.
            print("Respuesta Inválida")
            print()
            continue
    
    if resp == 1: # Proceso para registrar ventas.
        indice = 0
        encabezado_ventas() # Se llama la función para llamar el encabezado.
        indice = index_reg_ventas(indice)
        reg_venta(indice, matriz_vendedor, matriz_ventas, mat_inv)
    elif resp == 2: # Proceso para consultar datos del inventario.
        consulta_inventario(mat_inv)
    elif resp == 3: # Proceso para registrar productos y su llegada.
        indice = 0
        encabezado_agregar_productos() # Función para crear el encabezado.
        indice = index_agregar_productos(indice, linea) # Crea al indice.
        agregar_productos(indice) # Se agregan los indices previos.
    elif resp == 4: # Proceso para consultar las ventas. 
        consulta_ventas(matriz_ventas)
    elif resp == 5:
        while True: # Ciclo infinito para asegurar que se cumpla lo pedido. 
            try: # Intenta convertir el input a integer.
                tipo = int(input("Reportes por artículos,"
                                  + " presione 1."
                                  + " Por vendedor, presione 2: "))
                if tipo == 1 or tipo == 2:
                    
                    """Si la resp es 1 o 2, se sale del ciclo,
                       y "tipo" guarda su ultimo valor asignado."""
                
                    break 
                """Si sale del ciclo, la variable resp se
                    queda con su ultimo valor otorgado."""
                if resp != 1 and resp != 2: 
                    print("Respuesta Inválida")
                print()
            except: # Si no pudo convertir a int la resp, repite el ciclo.
                print("Respuesta Inválida")
                print()
                continue
        print()
        if tipo == 1:
            encabezado_reporte_producto() # Función del reporte por articulos.
            reporte_producto(matriz_ventas, mat_inv)
        else:
            encabezado_reporte_vendedor() # Función del reporte por vendedor.
            reporte_vendedor(matriz_ventas)
    elif resp == 6: # Proceso para agregar vendedores. 
        indice = 0
        encabezados_vendedores() 
        indice = index_agregar_vendedores(indice)
        agregar_vendedores(indice)        
    elif resp == 7: # Opción para salir o terminar el programa. 
        print("Gracias por visitar a Mueblería Sonora")
        exit()

def index_agregar_productos(indice, linea):
    """Establecimiento de un índice para los nuevos productos"""
    abrir = open("inventario.txt",'r') # Se abre el archivo para lectura.
    while True: # Repite el ciclo infinito hasta que no haya líneas por leer.
        indice += 1 # En cada repetición se le suma uno al índice.
        linea = abrir.readline() # Se lee por línea el archivo.
        if not linea: # Si no hay lineas, sale del ciclo.
            break 
    abrir.close() # Se cierra el archivo de lectura.
    return indice - 2 # Regresa el valor del ínidice - 2.
    """ Se le resta dos al índice para reajustarlo a los valores de los
    índices de los productos del archivo."""

def index_reg_ventas(indice):
    """Establecimiento de un índice para los nuevos productos"""
    abrir = open("registro_ventas.txt",'r') # Se abre el archivo para lectura.
    while True: # Repite el ciclo infinito hasta que no haya líneas por leer.
        indice += 1 # En cada repetición se le suma uno al índice.
        linea = abrir.readline() # Se lee por línea el archivo.
        if not linea: # Si no hay lineas, sale del ciclo.
            break 
    abrir.close() # Se cierra el archivo de lectura.
    return indice - 1 # Regresa el valor del ínidice - 2.
    """ Se le resta dos al índice para reajustarlo a los valores de los
    índices de los productos del archivo."""

def index_agregar_vendedores(indice):
    """Establecimiento de un índice para los nuevos productos"""
    abrir = open("vendedores.txt",'r') # Se abre el archivo para lectura.
    while True: # Repite el ciclo infinito hasta que no haya líneas por leer.
        indice += 1 # En cada repetición se le suma uno al índice.
        linea = abrir.readline() # Se lee por línea el archivo.
        if not linea: # Si no hay lineas, sale del ciclo.
            break 
    abrir.close() # Se cierra el archivo de lectura.
    return indice - 2 # Regresa el valor del ínidice - 2.
    """ Se le resta dos al índice para reajustarlo a los valores de los
    índices de los productos del archivo."""

def decision():
    """Función que recibirá la instrucción del usario."""
    while True: # Ciclo infinito para asegurar que se cumpla lo pedido. 
        try: # Intenta convertir el input a integer.
            resp = int(input("¿Desea registrar una venta?"
                                  + " 1.sí 2.no: "))
            if resp == 1 or resp == 2:
                return resp # Si la resp es 1 o 2, sale del ciclo.
            #Si sale del ciclo, se guarda resp con su último valor.
            elif resp != 1 and resp != 2: 
                print("Respuesta Inválida")
                print()
        except: # Si no pudo convertir a int la resp, repite el ciclo.
            print("Respuesta Inválida")
            print()
            continue
    print()
def decision_a_menu_principal():
    """Función que regrese al menu principal."""
    while True: # Ciclo infinito para asegurar que se cumpla lo pedido. 
        try: # Intenta convertir el input a integer.
            resp = int(input("¿Desea regresar al menu pricipal?"
                                  + " 1.sí 2.no: "))
            if resp == 1 or resp == 2:
                return resp # Si la resp es 1 o 2, sale del ciclo.
            #Si sale del ciclo, se guarda resp con su último valor.
            elif resp != 1 and resp != 2: 
                print("Respuesta Inválida")
                print()
        except: # Si no pudo convertir a int la resp, repite el ciclo.
            print("Respuesta Inválida")
            print()
            continue
    print()

def agregar_productos(indice):
    """Agrega productos al inventario al pedirle input al usuario."""
    contador = indice # Declara a varible contador usando la constante indice.
    print("Mueblería Sonora\n") # Imprime la marquesina.
    print("Agregar Productos\n")
    resp = 0 # Declara la variable resp.
    while True: # Ciclo infinito para asegurar que se cumpla lo pedido. 
        try: # Intenta convertir el input a integer.
            resp = int(input("¿Desea agregar algún producto?"
                                  + " 1.sí 2.no: "))
            if resp == 1 or resp == 2:
                break # Si la resp es 1 o 2, sale del ciclo.
            #Si sale del ciclo, se guarda resp con su último valor.
            elif resp != 1 and resp != 2: 
                print("Respuesta Inválida")
                print()
        except: # Si no pudo convertir a int la resp, repite el ciclo.
            print("Respuesta Inválida")
            print()
            continue
    print()
    
    while resp == 1: # Si la resp es 1, se piden datos del producto.
        contador += 1 # Se le suma uno a contador.
        # El valor actual de contador es el ID del producto a agregar.
        modelo = str(input("Ingrese el modelo del producto: "))
        comprobacion = modelo.split() # Se crea una lista con el input.
        longitud = len(comprobacion) # Se mide la longitud de la lista.
        
        """Mientras la entrada sea un espacio vacío o más de una
        palabra, rechazará la entrada y pedirá de nuevo el modelo."""
        
        while modelo == "" or longitud == 0 or longitud > 1:
            print("Modelo Inválido")
            print()
            modelo = str(input("Ingrese el modelo del producto: "))
            comprobacion = modelo.split()
            longitud = len(comprobacion)
        print()
        nombre = str(input("Ingrese el nombre del producto: "))
        comprobacion = nombre.split() # Se crea una lista con el input.
        longitud = len(comprobacion) # Se mide la longitud de la lista.
        
        """Mientras la entrada sea un espacio vacío o más de una
        palabra, rechazará la entrada y pedirá de nuevo el nombre."""
        
        while nombre == "" or longitud == 0 or longitud > 1:
            print("Nombre Inválido")
            nombre = str(input("Ingrese el nombre del producto: "))
            comprobacion = nombre.split()
            longitud = len(comprobacion)
        print()
        while True: # Este ciclo infinito asegura que se ingrese input válido.
            try: # Permite pedir input y verificar si es integer. 
                existencia = int(input("Ingrese la cantidad del producto en"
                                       + " existencia: "))
                if existencia <= 0:
                    print("Cantidad Inválida")
                elif existencia > 0:
                    break # Si cumple con la condición, sale del ciclo.
            except: # Si falla en try, except permite que continúe el ciclo.
                print("Cantidad Inválida")
                continue # Acaba la iteración actual y va a la siguiente.           
        print()
        while True: # Este ciclo infinito asegura que se ingrese input válido.
            try: # Permite pedir input y verificar si es float. 
                precio = float(input("Ingrese el precio del producto: "))
                if precio < 0:
                    # Si cumple con la condición sigue el ciclo.
                    print("Cantidad Inválida")
                elif precio > 0:
                    break 
            except: 
                print("Cantidad Inválida")
                continue 
        print()
        while True: 
            try:  # Permite pedir input y verificar si es integer. 
                mes = int(input(("Ingrese el mes de llegada al almacén"
                                 + " numéricamente (ejemplo: 01): ")))
                if mes < 1 or mes > 12:
                    print("Mes Inválido")
                else:   
                    break 
            except: # Si falla en try, except permite que continúe el ciclo.
                print("Mes Inválido")
                continue 
        print() 
        while True: 
            try: # Permite pedir input y verificar si es integer. 
                dia = int(input("Ingrese el día de llegada al almacén: "))
                """ Si se cumple con la condición de mes, se somete a
                verificación la validez de la variable "día" de acuerdo
                al mes ingresado. Si resulta ser válido, sale del
                ciclo, sino continúa rechazando la entrada de "día"."""
                if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    if dia <1 or dia > 30:
                        print("Día Inválido")
                    elif dia >= 1 and dia <= 30:
                        break
                elif mes == 2:
                    if dia < 1 or dia > 29:
                        print("Día Inválido")
                    elif dia >= 1 and dia <= 29:
                        break
                else:
                    if dia <1 or dia > 31:
                        print("Día Inválido")
                    elif dia >= 1 and dia <= 31:
                        break
            except:
                print("Día Inválido")
                continue    
        print()
        while True:
            try: # Permite pedir input y verificar si es integer. 
                anio = int(input(("Ingrese el año de llegada al almacén"
                                  + "(ejemplo: 2020): ")))
                if anio < 2000: 
                    print("Año Inválido")
                else:
                    break
            except:
                print("Año Inválido")
                continue
        print()
        
        fecha=(str(dia)+"/"+str(mes)+"/"+str(anio)) # Se concatenan datos.
        # El método lower se usa para volver minúscula a lo que está guardado.
        modelo_minuscula = modelo.lower()
        nombre_minuscula = nombre.lower()
        escribir = open("inventario.txt", "a") # Se abre el file con append.
        escribir.write(("{0:<15}   ".format(contador) # Se le da formato.
                          + "{0:<15}   ".format(modelo_minuscula)
                          + "{0:<30}   ".format(nombre_minuscula)
                          + "{0:<15}   ".format(existencia)
                          + "{0:<15}   ".format(precio)
                          + "{0}".format(fecha)) + "\n")
        while True:  # Ciclo infinito para asegurar que se cumpla lo pedido.
            try: # Permite pedir input y verificar si es integer.
                resp = int(input("¿Desea agregar"
                                      + " otro producto? 1.sí 2.no: "))
                if resp == 1 or resp == 2: 
                    break # Si cumple con la condición sale del ciclo while.
                else: # Si no la cumple, sigue reptiéndose el ciclo.
                    print("Respuesta Inválida")
            except: # Si se recibe un input con error, inicia el ciclo.
                print("Respuesta Inválida")
                continue
        escribir.close() # Se  cierra el archivo.
    if resp == 2:
        menu_principal() # Se llama la función de menú principal de nuevo.

def agregar_vendedores(indice):
    """Agrega productos al inventario al pedirle input al usuario."""
    contador = indice # Declara a varible contador usando la constante indice.
    print("Mueblería Sonora\n") # Imprime la marquesina.
    print("Agregar Vendedores\n")
    resp = 0 # Declara la variable resp.
    while True: # Ciclo infinito para asegurar que se cumpla lo pedido. 
        try: # Intenta convertir el input a integer.
            resp = int(input("¿Desea agregar algún vendedor?"
                                  + " 1.sí 2.no: "))
            if resp == 1 or resp == 2:
                break # Si la resp es 1 o 2, sale del ciclo.
            #Si sale del ciclo, se guarda resp con su último valor.
            elif resp != 1 and resp != 2: 
                print("Respuesta Inválida")
                print()
        except: # Si no pudo convertir a int la resp, repite el ciclo.
            print("Respuesta Inválida")
            print()
            continue
    print()
    if resp == 2:
        menu_principal() # Se llama la función de menú principal de nuevo.
    
    while resp == 1: # Si la resp es 1, se piden datos del producto.
        contador += 1 # Se le suma uno a contador.
        # El valor actual de contador es el ID del producto a agregar.
        nombre = str(input("Ingrese el nombre del vendedor"
                               + " (una sola palabra): "))
        comprobacion = nombre.split() # Se crea una lista con el input.
        longitud = len(comprobacion) # Se mide la longitud de la lista.
        
        """Mientras la entrada sea un espacio vacío o más de una
        palabra, rechazará la entrada y pedirá de nuevo el modelo."""
        
        while nombre == "" or longitud == 0 or longitud > 1:
            print("Nombre Inválido")
            print()
            nombre = str(input("Ingrese el nombre del vendedor"
                               + " (una sola palabra): "))
            comprobacion = nombre.split()
            longitud = len(comprobacion)
        print()
        apellido = str(input("Ingrese el primer apellido del vendedor"
                             + "(sólo una palabra): "))
        comprobacion = apellido.split() # Se crea una lista con el input.
        longitud = len(comprobacion) # Se mide la longitud de la lista.
        
        """Mientras la entrada sea un espacio vacío o más de una
        palabra, rechazará la entrada y pedirá de nuevo el nombre."""
        
        while apellido == "" or longitud == 0 or longitud > 1:
            print("Apellido Inválido")
            apellido = str(input("Ingrese el primer apellido del vendedor"
                                 + "(sólo una palabra): "))
            comprobacion = apellido.split()
            longitud = len(comprobacion)
        print()
        # El método title se usa para volver mayúscula a la primer letra
        nombre_titulo = nombre.title()
        apellido_titulo = apellido.title()
        escribir = open("vendedores.txt", "a") # Se abre el file con append.
        escribir.write(("{0:<10}   ".format(contador) # Se le da formato.
                          + "{0:<15}   ".format(nombre_titulo)
                          + "{0:<30}   ".format(apellido_titulo) + "\n"))
        while True:  # Ciclo infinito para asegurar que se cumpla lo pedido. 
            try: # Permite pedir input y verificar si es integer. 
                resp = int(input("¿Desea agregar"
                                      + " otro vendedor? 1.sí 2.no: "))
                if resp == 1 or resp == 2: 
                    break # Si cumple con la condición sale del ciclo while.
                else: # Si no la cumple, sigue reptiéndose el ciclo.
                    print("Respuesta Inválida")
            except: # Si se recibe un input con error, inicia el ciclo.
                print("Respuesta Inválida")
                continue
        escribir.close()# Se  cierra el archivo.
        if resp == 2:
            menu_principal() # Se llama la función de menú principal de nuevo.

def reg_venta(indice, matriz_vendedor, matriz_ventas, mat_inv):
    """Inserta los datos solicitados dentro de una matriz que conforme
       la venta."""
    print("Mueblería Sonora\n")
    print("Registro de Ventas\n")
    size_vendedor = len(matriz_vendedor)
    size_inventario = len(mat_inv)
    size_ventas = len(matriz_ventas)
    contador = indice
    while True: # Este ciclo infinito asegura que se ingrese input válido.
        try: # Permite pedir input y verificar si es integer. 
            encargado = int(input("Ingrese el ID del vendedor encargado"
                                  +" de la venta: "))
            if encargado <= 0 or encargado > size_vendedor - 1:
                print("Número Inválido")
            elif encargado > 0 and  encargado <= size_vendedor - 1:
                break # Si cumple con la condición, sale del ciclo.
        except: # Si falla en try, except permite que continúe el ciclo.
            print("Número Inválido")
            continue # Acaba la iteración actual y va a la siguiente.    
    nombre = matriz_vendedor[encargado][1]
    apellido = matriz_vendedor[encargado][2]
    while True: # Este ciclo infinito asegura que se ingrese input válido.
        try: # Permite pedir input y verificar si es integer. 
            id_producto = int(input("Ingrese el ID del producto: "))
            if id_producto <= 0 or id_producto > size_inventario -1:
                print("Número Inválido")
            elif id_producto > 0 and  id_producto <= size_inventario - 1:
                break # Si cumple con la condición, sale del ciclo.
        except: # Si falla en try, except permite que continúe el ciclo.
            print("Número Inválido")
            continue # Acaba la iteración actual y va a la siguiente.
    producto_indexado= mat_inv[id_producto][0]
    precio = mat_inv[id_producto][4] 
    while True: # Este ciclo infinito asegura que se ingrese input válido.
        try: # Permite pedir input y verificar si es integer. 
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            if cantidad <= 0 or cantidad > int(mat_inv[id_producto][3]):
                print("Número Inválido")
            elif cantidad > 0 and  cantidad <= int(mat_inv[id_producto][3]):
                break # Si cumple con la condición, sale del ciclo.
        except: # Si falla en try, except permite que continúe el ciclo.
            print("Número Inválido")
            continue # Acaba la iteración actual y va a la siguiente.
    lista_datos = [contador,nombre,apellido,producto_indexado,precio,cantidad]
    contador += 1
    print("Esta es la información de la venta.")
    print(lista_datos)
    print()
    while True: # Ciclo infinito para asegurar que se cumpla lo pedido. 
        try: # Intenta convertir el input a integer.
            resp = int(input("¿Desea registrar la venta?"
                                  + " 1.sí 2.no: "))
            if resp == 1 or resp == 2:
                break # Si la resp es 1 o 2, sale del ciclo.
            """Si sale del ciclo, la variable resp se
            queda con su ultimo valor otorgado."""
            if resp != 1 and resp != 2: 
                print("Respuesta Inválida")
                print()
        except: # Si no pudo convertir a int la resp, repite el ciclo.
            print("Respuesta Inválida")
            print()
            continue
    print()
    cantidad_productos = 0
    if resp == 1: # Se confirma la venta y se registra.
        for i in range(len(mat_inv)): # Se cicla para agregar la venta.
            if mat_inv[i][0] == str(id_producto): # Se 
                cantidad_productos = int(mat_inv[i][3]) # Integra el string.
                if cantidad_productos < cantidad: 
                    reg_venta(indice, matriz_vendedor, matriz_ventas, mat_inv)
                else:
                    cantidad_productos -= cantidad # Resta la cantidad previa.
                    mat_inv[i][3] = cantidad_productos
                    erase = open("inventario.txt", "w") # Abre inventario.txt.
                    erase.close() # Cierra inventario.txt.
                    for j in range(len(mat_inv)):
                        new_cant = open("inventario.txt", "a")
                        # El inventario se reescribe según el formato.
                        new_cant.write(("{0:<15}   ".format(mat_inv[j][0]) 
                              + "{0:<15}   ".format(mat_inv[j][1])
                              + "{0:<30}   ".format(mat_inv[j][2])
                              + "{0:<15}   ".format(mat_inv[j][3])
                              + "{0:<15}   ".format(mat_inv[j][4])
                              + "{0}".format(mat_inv[j][5]) + "\n")) 
                        new_cant.close() # Se cierra inventario.txt.
        unir_registro = open("registro_ventas.txt", "a") 
        pluma = (("{:<15}   ".format(lista_datos[0])
                     + "{:<15}   ".format(lista_datos[1])
                     + "{:<30}   ".format(lista_datos[2])
                     + "{:<15}   ".format(lista_datos[3])
                     + "{:<15}   ".format(lista_datos[4])
                     + "{}".format(lista_datos[5]) + "\n"))
        unir_registro.write(pluma)
        unir_registro.close() # Cierra registro_ventas luego de editar. 
        retorno = decision_a_menu_principal() # Pregunta si se desea salir.
        if retorno == 1:
            menu_principal()
        elif retorno == 2:
            reg_venta(contador, matriz_vendedor, matriz_ventas, mat_inv) 
    if resp == 2:
        menu_principal() # Se llama la función de menú principal de nuevo.
def consulta_inventario(mat_inv):
    """Se presenta el inventario actual."""
    print("Mueblería Sonora\n") # Imprime la marquesina.
    print("Datos Inventario\n")
    tamano = len(mat_inv)
    for i in range(tamano):
        pluma = (("{0:<10}   ".format(mat_inv[i][0])
                  + "{0:<15}   ".format(mat_inv[i][1])
                  + "{0:<20}   ".format(mat_inv[i][2])
                  + "{0:<15}   ".format(mat_inv[i][3])
                  + "{0:<15}   ".format(mat_inv[i][4])
                  + "{0}".format(mat_inv[i][5])) + "\n")
        print(pluma)
    print()
    resp = decision_a_menu_principal()
    if resp == 1:
        menu_principal() # Se llama la función de menú principal de nuevo.
    elif resp == 2:
        print("\nGracias por visitar a Mueblería Sonora")
        exit()
def consulta_ventas(matriz_ventas):
    """Se presentan las ventas actuales."""
    print("Mueblería Sonora\n") # Imprime la marquesina.
    print("Consulta Ventas")
    tamano = len(matriz_ventas)
    for i in range(tamano):
        pluma = (("{0:<12}   ".format(matriz_ventas[i][0])
                  + "{0:<15}   ".format(matriz_ventas[i][1])
                  + "{0:<20}   ".format(matriz_ventas[i][2])
                  + "{0:<15}   ".format(matriz_ventas[i][3])
                  + "{0:<15}   ".format(matriz_ventas[i][4])
                  + "{0}".format(matriz_ventas[i][5])) + "\n")
        print(pluma)
    print()
    resp = decision_a_menu_principal()
    if resp == 1:
        menu_principal() # Se llama la función de menú principal de nuevo.
    elif resp == 2:
        print("\nGracias por visitar a Mueblería Sonora")
        exit()
def reporte_vendedor(matriz_ventas):
    """Reporte que presenta los ventas del vendedor solicitado."""
    print("Mueblería Sonora\n")
    print("Reporte por Vendedor\n")
    matriz_reportes = [] # Matriz que recolectara los datos de ventas.
    precio_total = 0
    cantidad_total = 0
    nombre = str(input("Ingrese el nombre del vendedor: "))
    comprobacion = nombre.split() # Se crea una lista con el input.
    longitud = len(comprobacion) # Se mide la longitud de la lista.
    
    """Mientras la entrada sea un espacio vacío o más de una
    palabra, rechazará la entrada y pedirá de nuevo el nombre."""
    
    while nombre == "" or longitud == 0 or longitud > 1:
        print("Nombre Inválido")
        nombre = str(input("Ingrese el nombre del vendedor: "))
        comprobacion = nombre.split()
        longitud = len(comprobacion)
    nombre_title = nombre.title()
    size_ventas = len(matriz_ventas) # Obtencion de longitud de matriz_ventas.
    print(("{0:<15}   ".format("ID")
            + "{0:<15}   ".format("Nombre")
            + "{0:<30}   ".format("Apellido")
            + "{0:<15}   ".format("ID_Producto")
            + "{0:<15}   ".format("Precio")
            + "{0}   ".format("Cantidad")+ "\n"))
    for i in range(size_ventas): # Ciclo que recolectará cada venta.
        if nombre_title == matriz_ventas[i][1]:
            matriz_reportes = matriz_ventas[i]
            precio_total = (precio_total
                            + (float(matriz_ventas[i][4])
                            *int(matriz_ventas[i][5])))
            cantidad_total = cantidad_total + int(matriz_ventas[i][5])
            unir_registro = open("reporte_por_vendedor.txt", "a") 
            pluma = (("{0:<15}   ".format(matriz_reportes[0])
                         + "{0:<15}   ".format(matriz_reportes[1])
                         + "{0:<30}   ".format(matriz_reportes[2])
                         + "{0:<15}   ".format(matriz_reportes[3])
                         + "{0:<15}   ".format(matriz_reportes[4])
                         + "{0}".format(matriz_reportes[5]) + "\n"))
            unir_registro.write(pluma)

            print(pluma)
            unir_registro.close() # Se cierra reporte_por_vendedor. 
    # Se abre reporte_por_vendedor para añadir datos.
    reporte_encabezado = open("reporte_por_vendedor.txt", "a")
    # Se escribe la información siguiendo el formato establecido.
    pluma_2 = (("\n{0:<30}   ".format("Total_Cantidad")
                + "{0:<15}   ".format(cantidad_total)
                + "{0:<30}   ".format("Total_Recaudado")
                + "{0:<15}   ".format(precio_total)+ "\n"))
    reporte_encabezado.write(pluma_2)
    print(pluma_2)
    reporte_encabezado.close() # Se cierra el archivo de añadicion.
    resp = decision_a_menu_principal()
    if resp == 1:
        menu_principal() # Se llama la función de menú principal de nuevo.
    elif resp == 2:
        print("Gracias por visitar a Mueblería Sonora")
        exit()
def reporte_producto(matriz_ventas,mat_inv):
    """Reporte que presenta las ventas de un producto especifico."""
    print("Mueblería Sonora\n")
    print("Reportes por producto\n")
    matriz_reporte_producto = [] # Matriz que recolectara los datos de ventas.
    size_inventario = len(mat_inv)
    precio_total = 0
    cantidad_total = 0
    while True: # Este ciclo infinito asegura que se ingrese input válido.
        try: # Permite pedir input y verificar si es integer. 
            id_producto = int(input("Ingrese el ID del producto: "))
            if id_producto <= 0 or id_producto > size_inventario -1:
                print("Número Inválido")
            elif id_producto > 0 and  id_producto <= size_inventario - 1:
                break # Si cumple con la condición, sale del ciclo.
        except: # Si falla en try, except permite que continúe el ciclo.
            print("Número Inválido")
            continue # Acaba la iteración actual y va a la siguiente.
    size_ventas = len(matriz_ventas) # Obtencion de longitud de matriz_ventas.
    print(("{0:<15}   ".format("ID")
            + "{0:<15}   ".format("Modelo")
            + "{0:<15}   ".format("Nombre_Producto")
            + "{0:<15}   ".format("Nombre_Vendedor")
            + "{0:<30}   ".format("Apellido_Vendedor")
            + "{0:<15}   ".format("Precio_Producto")
            + "{0}   ".format("Cantidad")+ "\n"))
    for i in range(size_ventas):
        if str(id_producto) == matriz_ventas[i][3]:
            matriz_reporte_producto = matriz_ventas[i]
            precio_total =( precio_total
                            + (float(matriz_ventas[i][4])
                            *int(matriz_ventas[i][5])))
            cantidad_total = cantidad_total + int(matriz_ventas[i][5])
            unir_registro = open("reporte_productos.txt", "a")
            pluma = (("{0:<15}   ".format(matriz_reporte_producto[0])
                         + "{0:<15}   ".format(mat_inv[id_producto][1])
                         + "{0:<15}   ".format(mat_inv[id_producto][2])
                         + "{0:<15}   ".format(matriz_reporte_producto[1])
                         + "{0:<30}   ".format(matriz_reporte_producto[2])
                         + "{0:<15}   ".format(matriz_reporte_producto[4])
                         + "{0}".format(matriz_reporte_producto[5]) + "\n"))
            unir_registro.write(pluma)

            print(pluma)
            unir_registro.close()
    # Se abre reporte_por_vendedor para añadir datos.
    reporte_encabezado = open("reporte_productos.txt", "a")
    # Se escribe la información siguiendo el formato establecido.
    pluma_2 = (("\n{0:<30}   ".format("Total_Cantidad")
                + "{0:<15}   ".format(cantidad_total)
                + "{0:<30}   ".format("Total_Recaudado")
                + "{0:<15}   ".format(precio_total)+ "\n"))
    reporte_encabezado.write(pluma_2)
    print(pluma_2)
    reporte_encabezado.close() # Se cierra el archivo de añadicion.
    resp = decision_a_menu_principal()
    if resp == 1:
        menu_principal() # Se llama la función de menú principal de nuevo.
    elif resp == 2:
        print("Gracias por visitar a Mueblería Sonora")
        exit()
def encabezado_reporte_vendedor():
    """Si el archivo está vacío, se crea un encabezado."""
    # Se abre reporte_encabezado para escribir.
    reporte_encabezado = open("reporte_por_vendedor.txt", "w")
    # Se escribe la información siguiendo el formato establecido.
    reporte_encabezado.write(("{0:<15}   ".format("ID")
                             + "{0:<15}   ".format("Nombre")
                             + "{0:<30}   ".format("Apellido")
                             + "{0:<15}   ".format("ID_Producto")
                             + "{0:<15}   ".format("Precio")
                             + "{0}   ".format("Cantidad")+ "\n"))

def encabezado_ventas():
    """Si el archivo está vacío, se crea un encabezado."""
    abrir_ventas = open("registro_ventas.txt", "r") # Se abre inventario.txt.
    contenido = abrir_ventas.readline(1) # Lee el caracter uno del archivo.
    abrir_ventas.close() # Se cierra el archivo.
    if contenido != "I": # Si se cumple la condición, se crea el encabezado.
        #Se abre registro_ventas para escribir el encabezado.
        encabezado_ventas = open("registro_ventas.txt", "w")
        # Se escribe la información siguiendo el formato establecido.
        encabezado_ventas.write(("{0:<15}   ".format("ID_Venta")
                                 + "{0:<15}   ".format("Nombre")
                                 + "{0:<30}   ".format("Apellido")
                                 + "{0:<15}   ".format("ID_Producto")
                                 + "{0:<15}   ".format("Precio")
                                 + "{0}   ".format("Cantidad")+ "\n"))

        encabezado_ventas.close() # Se cierra el archivo de escritura.

def encabezado_agregar_productos():
    """Si el archivo está vacío, se crea un encabezado."""
    archivo_entrada = open("inventario.txt", "r") # Se abre el inventario.txt.
    contenido = archivo_entrada.readline(1) # Lee el caracter uno del archivo.
    archivo_entrada.close() # Se cierra el archivo.
    if contenido != "I": # Si se cumple la condición, se crea el encabezado.
        encabezado = open("inventario.txt", "w") # Se abre para escritura.
        # Se escribe la información siguiendo el formato establecido.
        encabezado.write(("{0:<15}   ".format("ID") 
                          + "{0:<15}   ".format("Modelo")
                          + "{0:<30}   ".format("Nombre")
                          + "{0:<15}   ".format("Existencia")
                          + "{0:<15}   ".format("Precio")
                          + "{0}".format("Fecha de llegada")) + "\n")
        encabezado.close() # Se cierra el archivo de escritura.

def encabezado_reporte_producto():
    """Si el archivo está vacío, se crea un encabezado."""
    # Se abre reporte_encabezado para escribir.
    reporte_encabezado = open("reporte_productos.txt", "w") 
    # Se escribe la información siguiendo el formato establecido.
    reporte_encabezado.write((("{0:<15}   ".format("ID")
                               + "{0:<15}   ".format("Modelo")
                               + "{0:<15}   ".format("Nombre_Producto")
                               + "{0:<15}   ".format("Nombre_Vendedor")
                               + "{0:<30}   ".format("Apellido_Vendedor")
                               + "{0:<15}   ".format("Precio_Producto")
                               + "{0}   ".format("Cantidad")+ "\n")))
    reporte_encabezado.close() # Se cierra reporte_por_producto.txt. 

def encabezados_vendedores():
    """Si el archivo está vacío, se crea un encabezado."""
    archivo_entrada = open("vendedores.txt", "r") # Se abre el vendedores.txt.
    contenido = archivo_entrada.readline(1) # Lee el caracter uno del archivo.
    archivo_entrada.close() # Se cierra el archivo.
    if contenido != "I": # Si se cumple la condición, se crea el encabezado.
        encabezado = open("vendedores.txt", "w") # Se abre para escritura.
        # Se escribe la información siguiendo el formato establecido.
        encabezado.write(("{0:<10}   ".format("ID") 
                          + "{0:<15}   ".format("Nombre")
                          + "{0:<30}   ".format("Apellido") + "\n"))
        encabezado.close() # Se cierra el archivo de escritura.
mat_inv = [] # Matriz global que guardará datos del inventario.
matriz_vendedor = [] # Matriz global que guardará datos de cada vendedor.
matriz_ventas = [] # Matriz global que guardara las ventas de los vendedores.
leer_inventario = open("inventario.txt", "r") # Se abre inventario.txt.
for linea in leer_inventario: # Se lee cada línea del archivo.
    linea_inventario = linea.split() # Se guarda cada línea del archivo.
    mat_inv.append(linea_inventario) # Se añade cada línea previa. 
leer_inventario.close() # Se cierra inventario.txt.
leer_vendedor = open("vendedores.txt", "r") # Se abre vendedores.txt.
for linea in leer_vendedor: # Se lee cada línea del archivo.
    linea_vendedor = linea.split() # Se guarda cada línea del archivo.
    matriz_vendedor.append(linea_vendedor) # Se añade cada línea previa.
leer_vendedor.close() # Se cierra vendedores.txt.
leer_ventas = open("registro_ventas.txt", "r") # Se abre registro_ventas.txt.
for linea in leer_ventas: # Se lee cada línea del archivo.
    linea_ventas = linea.split() # Se guarda cada línea del archivo.
    matriz_ventas.append(linea_ventas) # Se añade cada línea previa.
leer_ventas.close() # Se cierra registro_ventas.txt.

menu_principal() # Se llama la función de menu principal.