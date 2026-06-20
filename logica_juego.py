#INFO SECCION
'''Implementa la lógica del juego, como mostrar la habitación actual, mover al jugador, tomar y usar objetos, y procesar comandos,Gestiona el estado del jugador, incluyendo su posición e inventario.'''

# Imports
from datos_juego import habitaciones, objetos_en_habitacion, comandos_validos, salidas, misiones
from estado_jugador import jugador, inventario
from pixel_art import print_image
import textwrap

# FUNCIONES GENERALES:
#No olvidar comentar para q sirve,q necesita y q retorna.
#-Funcion bienvenida
#- Funcion creditos

def ver_ayuda():
  print(" Ayuda ".center(60, "▬"))
  print("Recuerda usar la sintaxis: verbo + objeto.")
  print("Estos son los verbos disponibles:")
  for comando in comandos_validos: #recorrerá el diccionario comandos_validos y mostrarà los comandos disponibles.
    print("•", comando.capitalize())
  print()
#terminada y comprobada
def print_inventario(lst_inventario):  
  '''recibe la lista del inventario e imprime 
  su contenido de manera horizotal en forma de lista'''
  if len(lst_inventario) != 0:
    print()
    print('----elementos en tu inventario:---- \n')
    for objeto in lst_inventario:
      print(f"- {objeto}")
  else:
    print("no tienes ningun elemento en el inventario.")
  print()
#terminada y comprobada
def validar_espacio(comando):
  '''Recibe el comando del usuario y valida que tenga un solo espacio para poder luego hacerle split y que no bote un error, recibe comando del usuario y retorna un booleano'''
  if comando.count(' ') != 1:
    return True  #repetir ciclo hasta que escriba bien
  else:
    return False

#En revision
def procesar_comando(comando, salidas, lst_inventario,list_habitaciones_visitadas,dic_habitaciones,dic_objetos_habitacion):
  '''Funcion que valida y procesa los comandos dado por el usuario, recibe el comando,dic_salidas, lst_inventario, list_Habitaciones_visitadas, dic_habitaciones, dic_objetos_habitacion y su retorno varia dependiendo del comando ingresado por el usuario'''


  if validar_espacio(comando):
    print('-Comando escrito incorrectamente, recuerda usar la sintaxis "Verbo Objeto" ')
    return

  #Una vez verificado que sea un comando escrito corractamente, se procede a separarlo en verbo - objeto para validar cada uno
  verbo, objeto = comando.lower().split(' ')

  if verbo not in comandos_validos:  #verificamos verbo exista en los verbos permitidos, podemos hacerlo directamente con las keys del diccionario de comandos_validos
    print(f'Verbo -{verbo}- no reconocido')
    return

  if objeto not in comandos_validos[
      verbo]:  #verifica que el objeto exista entre todos los objetos
    print(f'-{objeto}- no reconocido')
    return

  if objeto not in comandos_validos[
      verbo]:  #verifica que el verbo vaya de acuerdo al objeto
    print(f"-Comando invalido-")
    print(f"Piensas -{verbo}- {objeto}?... ")
    return

  #---------pasamos a hacer las acciones de acuerdo al verbo-------

  if verbo == 'ir':
    recorrer(objeto, salidas, jugador,list_habitaciones_visitadas,dic_habitaciones)

    # validar si la habitacion es la misma que la anterior(osea no se movio) -> no mostrar la ubicacion
    #en casa deq no si mostrar la ubicacion
    mostrar_ubicacion(habitaciones, salidas, jugador,dic_objetos_habitacion)  #muestra los detalles de la nueva habitacion
  elif verbo == 'recoger':

    if validar_objeto_existente(objeto,jugador['posicion']):
      habitacion_actual = jugador['posicion']
      inventario.append(objeto)
      print(f'Se ha recogido "{objeto}".')
      print()

      #VERIFICARRRR
      objetos_en_habitacion[habitacion_actual].remove(objeto)   #eliminar el objeto de la lista de objetos en habitacion
    else:
      print(f'El objeto "{objeto}" no se encuentra en la habitación.')
      print()
      
  elif objeto == 'ayuda':
    return ver_ayuda()  #Funcion que muestre los verbos disponible a usar y la sintaxis

  elif objeto == 'inventario':
    return print_inventario(lst_inventario)  #Funcion que muestre el inventario del jugador

  elif objeto == 'misiones':
    return mostrar_misiones(misiones)

  elif objeto == 'juego':  #comprobar
      salir_juego(jugador)
  else:
    print('-Comando invalido-')


def validar_objeto_existente_inventario(objeto, inventario):
  '''Valida si el objeto a usar se encuentra en el inventario del jugador.'''
  if objeto in inventario:
    return True
  else:
    return False
#terminada y comprobada
def validar_direccion(direccion, dic_salidas, dic_jugador,list_habitaciones_visitadas, dic_habitaciones):
  '''valida que la direccion cardinal dada por el jugador este disponible en la habitacion actual, 
  recibe la direccion, el diccionario de salidas y el diccionario del jugador, retorna un booleano'''
  posicion_actual = dic_jugador['posicion']
  habitacion_actual = dic_habitaciones[posicion_actual]['nombre'] # nombre de la habitacion actual
  if direccion in dic_salidas[posicion_actual]:
    list_habitaciones_visitadas.append(habitacion_actual) #agrega el nombre de la habitacion actual a la     lista de habitaciones visitadas
    return True
  else:
    return False

#terminada y comprobada(falta pulir algo por Alan)
def recorrer(direccion, salidas, jugador, list_habitaciones_visitadas,dic_habitaciones):
  '''valida la direccion con otra funcion, si la direccion es correcta
    actualizara directamente la variable de la posicion del jugador, 
    en caso de que no avisa al jugador del error,Pide direccion escrita por el jugador, 
    el diccionario de salidas para validar  y el diccionario jugador para obtener y actualizar
    la posicion'''

  if validar_direccion(direccion, salidas,jugador,list_habitaciones_visitadas, dic_habitaciones):  #validamos que la direccion exista en la habitacion
    posicion_actual = jugador['posicion']
    num_nueva_habitacion = salidas[posicion_actual][direccion]  #guardamos el numero de la habitacion que se movera
    jugador['posicion'] = num_nueva_habitacion  #actualizamos la posicion en la que se encontraba.(se movio)
    modificador_tiempo(jugador)

  else:
    print(f"La direccion colocada no existe en la habitacion!")

#terminada y comprobada
def modificador_tiempo(jugador):
  '''Funcion que modifica el tiempo conforme el jugador se mueve en las habitaciones,
  solo modifica, no retorna.'''
  jugador['tiempo'] -= 2 #por cada habitacion que se mueva se va restar 2 'minutos' al tiempo

def validar_objeto_existente(objeto, posicion):
  '''Valida si el objeto a recoger se encuentra en la habitación en la que está el jugador.'''
  if objeto in objetos_en_habitacion[posicion]:
    return True
  else:
    return False

def mostrar_descripcion_objeto(dic_objetos_descripciones, dic_jugador):
  habitacion_actual = dic_jugador['posicion']
  for objeto, lst_descripcion in dic_objetos_descripciones[habitacion_actual].items():
    if not lst_descripcion[0]:
      print(f'*{lst_descripcion[1]}*')

def verificar_7_misiones(dic_misiones):
  '''Esta funcion verificara constantemente que se hayan realizado las 7 misiones previa
  a la 14(de escapar), devolvera un booleano?'''
  vrf_mision1 = dic_misiones[1]['bool']
  vrf_mision2 = dic_misiones[2]['bool']
  vrf_mision3 = dic_misiones[3]['bool']
  vrf_mision4 = dic_misiones[4]['bool']
  vrf_mision7 = dic_misiones[7]['bool']
  vrf_mision10 = dic_misiones[10]['bool']
  vrf_mision13 = dic_misiones[13]['bool']

  if vrf_mision1 and vrf_mision2 and vrf_mision3 and vrf_mision4 and vrf_mision7 and vrf_mision10 and vrf_mision13:
    return True #retorna True dando paso a que el usuario pueda realizar la funcion 14(escapar)
  else:
    return False #no da paso a ejecutar la funcion 14(escapar)

def salir_juego(dic_jugador):
  dic_jugador['salir'] = True
  

#FUNCIONES Q DEVUELVEN INFORMACION(estado del jugador,posicion, inventario,etc):

#terminada y comprobada
def mostrar_ubicacion(dic_habitaciones, dic_salidas, dic_jugador,dic_objetos_habitacion):
  '''Muestra la ubicación actual del jugador y las salidas disponibles.Recibe diccionario de habitaciones,
  dic de salidas y dic del estado del jugador.No Retorna solo imprime'''
  posicion_actual = dic_jugador['posicion']
  print_image(f"{dic_habitaciones[posicion_actual]['imagen']}") #imprime la imagen del cuarto
  print(f"⌈Tiempo disponible: {dic_jugador['tiempo']} min.⌋")
  print("Te encuentras en:\n\n",f" {dic_habitaciones[posicion_actual]['nombre']} ".center(80,'▬'),sep='')
  print(textwrap.fill(f"{dic_habitaciones[posicion_actual]['descripcion']} \n",width = 80))
  print()
  if len(dic_objetos_habitacion[posicion_actual]) > 0:  #muestra los objetos en la habitacion
    print(f"En esta habitación puedes ver: ")
    for objeto in dic_objetos_habitacion[posicion_actual]:
      print(f"- {objeto}")
    print()
  print(f"\nSalidas disponibles:\n")
  salidas_habitacion = dic_salidas[posicion_actual]
  for direccion, habitacion in salidas_habitacion.items():
    print(f"- {direccion.capitalize()} ({dic_habitaciones[habitacion]['nombre']})")
  print()
  
def mostrar_misiones(dic_misiones):
  print('Misiones disponibles'.center(50, '='))
  for num_mision, dic_detalles in dic_misiones.items():
    if num_mision in [1, 2, 10, 13, 14, 3, 4, 7] and not dic_detalles['bool']:     #colocar el num de las misiones obligatorias en las lista aqui
      print(f"▰ {dic_detalles['nombre']} (obligatoria)")
    elif not dic_detalles['bool']:
      print(f"▰ {dic_detalles['nombre']}")
  print()


#--------------misiones-----------------

#-----------------Misión 1: Restaurar el Soporte Vital-------------------
def restaurar_soporte_vital(lst_inventario,dic_jugador, dic_misiones): #devuelve un bool false o true para que no se vuelva a repetir una vez ya hecha
  
  posicion_actual = dic_jugador['posicion'] #int
  objetos_necesarios = dic_misiones[1]['objetos_necesarios'] # list
  descripcion = dic_misiones[1]['descripcion'] #str
  
  if (dic_misiones[1]['bool'] == False) and (posicion_actual == 10): #--------LLLLLL

    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()
      
    if usr1 == 'si':
      usr = input('Ingresa "restaurar" para realizar la mision:  ').lower().strip()
      while usr != 'restaurar':
        print()
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "restaurar" para realizar la mision.. ').lower().strip()
        print()

      if (objetos_necesarios[0] not in lst_inventario) or (objetos_necesarios[1] not in lst_inventario):
        print()
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('Reune los objetos necesarios para poder cumplir la mision')
        print()
      else:
        print('Has reparado el sistema de soporte vital..')
        print()
        dic_misiones[1]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()

  return dic_misiones[1]['bool']  

    
    
#----------------------- Misión 2: Estabilizar el Control de Energía--------------------
def estabilizar_control_energia(lst_inventario,dic_jugador, dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[2]['objetos_necesarios']
  descripcion = dic_misiones[2]['descripcion']

  if (dic_misiones[2]['bool'] == False) and posicion_actual == 28:
    
    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "estabilizar" para realizar la mision: ').lower().strip()
      while usr != 'estabilizar':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "estabilizar" para realizar la mision.. ').lower().strip()
        
      if (objetos_necesarios[0] not in lst_inventario) or (objetos_necesarios[1] not in lst_inventario) or (objetos_necesarios[2] not in lst_inventario) or (objetos_necesarios[3] not in lst_inventario):
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('reune los objetos necesarios para poder cumplir la mision.. ')
      else:
        print('Has reparado el sistema de control de energía..')
        print()
        dic_misiones[2]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()
      
  return dic_misiones[2]['bool']

#----------------Misión 3: Reiniciar el Sistema de Comunicaciones-------------
def reiniciar_sistema_comunicaciones(lst_inventario,dic_jugador, dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[3]['objetos_necesarios']
  descripcion = dic_misiones[3]['descripcion']

  if (dic_misiones[3]['bool'] == False) and (posicion_actual == 7):
    
    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "reiniciar" para realizar la mision: ').lower().strip()
      while usr != 'reiniciar':
        print('-Palabra incorrecta')
        usr1 = input('Ingresa correctamente la palabra: "reiniciar" para realizar la mision.. ').lower().strip()
        
      if (objetos_necesarios[0] not in lst_inventario) or (objetos_necesarios[1] not in lst_inventario):
        print('No tienes los objetos necesarios para cumplir esta mision.. ')
        print('reune los objetos necesarios para poder cumplir la mision')
      else:
        print('Has reiniciado el sistema de comunicaciones..')
        dic_misiones[3]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()
      
  return dic_misiones[3]['bool']

#---------------Misión 4: Desactivar el Sistema de Seguridad del Laboratorio Químico------------------
def desactivar_sistema_seguridad_laboratorio_quimico(lst_inventario,dic_jugador, dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[4]['objetos_necesarios']
  descripcion = dic_misiones[4]['descripcion']

  if (dic_misiones[4]['bool'] == False) and (posicion_actual == 5):
    
    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "desactivar" para realizar la mision: ').lower().strip()
      while usr != 'desactivar':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "desactivar" para realizar la mision.. ').lower().strip()

      if (objetos_necesarios[0] not in lst_inventario) or (objetos_necesarios[1] not in lst_inventario):
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('reune los objetos necesarios para poder cumplir la mision')
      else:
        print('Has desactivado el sistema de seguridad del laboratorio químico..')
        dic_misiones[4]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()
      
  return dic_misiones[4]['bool']

# --------------------Misión 5: Obtener Información del Laboratorio Biológico-------------
def obtener_informacion_laboratorio_biologico(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[5]['objetos_necesarios']
  descripcion = dic_misiones[5]['descripcion']

  if (dic_misiones[5]['bool'] == False) and (posicion_actual == 3):

    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "obtener" para realizar la mision: ').lower().strip()
      while usr != 'obtener':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "obtener" para realizar la mision.. ').lower().strip()

      if (objetos_necesarios[0] not in lst_inventario) :
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('reune los objetos necesarios para poder cumplir la mision')
      else:
        print('Has recolectado la información del laboratorio biológico..')
        dic_misiones[5]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()
      
  return dic_misiones[5]['bool']

#--------------Misión 6: Recuperar Herramientas Esenciales-----------------
def recuperar_herramientas_esenciales(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[6]['objetos_necesarios']
  descripcion = dic_misiones[6]['descripcion']
  
  if (dic_misiones[6]['bool'] == False) and (posicion_actual == 30):

    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "recuperar" para realizar la mision: ').lower().strip()
      while usr != 'recuperar':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "recuperar" para realizar la mision.. ').lower().strip()

      if (objetos_necesarios[0] not in lst_inventario) or (objetos_necesarios[1] not in lst_inventario):
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('reune los objetos necesarios para poder cumplir la mision')
      else:
        print('Has recuperado herramientas esenciales para futuras reparaciones..')
        dic_misiones[6]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()
      
  return dic_misiones[6]['bool']

#-------------Misión 7: Reparar el Sistema de Propulsión-----------------
def reparar_sistema_propulcion(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[7]['objetos_necesarios']
  descripcion = dic_misiones[7]['descripcion']

  if (dic_misiones[7]['bool'] == False) and (posicion_actual == 26):
    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "reparar" para realizar la mision: ').lower().strip()
      while usr != 'reparar':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "reparar" para realizar la mision.. ').lower().strip()

      if (objetos_necesarios[0] not in lst_inventario) or (objetos_necesarios[1] not in lst_inventario):
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('reune los objetos necesarios para poder cumplir la mision')
      else:
        print('Has reparado el sistema de propulsión..')
        dic_misiones[7]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()
      
  return dic_misiones[7]['bool']

#------------Misión 8: Recuperar la Tarjeta de Acceso del Capitán---------------
def recuperar_tarjeta_acceso_capitan(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[8]['objetos_necesarios']
  descripcion = dic_misiones[8]['descripcion']

  if (dic_misiones[8]['bool'] == False) and (posicion_actual == 11):

    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "recuperar" para realizar la mision: ').lower().strip()
      while usr != 'recuperar':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "recuperar" para realizar la mision.. ').lower().strip()

      if (objetos_necesarios[0] not in lst_inventario) or (objetos_necesarios[1] not in lst_inventario):
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('reune los objetos necesarios para poder cumplir la mision')
      else:
        print('Has recuperado la tarjeta de acceso del capitán..')
        dic_misiones[8]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()
      
  return dic_misiones[8]['bool']

#----------------Misión 9: Investigar el Módulo de Control--------------------
def investigar_modulo_control(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  descripcion = dic_misiones[9]['descripcion']

  if (dic_misiones[9]['bool'] == False) and (posicion_actual == 2):

    print('Tienes una mision por hacer..')
    print(descripcion)
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "investigar" para realizar la mision: ').lower().strip()
      while usr != 'investigar':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "investigar" para realizar la mision.. ').lower().strip()

      print()
      print('Al momento de investigar el modulo de control has activado una alarma y la Sala de robots ahora está activa… Los robots están descontrolados, comienzan a moverse y esto es una amenaza inminente para ti')
      print()
      
      dic_misiones[9]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()
      
  return dic_misiones[9]['bool']

#----------------Misión 10: Enfrentar la Amenaza en la Sala de Robots-------------
def enfrentar_amenaza_sala_robots(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[10]['objetos_necesarios']
  descripcion = dic_misiones[10]['descripcion']

  if (dic_misiones[10]['bool'] == False) and (posicion_actual == 29):

    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "enfrentar" para realizar la mision: ').lower().strip()
      while usr != 'enfrentar':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "enfrentar" para realizar la mision.. ').lower().strip()

      if (objetos_necesarios[0] not in lst_inventario) or (objetos_necesarios[1] not in lst_inventario):
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('reune los objetos necesarios para poder cumplir la mision')
      else:
        print('Has enfrentado la amenaza en la sala de robots, estas a salvo, por ahora...')
        dic_misiones[10]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()
      
  return dic_misiones[10]['bool']

#---------------Misión 11: Investigar el Área de Experimentos----------------------
def investigar_area_experimentos(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  descripcion = dic_misiones[11]['descripcion']

  if (dic_misiones[11]['bool'] == False) and (posicion_actual == 22):

    print('Tienes una mision por hacer..')
    print(descripcion)
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "investigar" para realizar la mision: ').lower().strip()
      while usr != 'investigar':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "investigar" para realizar la mision.. ').lower().strip()

      print()
      print('has investigado el area de experimentos')
      dic_misiones[11]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()

  return dic_misiones[11]['bool']

#---------------Misión 12: Reunir la Información Final------------------------
def reunir_informacion_final(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[12]['objetos_necesarios']
  descripcion = dic_misiones[12]['descripcion']

  if (dic_misiones[12]['bool'] == False) and (posicion_actual == 35):

    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "reunir" para realizar la mision: ').lower().strip()
      while usr != 'reunir':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "reunir" para realizar la mision.. ').lower().strip()

      if (objetos_necesarios[0] not in lst_inventario):
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('reune los objetos necesarios para poder cumplir la mision')
      else:
        print('Al momento de investigar lograste ver una nota, donde se ve un código de acceso..')
        dic_misiones[12]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()

  return dic_misiones[12]['bool']

#---------------Misión 13: Reparar el Sistema de Estabilización-------------
def reparar_sistema_estabilizacion(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[13]['objetos_necesarios']
  descripcion = dic_misiones[13]['descripcion']

  if (dic_misiones[13]['bool'] == False) and (posicion_actual == 24):

    print('Tienes una mision por hacer..')
    print(descripcion)
    print(f'Para completar esta mision debes tener los siguientes objetos: ')
    for objeto in objetos_necesarios:
      print(f'+ {objeto}')
    print()

    usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
    while usr1 != 'si' and usr1 != 'no':
      print('-Palabra incorrecta')
      usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
      print()

    if usr1 == 'si':
      usr = input('Ingresa "reparar" para realizar la mision: ').lower().strip()
      while usr != 'reparar':
        print('-Palabra incorrecta')
        usr = input('Ingresa correctamente la palabra: "reparar" para realizar la mision.. ').lower().strip()

      if (objetos_necesarios[0] not in lst_inventario) or (objetos_necesarios[1] not in lst_inventario):
        print('No tienes los objetos necesarios para cumplir esta mision..')
        print('reune los objetos necesarios para poder cumplir la mision')
      else:
        print('Has recuperado herramientas esenciales para futuras reparaciones..')
        dic_misiones[13]['bool'] = True
    else:
      print(f'Has decidido no completar la mision.')
      print()

  return dic_misiones[13]['bool']

#-------------------Misión 14: Escapar de la Estación-------------------------
def escapar_estacion(lst_inventario,dic_jugador,dic_misiones):
  posicion_actual = dic_jugador['posicion']
  objetos_necesarios = dic_misiones[14]['objetos_necesarios']
  descripcion = dic_misiones[14]['descripcion']

  if (dic_misiones[14]['bool'] == False) and (posicion_actual == 32): #A
    if verificar_7_misiones(misiones):

      print('Tienes una mision por hacer..')
      print(descripcion)
      print(f'Para completar esta mision debes tener los siguientes objetos: ')
      for objeto in objetos_necesarios:
        print(f'+ {objeto}')
      print()
  
      usr1 = input('¿Quieres completar la mision? (si/no): ').lower().strip()
      while usr1 != 'si' and usr1 != 'no':
        print('-Palabra incorrecta')
        usr1 = input('Ingresa correctamente la palabra: "si" o "no": ').lower().strip()
        print()
  
      if usr1 == 'si':
        usr = input('Ingresa "escapar" para realizar la mision: ').lower().strip()
        while usr != 'escapar':
          print('-Palabra incorrecta')
          usr = input('Ingresa correctamente la palabra: "escapar" para realizar la mision.. ').lower().strip()
  
        if (objetos_necesarios[0] not in lst_inventario):
          print('No tienes los objetos necesarios para cumplir esta mision..')
          print('reune los objetos necesarios para poder cumplir la mision')
        else:
          print('Has recuperado herramientas esenciales para futuras reparaciones..')
          dic_misiones[14]['bool'] = True
      else:
        print(f'Has decidido no completar la mision.')
        print()
    else:
      print('Aqui esta la capsula de escape!, completa la 7 misiones obligatorias para poder activar la mision final de "escapar"')
  
  return dic_misiones[14]['bool']

#funcion donde se van a ejecutar las misiones dentro del bucle principal 
#falta hacerla bien xd 
# def ejecutar_misiones(lst_inventario,dic_jugador,dic_misiones):
#   #mision 1  --obligatoria --
#   if restaurar_soporte_vital(lst_inventario,dic_jugador,dic_misiones):
#     #mision 2  --obligatoria --
#     if estabilizar_control_energia(lst_inventario,dic_jugador,dic_misiones):
#       #mision 3  --obligatoria --
#       if reiniciar_sistema_comunicaciones(lst_inventario,dic_jugador,dic_misiones):
#         #mision 6  --obligatoria --
#         if recuperar_herramientas_esenciales(lst_inventario,dic_jugador,dic_misiones):
#           #mision 7  --obligatoria --
#           if reparar_sistema_propulcion(lst_inventario,dic_jugador,dic_misiones):
#             #mision 8  --obligatoria --
#             if recuperar_tarjeta_acceso_capitan(lst_inventario,dic_jugador,dic_misiones):
#               #mision 9  --obligatoria --
#               if investigar_modulo_control(lst_inventario,dic_jugador,dic_misiones):
#                 #mision 10  --obligatoria --
#                 if enfrentar_amenaza_sala_robots(lst_inventario,dic_jugador,dic_misiones):
#                   #mision 12  --obligatoria --
#                   if reunir_informacion_final(lst_inventario,dic_jugador,dic_misiones):
#                     #mision 13  --obligatoria --
#                     if reparar_sistema_estabilizacion(lst_inventario,dic_jugador,dic_misiones):
#                       #mision 14  --obligatoria --
#                       if escapar_estacion(lst_inventario,dic_jugador,dic_misiones):
#                         mensaje = 'escapaste de la nave, felicidades. :)'
#                         return mensaje
  

# se puede seguir casi la misma estructura como:
# sacar la posicion(int), objetos necesararios(list), descripcin(str)
# verificar que la mision no se haya hecho antes
#verificar la posicion de del jugador concuerde con la habitacion de la mision e imprimir la descripcion de la mision
# el usr(pedir al usuario escribir algo para ejecutar la mision) y verificarlo para evitar que se caiga el juego
# verificar que tenga los objetos necesarios 
# retornar el True cuando cumpla la mision