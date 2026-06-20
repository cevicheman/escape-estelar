#Funciones extras a agregar, sonido, imagenes ,tiempo, etc.

#- Funcion del tiempo
import logica_juego as lg



def bienvenida():
  '''Da la buenvenida al juego,solo imprime'''

  print('''
 ______   ______  ______  ______  ______  ______    
/\  ___\ /\  ___\/\  ___\/\  __ \/\  == \/\  ___\   
\ \  __\ \ \___  \ \ \___\ \  __ \ \  _-/\ \  __\   
 \ \_____ \/\_____\ \_____\ \_\ \_\ \_\   \ \_____\ 
  \/_____/ \/_____/\/_____/\/_/\/_/\/_/    \/_____/ 
'''.center(150))

  print('''
 ______   ______  ______  ______   __      ______  ______    
/\  ___\ /\  ___\/\__  _\/\  ___\ /\ \    /\  __ \/\  == \   
\ \  __\ \ \___  \/_/\ \/\ \  __\ \ \ \___\ \  __ \ \  __<   
 \ \_____\ /\_____\ \ \_\ \ \_____ \ \_____\ \_\ \_\ \_\ \_\ 
  \/_____/ \/_____/  \/_/  \/_____/ \/_____/\/_/\/_/\/_/ /_/ 

'''.center(300))
  print(
      '''‖ Bienvenido a escape Estelar!, recuerda leer el manual de la historia y 
de uso del juego.''')
  lg.ver_ayuda()
  print('⌂ Para ayuda durante la ejecucion, escribe "Ver ayuda" ')
  print('⌂ Para ver inventario durante la ejecucion, escribe "Ver inventario" ')
  print('⌂ Para ver durante la ejecucion las misiones disponibles, escribe "Ver misiones" ')
  print('⌂ Escribe "salir juego" para finalizar la ejecucion')
  print('suerte... \n')
  input('Press Enter to start...')
  #pagina de text-art -> https://patorjk.com/software/taag/#p=display&h=2&v=1&f=Sub-Zero&t=Escape
  #fuente -> subzero con Width 'Smush(R)'

def print_gameOver():
  '''Imprime el mensaje de game over, solo imprime'''
  print(''' 
 ______  ______  __    __  ______    
/\  ___\/\  __ \/\ "-./  \/\  ___\   
\ \ \__ \ \  __ \ \ \-./\ \ \  __\   
 \ \_____\ \_\ \_\ \_\ \ \_\ \_____\ 
  \/_____/\/_/\/_/\/_/  \/_/\/_____/ ''')
  print(''' 
 ______  __   ________  ______    
/\  __ \/\ \ / /\  ___\/\  == \   
\ \ \/\ \ \ \'/\ \  __\\ \  __<   
 \ \_____\ \__/ \ \_____\ \_\ \_\ 
  \/_____/\/_/   \/_____/\/_/ /_/ 
  ''')

#Apuntes Alan
#2 .- modificar misiones que sumen tiempo al contador