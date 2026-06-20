#INFO SECCION
'''Contiene todas las estructuras de datos, como habitaciones, objetos, comandos, salidas,etc .'''
#imports

#Estructuras de datos:
habitaciones = {
    1: {
        'nombre': 'Módulo de descanso',
        'descripcion':
        'Las luces parpadean suavemente, y el aire se siente denso y opresivo. El eco de tus pasos resuena de manera inquietante, haciendo que cada sombra se alargue y cobre vida, como si algo invisible estuviera acechando en las esquinas. Las paredes muestran grietas y pequeños escombros flotan en el aire, aumentando la sensación de claustrofobia.',
        'imagen': 'imagenescuartos/Modulo de descanso.webp'
    },
    2: {
        'nombre': 'Módulo de control',
        'descripcion':
        'Las consolas están cubiertas de polvo y las pantallas emiten una estática perturbadora. Los monitores rotos reflejan tu imagen de forma distorsionada, como si algo desconocido estuviera observándote desde el otro lado, esperando su momento. Fragmentos de metal y cables sueltos cuelgan del techo, creando chispas ocasionales que iluminan la sala de forma aterradora.',
        'imagen': 'imagenescuartos/Módulo de control.webp'
    },
    3: {
        'nombre': 'Módulo de laboratorio biológico',
        'descripcion':
        'Frascos llenos de líquidos burbujeantes emiten un brillo siniestro en la penumbra, mientras especímenes extraños parecen moverse ligeramente bajo la tenue luz. Un escalofrío recorre tu espalda al darte cuenta de que no estás solo en esta sala. El techo presenta brechas por las que se filtra un leve y frío silbido, lo que contribuye a la atmósfera inquietante.',
        'imagen': 'imagenescuartos/Módulo de laboratorio biológico.webp'
    },
    4: {
        'nombre': 'Invernadero',
        'descripcion':
        'La vegetación es tan densa que parece asfixiarte, susurrando en un lenguaje desconocido con cada leve brisa. Las sombras de las plantas se mueven como si tuvieran voluntad propia, y una bruma extraña en el aire hace que cada respiro sea un desafío. Algunas partes del techo han caído, dejando entrar una luz tenue y fragmentada que proyecta sombras irregulares.',
        'imagen': 'imagenescuartos/Invernadero.webp'
    },
    5: {
        'nombre': 'Módulo de laboratorio químico',
        'descripcion':
        'Frascos y tubos de ensayo están desparramados por todas partes, creando una sensación de caos. Un olor acre y penetrante llena el ambiente, y las sombras que proyecta la luz parpadeante parecen danzar macabramente a tu alrededor. Las paredes muestran manchas quemadas y grietas, haciendo que te preguntes cuánto tiempo más podrá soportar este módulo.',
        'imagen': 'imagenescuartos/Módulo de laboratorio químico.webp'
    },
    6: {
        'nombre': 'Módulo de laboratorio físico',
        'descripcion':
        'Equipos y maquinarias permanecen apagados, envueltos en un silencio absoluto. Cada paso que das resuena como un trueno, y la sensación de estar en un lugar prohibido y olvidado se intensifica con cada movimiento. Un agujero en la pared permite ver el vasto y oscuro espacio exterior, recordándote lo frágil que es la estructura de la estación.',
        'imagen': 'imagenescuartos/Módulo de laboratorio físico.webp'
    },
    7: {
        'nombre': 'Módulo de comunicaciones',
        'descripcion':
        'Cables colgando del techo y pantallas rotas te rodean. Un mensaje incompleto parpadea en una pantalla, creando una sensación de urgencia y desesperación mientras intentas descifrarlo. Varias conexiones están cortadas, y un leve chisporroteo emana de los paneles de control, haciéndote dudar de la posibilidad de enviar un mensaje de socorro.',
        'imagen': 'imagenescuartos/Módulo de comunicaciones.webp'
    },
    8: {
        'nombre': 'Módulo de almacenamiento',
        'descripcion':
        'Cajas y contenedores sellados llenan el espacio. Cada crujido y eco de tus pasos reverbera en el vacío, y la sensación de paranoia se intensifica con cada rincón oscuro que exploras. Algunos contenedores están abiertos, con su contenido derramado por el suelo, creando un desorden que dificulta saber qué es útil y qué está dañado.',
        'imagen': 'imagenescuartos/Módulo de almacenamiento.webp'
    },
    9: {
        'nombre': 'Módulo de mantenimiento',
        'descripcion':
        'Estás en el Módulo de mantenimiento. Herramientas dispersas y luces intermitentes te rodean. El olor a aceite y metal caliente es penetrante, y parece que alguien ha dejado el trabajo a medio terminar en medio de una prisa desesperada. Algunas piezas de la estación están colapsadas o dobladas, como si se hubiera intentado reparar algo sin éxito.',
        'imagen': 'imagenescuartos/Módulo de mantenimiento.webp'
    },
    10: {
        'nombre': 'Módulo de soporte vital',
        'descripcion':
        'El sonido constante de los sistemas de respiración y el brillo frío de las luces de emergencia crean un ambiente claustrofóbico, haciendo que cada respiro parezca un esfuerzo titánico. Fisuras en las paredes dejan escapar un débil pero constante silbido de aire, aumentando la presión de encontrar una solución rápidamente.',
        'imagen': 'imagenescuartos/Módulo de soporte vital.webp'
    },
    11: {
        'nombre': 'Habitación 1H (del capitán)',
        'descripcion':
        'Los muebles están cubiertos de polvo y las ventanas son opacas. Un diario abierto en la mesa muestra una última entrada desesperada, y la sensación de abandono es abrumadora. El techo presenta grietas y algunas pertenencias están esparcidas por el suelo, como si hubieran caído durante un temblor.',
        'imagen': 'imagenescuartos/Habitación 1H (del capitán).webp'
    },
    12: {
        'nombre': 'Módulo de observación',
        'descripcion':
        'La vista del espacio exterior es impresionante, pero el vasto vacío negro te hace sentir insignificante y vulnerable. Algo en la oscuridad parece acechar, esperando el momento adecuado para mostrarse. Las ventanas están parcialmente fracturadas, dejando ver pequeñas fisuras por las que se filtran rayos de luz, dándole un aspecto aún más siniestro.',
        'imagen': 'imagenescuartos/Módulo de observación.webp'
    },
    13: {
        'nombre': 'Módulo de cocina',
        'descripcion':
        'El desorden es total, con restos de comida y utensilios abandonados por todas partes. El goteo constante de un grifo roto es el único sonido, creando un ritmo inquietante que resuena en el silencio. Parte de las estanterías están rotas, y algunas latas y paquetes de comida están esparcidos por el suelo, aplastados y en mal estado.',
        'imagen': 'imagenescuartos/Módulo de cocina.webp'
    },
    14: {
        'nombre': 'Comedor',
        'descripcion':
        'Las mesas y sillas están volcadas, y la sensación de abandono es palpable. Las sombras parecen moverse en las esquinas de tu visión, creando una atmósfera de suspenso y temor. El techo muestra signos de colapso parcial, y algunos escombros flotan en el aire, añadiendo a la atmósfera ya tensa.',
        'imagen': 'imagenescuartos/Comedor.webp'
    },
    15: {
        'nombre': 'Gimnasio',
        'descripcion':
        'Las máquinas de ejercicio están cubiertas de polvo y el aire es pesado. El silencio absoluto hace que cada movimiento y sonido resuene más de lo esperado, aumentando la sensación de soledad. Algunas piezas del equipo están fuera de lugar, y un pequeño agujero en la pared permite ver la vastedad del espacio exterior.',
        'imagen': 'imagenescuartos/Gimnasio.webp'
    },
    16: {
        'nombre': 'Vestuarios',
        'descripcion':
        'Los casilleros abiertos y las toallas desechadas crean una atmósfera de abandono. El sonido de una gota de agua cayendo ecoa sin fin, añadiendo un ritmo constante a la inquietud del lugar. La humedad en el aire ha empeorado, y el goteo constante parece marcar el tiempo en un ambiente ya cargado de tensión.',
        'imagen': 'imagenescuartos/Vestuarios.webp'
    },
    17: {
        'nombre': 'Sala de reuniones',
        'descripcion':
        'Las sillas están desordenadas y documentos esparcidos por la mesa. Las luces parpadean, creando un juego de sombras que te pone los pelos de punta y una sensación de ser observado. Las paredes tienen grietas significativas, y una de las ventanas muestra una fisura que añade al ambiente tenso de la sala.',
        'imagen': 'imagenescuartos/Sala de reuniones.webp'
    },
    18: {
        'nombre': 'Módulo médico',
        'descripcion':
        'Equipos médicos obsoletos y camas deshechas te rodean. El olor a desinfectante es penetrante, y los instrumentos quirúrgicos brillan siniestros bajo la luz tenue, como si estuvieran esperando ser usados nuevamente. Algunas de las camas han sido volcadas, y uno de los gabinetes está abierto, con suministros médicos desperdigados por el suelo.',
        'imagen': 'imagenescuartos/Módulo médico.webp'
    },
    19: {
        'nombre': 'Bahía de carga',
        'descripcion':
        'El espacio es vasto y vacío, y el eco de tus pasos resuena en la oscuridad. Las cajas apiladas crean un laberinto de sombras inquietantes que parecen moverse con cada paso que das. Algunas pilas de contenedores han colapsado, creando un caos de escombros y materiales dispersos que dificultan la navegación.',
        'imagen': 'imagenescuartos/Bahía de carga.webp'
    },
    20: {
        'nombre': 'Cámara de aire',
        'descripcion':
        'El espacio es pequeño y claustrofóbico. El sonido del sistema de presurización es ensordecedor, y la puerta parece demasiado pesada para abrirse, aumentando la sensación de estar atrapado. Las paredes muestran grietas y el suelo presenta una inclinación anormal, señales de que la estructura ha sido debilitada.',
        'imagen': 'imagenescuartos/Cámara de aire.webp'
    },
    21: {
        'nombre': 'Habitación 7P (del encargado biológico)',
        'descripcion':
        'Los especímenes y documentos científicos están esparcidos por todas partes. La sensación de ser observado es intensa, y cada pequeño sonido te hace saltar de miedo. Las paredes y techos muestran grietas, y una de las vitrinas de especímenes se ha roto, esparciendo su contenido por el suelo, creando un ambiente aún más inquietante.',
        'imagen':
        'imagenescuartos/Habitación 7P (del encargado biológico).webp'
    },
    22: {
        'nombre': 'Área de experimentos',
        'descripcion':
        'Equipos científicos extraños y misteriosos llenan la sala. Rastros de experimentos fallidos y marcas en las paredes sugieren que algo salió terriblemente mal aquí. La sala parece desestabilizada, con maquinaria volcada y cables colgando del techo, aumentando la sensación de peligro inminente.',
        'imagen': 'imagenescuartos/Área de experimentos.webp'
    },
    23: {
        'nombre':
        'Habitación 4D (del ingeniero mecánico o aeronáutico)',
        'descripcion':
        'Equipos y herramientas están desordenados, y la luz parpadeante hace que las sombras se alarguen. El aire es denso y la sensación de abandono te pone nervioso. Los paneles están desprendidos, y un leve silbido emana de una grieta en la pared, haciendo que cada segundo en este lugar sea una prueba para tus nervios.',
        'imagen':
        'imagenescuartos/Habitación 4D (del ingeniero mecánico o aeronáutico).webp'
    },
    24: {
        'nombre': 'Laboratorio de computación',
        'descripcion':
        'Monitores apagados y teclados cubiertos de polvo te rodean. El zumbido constante de los servidores apagados crea una atmósfera inquietante. Algunos monitores han caído al suelo, sus pantallas rotas reflejan una luz parpadeante que parece darle vida a las sombras en la habitación.',
        'imagen': 'imagenescuartos/Laboratorio de computación.webp'
    },
    25: {
        'nombre': 'Sala de servidores',
        'descripcion':
        'El zumbido constante de las máquinas es ensordecedor. La falta de luz natural y la atmósfera fría hacen que el lugar se sienta opresivo y desolador. Las vibraciones han dañado algunos racks de servidores, dejando cables sueltos que chisporrotean en la penumbra.',
        'imagen': 'imagenescuartos/Sala de servidores.webp'
    },
    26: {
        'nombre': 'Control de propulsión',
        'descripcion':
        'Paneles de control y palancas llenan la sala. El silencio y la falta de actividad hacen que el lugar se sienta abandonado, como si nadie hubiera estado aquí en mucho tiempo. Algunos paneles cuelgan y las luces de advertencia parpadean sin cesar, señal de un mal funcionamiento que podría ser crítico.',
        'imagen': 'imagenescuartos/Control de propulsión.webp'
    },
    27: {
        'nombre': 'Control de navegación',
        'descripcion':
        'Estás en el Control de navegación. Pantallas apagadas y mapas estropeados te rodean. La sensación de estar a la deriva en el espacio es palpable, y cada movimiento se siente crucial. Las paredes muestran signos de estrés, con grietas que indican que la sala está comprometida, haciendo que cada segundo cuente.',
        'imagen': 'imagenescuartos/Control de navegación.webp'
    },
    28: {
        'nombre': 'Control de energía',
        'descripcion':
        'Interruptores y generadores llenan la sala. La atmósfera estancada y la falta de ruido te hacen sentir como si estuvieras en un lugar prohibido y peligroso. Los generadores están dañados, con ocasionales chispazos que iluminan brevemente la sala.',
        'imagen': 'imagenescuartos/Control de energía.webp'
    },
    29: {
        'nombre': 'Sala de robots',
        'descripcion':
        'Máquinas inactivas y piezas dispersas llenan el espacio. El silencio absoluto y la presencia de figuras metálicas inmóviles crean una sensación de inquietud que no puedes sacudirte. Algunos robots se han desprendido de sus soportes, dejando sus cuerpos inertes tirados en el suelo, como si estuvieran esperando a ser reactivados.',
        'imagen': 'imagenescuartos/Sala de robots.webp'
    },
    30: {
        'nombre': 'Depósito de herramientas',
        'descripcion':
        'Herramientas oxidadas y el olor a metal añaden una sensación de peligro. La oscuridad y el desorden hacen que el lugar sea aún más aterrador. Varias estanterías han colapsado, esparciendo herramientas por todo el suelo, creando un campo minado de objetos cortantes y peligrosos.',
        'imagen': 'imagenescuartos/Depósito de herramientas.webp'
    },
    31: {
        'nombre': 'Depósito de suministros',
        'descripcion':
        'Estanterías vacías y cajas dispersas llenan la sala. La sensación de escasez y el eco de tus pasos te hacen sentir desesperado por encontrar algo útil. La mayoría del almacenamiento ha sido destruido, dejando solo un par de cajas intactas, aumentando la urgencia de encontrar los recursos necesarios para sobrevivir.',
        'imagen': 'imagenescuartos/Depósito de suministros.webp'
    },
    32: {
        'nombre': 'Sala de cápsulas de escape',
        'descripcion':
        'Las cápsulas parecen intactas, pero el ambiente tenso y la sensación de urgencia hacen que cada segundo cuente mientras te preparas para abandonar la estación. La sala está en un estado precario, con luces de advertencia parpadeando y un leve sonido de alarma en el fondo, recordándote que el tiempo se agota.',
        'imagen': 'imagenescuartos/Sala de cápsulas de escape.webp'
    },
    33: {
        'nombre': 'Sala de control de drones',
        'descripcion':
        'Pantallas y controles llenan la sala. Los drones apagados y la falta de actividad crean una atmósfera de abandono y peligro inminente. Los sistemas de control están dañados, con pantallas rotas y paneles desprendidos, haciendo que la reactivación de los drones parezca una tarea imposible.',
        'imagen': 'imagenescuartos/Sala de control de drones.webp'
    },
    34: {
        'nombre': 'Sala de simulación',
        'descripcion':
        'Equipos abandonados y proyecciones holográficas parpadeantes crean sombras inquietantes. La atmósfera es tensa y cada sonido parece amplificado. Las simulaciones se activan aleatoriamente, creando un ambiente caótico donde es difícil distinguir la realidad de la ilusión.',
        'imagen': 'imagenescuartos/Sala de simulaciones.webp'
    },
    35: {
        'nombre': 'Estación de investigación',
        'descripcion':
        'Documentos y equipos abandonados están por todas partes. La falta de actividad y la atmósfera opresiva hacen que el lugar se sienta peligroso y olvidado. La estructura está visiblemente dañada, con grietas en las paredes y luces de emergencia que parpadean de manera errática, como si la estación misma estuviera a punto de colapsar.',
        'imagen': 'imagenescuartos/Estación de investigación.webp'
    },
    36: {
        'nombre':
        'Habitación 3A (habitación del personaje principal)',
        'descripcion':
        'Tus pertenencias están desordenadas, y la atmósfera es pesada con recuerdos de tiempos mejores. La sensación de soledad es abrumadora mientras te preparas para lo que viene. Algunos objetos personales han caído al suelo, y una grieta en la pared permite ver el espacio exterior, recordándote lo precaria que es tu situación.',
        'imagen':
        'imagenescuartos/Habitación 3A (habitación del personaje principal).webp'
    },
}


#--------------------diccionario de misiones--------------------------------
#misiones obligatorias 1, 2, 10, 13, 3, 4, 7,14
misiones = {
    1:  {
        'nombre' : 'Restaurar el Soporte Vital',
        'objetos_necesarios' : ['llave_inglesa','kit_de_reparacion'] ,
        'descripcion' :'La estación ha sufrido graves daños, y los sistemas de soporte vital están fallando. El oxígeno es escaso y la atmósfera se vuelve cada vez más irrespirable. Debes encontrar las herramientas necesarias, como un kit de reparación y una llave inglesa, para acceder al núcleo de soporte vital y reparar los conductos antes de que sea demasiado tarde. El tiempo apremia, y cada segundo cuenta para evitar una catástrofe.',
        'bool' : False
    },
    2: {
        'nombre' : 'Estabilizar el Control de Energía',
        'objetos_necesarios' :  ['martillo', 'soldador', 'celda_de_combustible', 'tarjeta_ce'] ,
        'descripcion' :'La energía de la estación es inestable y amenaza con apagones que podrían ser fatales. Debes estabilizar el Control de Energía para evitar el colapso total. Reúne las herramientas necesarias, como un martillo, un soldador y una celda de combustible, y consigue la tarjeta de acceso para entrar en la sala de control. El tiempo es crítico, y debes actuar con rapidez para asegurar la estabilidad de la estación.',
        'bool' : False
    },
    3: {
        'nombre' : 'Reiniciar el Sistema de Comunicaciones',
        'objetos_necesarios' : ['pendrive_de_hackeo', 'cable_megasync'] ,
        'descripcion' :'La comunicación con la Tierra se ha perdido, dejando la estación aislada en la inmensidad del espacio. Para restablecer el contacto, es necesario reiniciar el sistema de comunicaciones. Utiliza un pendrive de hackeo y un cable Megasync para acceder al núcleo de datos y reconfigurar el sistema. La estación está en un estado crítico, y debes actuar rápidamente para asegurar una conexión estable antes de que sea demasiado tarde.',
        'bool' : False
    },
    4: {
        'nombre' : 'Desactivar el Sistema de Seguridad del Laboratorio Químico',
        'objetos_necesarios' : ['tarjeta_aq', 'mascara_de_gas'] ,
        'descripcion' :'El Laboratorio Químico ha quedado sellado debido a la liberación de gases tóxicos. Para acceder y desactivar el sistema de seguridad, debes encontrar una máscara de gas y la tarjeta de acceso adecuada. La atmósfera dentro del laboratorio es letal, y las trampas químicas son peligrosas. Desactivar el sistema es esencial para restaurar la seguridad en esta área crítica de la estación.',
        'bool' : False
    },
    5: {
        'nombre' : 'Obtener Información del Laboratorio Biológico',
        'objetos_necesarios' : ['linterna'] ,
        'descripcion' :'El Módulo de laboratorio biológico está envuelto en sombras, con la mayoría de los sistemas apagados. Debes explorar el laboratorio con una linterna para descubrir pistas sobre el estado de la estación. La luz revela detalles inquietantes de experimentos abandonados y notas dispersas que sugieren que algo terrible ocurrió aquí. Es crucial obtener esta información para entender mejor la situación en la estación.',
        'bool' : False
    },
    6: {
        'nombre' : 'Recuperar Herramientas Esenciales',
        'objetos_necesarios' : ['herramienta_de_corte', 'refrigerante'],
        'descripcion' :'Las reparaciones necesarias para asegurar la estación requieren herramientas específicas. Debes encontrar una herramienta de corte y un refrigerante, esenciales para las reparaciones críticas. El camino para recuperarlos no será fácil, con puertas atascadas y fluctuaciones extremas de temperatura en los pasillos. Estas herramientas son clave para completar las reparaciones necesarias.',
        'bool' : False
    },
    7: {
        'nombre' : 'Reparar el Sistema de Propulsión',
        'objetos_necesarios' : ['herramienta_de_corte', 'refrigerante'] ,
        'descripcion' :'El sistema de propulsión de la estación, vital para mantener su órbita, está al borde del colapso. Con la herramienta de corte y el refrigerante, debes acceder al módulo de propulsión y realizar las reparaciones necesarias. La sala está llena de peligros, con gases calientes y chispas volando. Cada acción debe ser precisa para asegurar la estabilidad de la estación y evitar que se desvíe de su curso.',
        'bool' : False
    },
    8: {
        'nombre' : 'Recuperar la Tarjeta de Acceso del Capitán',
        'objetos_necesarios' : ['linterna', 'tarjeta_cap'] ,
        'descripcion' :'La tarjeta de acceso del Capitán es necesaria para acceder a las áreas más críticas de la estación. Se encuentra en algún lugar oscuro, posiblemente bajo escombros y sombras. Con la linterna, debes explorar y recuperar la tarjeta para poder avanzar en las tareas esenciales que asegurarán tu supervivencia y la de la estación.',
        'bool' : False
    },
    9: {
        'nombre' : 'Investigar el Módulo de Control',
        'objetos_necesarios' : [] ,
        'descripcion' :'El Módulo de Control, el cerebro de la estación, se encuentra en un estado extraño. Las consolas parpadean con datos incompletos y los registros muestran inconsistencias inquietantes. Debes investigar este lugar, que debería estar lleno de vida, pero que ahora está silencioso y vacío. La investigación podría revelar pistas cruciales sobre lo que está sucediendo en la estación.',
        'bool' : False
    },
    10: {
        'nombre' : 'Enfrentar la Amenaza en la Sala de Robots',
        'objetos_necesarios' : ['extintor_de_incendios','gafas_de_protección'] ,
        'descripcion' :'Los robots de la estación, antes compañeros de trabajo, ahora son una amenaza letal. En la Sala de Robots, los androides patrullan con intenciones hostiles. Debes enfrentarte a ellos utilizando un extintor de incendios y protegerte con gafas especiales. Neutralizar a los robots o evadir sus ataques será esencial para continuar con la misión y asegurar tu supervivencia.',
        'bool' : False
    },
    11: {
        'nombre' : 'Investigar el Área de Experimentos',
        'objetos_necesarios' : [] ,
        'descripcion' :'El Área de Experimentos está envuelta en misterio, con signos de actividades que se salieron de control. Notas dispersas, frascos rotos y máquinas extrañas sugieren que los experimentos aquí realizados eran peligrosos y no convencionales. Debes investigar este lugar para obtener información crítica sobre lo que realmente ocurrió en la estación. Cada pista puede acercarte a entender la magnitud de la amenaza que enfrentas.',
        'bool' : False
    },
    12: {
        'nombre' : 'Reunir la Información Final',
        'objetos_necesarios' : ['pendrive_de_hackeo'] ,
        'descripcion' :'La clave para entender lo que ha ocurrido en la estación se encuentra en la Estación de Investigación, pero está bloqueada por un avanzado sistema de seguridad. Con un pendrive de hackeo, debes infiltrarte en los sistemas protegidos y reunir la información crucial. Esta misión es vital para entender completamente la situación y prepararte para los desafíos finales que te esperan.',
        'bool' : False
    },
    13: {
        'nombre' : 'Reparar el Sistema de Estabilización',
        'objetos_necesarios' : ['pendrive_sistema_est', 'destornillador_especial'],
        'descripcion' :'El Sistema de Estabilización está fallando, y es esencial repararlo para evitar un desastre mayor. Con un pendrive especial y un destornillador, debes acceder al sistema y realizar las reparaciones necesarias. La estación depende de esta misión para mantener su integridad y evitar el colapso total.',
        'bool' : False
    },
    14: {
        'nombre' : 'Escapar de la Estación',
        'objetos_necesarios' : ['codigo_capsula_escape'] ,
        'descripcion' :'Con la estación al borde del desastre, la única opción es escapar. Debes llegar a la Sala de Cápsulas de Escape y utilizar el código de acceso que está escondido en un lugar crucial. El caos se intensifica, con alarmas y luces parpadeando por toda la estación. Debes actuar rápidamente para activar la cápsula y escapar antes de que todo colapse a tu alrededor.',
        'bool' : False
    }
} 

#diccionario de comando validos para cada objeto
comandos_validos = {  #Escrito en miniscula para disminuir errores al validar
    'recoger': ['linterna','mascara_de_gas' , 'pendrive_de_hackeo', 'llave_inglesa', 'extintor_de_incendios','tarjeta_aq', 'tarjeta_ce', 'gafas_de_proteccion', 'soldador', 'martillo', 'guantes', 'herramienta_de_corte','tarjeta_cap','refrigerante', 'celda_de_combustible', 'pendrive_sistema_est', 'gafas_de_proteccion', 'codigo_capsula_escape', 'destornillador_especial','kit_de_reparacion', 'cable_megasync', 'botella','flameador','tijeras','foto_familiar', 'pinzas','banda_elastica','manometro','cinta','espejo',],#30 objetos
    'ir': ['norte', 'sur', 'este', 'oeste'],
    'ver': ['ayuda', 'inventario', 'misiones'],
    'salir' : ['juego']
} 

#dicionarios de objetos en cada habitacion
objetos_en_habitacion = {
    1: ['botella'],
    2: [],# no colocar objetos
    3: [],#no colocar objetos
    4: ['tijeras'],
    5: [],#no colocar objetos
    6: ['martillo','refrigerante'],
    7: ['cable_megasync','codigo_capsula_escape'],
    8: [],#no colocar objetos
    9: ['flameador','kit_de_reparacion'],
    10: [], #no colocar objetos
    11: [], #no colocar objetos
    12: ['linterna'],
    13: ['pinzas'],
    14: [],
    15: ['banda_elastica'],
    16: ['tarjeta_aq','espejo'],
    17: ['extintor_de_incendios'],
    18: ['mascara_de_gas'],
    19: ['llave_inglesa'],
    20: ['manometro'],
    21: ['tarjeta_ce'],
    22: [], #no colocar objetos
    23: ['pendrive_sistema_est'],
    24: [],#no colocar objetos
    25: ['pendrive_de_hackeo','cinta'],
    26: [],#no colocar objetos
    27: ['tarjeta_cap'],
    28: [], #no colocar objetos
    29: [],    #no colocar objetos
    30: [], #no colocar objetos
    31: ['herramienta_de_corte'],
    32: [], #no colocar objetos
    33: ['soldador','celda_de_combustible'],
    34: ['gafas_de_proteccion','destornillador_especial'],
    35: [], #no colocar objetos
    36: ['foto_familiar'],
}
salidas = {
    1: {
        'norte': 6,
        'sur': 15,
        'oeste': 31
    },  #Seguir en base al mapa de habitaciones
    2: {
        'norte': 7,
        'sur': 12,
        'oeste': 3
    },
    3: {
        'norte': 21,
        'este': 2,
        'sur': 17,
        'oeste': 6
    },
    4: {
        'sur': 5
    },
    5: {
        'norte': 4,
        'este': 21,
        'sur': 6
    },
    6: {
        'norte': 5,
        'este': 3,
        'sur': 1
    },
    7: {
        'norte': 22,
        'sur': 2,
        'oeste': 21
    },
    8: {
        'norte': 10,
        'este': 19,
        'oeste': 30
    },
    9: {
        'este': 27,
        'sur': 36,
        'oeste': 23
    },
    10: {
        'norte': 20,
        'sur': 8,
        'oeste': 18
    },
    11: {
        'norte': 25
    },
    12: {
        'norte': 2,
        'este': 34,
        'oeste': 17
    },
    13: {
        'norte': 15,
        'este': 14
    },
    14: {
        'norte': 16,
        'oeste': 13
    },
    15: {
        'norte': 1,
        'este': 16,
        'sur': 13
    },
    16: {
        'norte': 17,
        'sur': 14,
        'oeste': 15
    },
    17: {
        'norte': 3,
        'este': 12,
        'sur': 16
    },
    18: {
        'norte': 35,
        'este': 10
    },
    19: {
        'este': 33,
        'oeste': 8
    },
    20: {
        'este': 28,
        'sur': 10,
        'oeste': 35
    },
    21: {
        'este': 7,
        'sur': 3,
        'oeste': 5
    },
    22: {
        'sur': 7
    },
    23: {
        'norte': 34,
        'este': 9,
        'oeste': 25
    },
    24: {
        'oeste': 27
    },
    25: {
        'este': 23,
        'sur': 11
    },
    26: {
        'sur': 33
    },
    27: {
        'este': 24,
        'sur': 29,
        'oeste': 9
    },
    28: {
        'oeste': 20
    },
    29: {
        'norte': 27,
        'oeste': 36
    },
    30: {
        'este': 8,
        'sur': 34
    },
    31: {
        'este': 1
    },
    32: {
        'norte': 33
    },
    33: {
        'norte': 26,
        'sur': 32,
        'oeste': 19
    },
    34: {
        'norte': 30,
        'sur': 23,
        'oeste': 12
    },
    35: {
        'este': 20,
        'sur': 18
    },
    36: {
        'norte': 9,
        'este': 29
    }
}
