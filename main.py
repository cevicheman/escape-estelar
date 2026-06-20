#Punto de entrada del juego, donde se ejecutara el bucle principal

#imports:
import time
from datos_juego import habitaciones, objetos_en_habitacion, comandos_validos, salidas, misiones
import logica_juego as lg
from estado_jugador import jugador, inventario, habitaciones_visitadas
import z_extras as ex

#PREVIA DEL JUEGO
print(f"Bienvenido al juego!")
ex.bienvenida()

#INICIO DEL JUEGO
lg.mostrar_ubicacion(habitaciones, salidas, jugador, objetos_en_habitacion)

while not (misiones[14]['bool']) and jugador['tiempo'] > 0 and not (
        jugador['salir']):
    comando = input("> ")

    lg.procesar_comando(comando, salidas, inventario, habitaciones_visitadas, habitaciones, objetos_en_habitacion)

    #misiones
    lg.restaurar_soporte_vital(inventario, jugador, misiones)
    lg.estabilizar_control_energia(inventario, jugador, misiones)
    lg.reiniciar_sistema_comunicaciones(inventario, jugador, misiones)
    lg.desactivar_sistema_seguridad_laboratorio_quimico(
        inventario, jugador, misiones)
    lg.obtener_informacion_laboratorio_biologico(inventario, jugador, misiones)
    lg.recuperar_herramientas_esenciales(inventario, jugador, misiones)
    lg.reparar_sistema_propulcion(inventario, jugador, misiones)
    lg.recuperar_tarjeta_acceso_capitan(inventario, jugador, misiones)
    lg.investigar_modulo_control(inventario, jugador, misiones)
    lg.enfrentar_amenaza_sala_robots(inventario, jugador, misiones)
    lg.investigar_area_experimentos(inventario, jugador, misiones)
    lg.reunir_informacion_final(inventario, jugador, misiones)
    lg.reparar_sistema_estabilizacion(inventario, jugador, misiones)
    lg.escapar_estacion(inventario, jugador, misiones)

#FINAL JUEGO
if jugador['tiempo'] <= 0:
    print('**************'.center(50, '='))
    print('''⌈ El reloj marca el final ⌋.
        Mientras luchas por abrirte camino a través del oscuro corredor de la nave,
        una vibración intensa sacude todo a tu alrededor.
        La nave rechina y cruje como si estuviera viva, sus sistemas fallando uno tras otro. 
        Las luces parpadean violentamente, y el zumbido constante de la alarma de emergencia se corta en 
        un silencio inquietante.
        La estacion se ha destruido...''')
    time.sleep(7)
    ex.print_gameOver()
elif misiones[14]['bool']:
    print('**************'.center(50, '='))
    print('''⌈ Lo lograstes! ⌋. 
        Después de una serie de desafíos agotadores y momentos en los que todo parecía perdido,
        te encuentras finalmente dentro de la cápsula de escape. El eco de las explosiones y 
        los crujidos de la estación espacial a punto de colapsar aún retumban en tus oídos. 
        Con manos temblorosas, introduces el código de activación que has luchado por encontrar. 
        La pantalla de la cápsula parpadea, mostrando las coordenadas correctas.
        Observas la inmesidad del oceano terrestre desde la ventana de tu capsula
        Estás a salvo. Has sobrevivido.''')
    time.sleep(7)
    ex.print_gameOver()
elif jugador['salir']:
    print('Has salido del juego...')
