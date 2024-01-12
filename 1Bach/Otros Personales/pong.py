import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 640
ALTURA = 480
PANTALLA = pygame.display.set_mode((ANCHO, ALTURA))
pygame.display.set_caption('Pong')

# Configuración de colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración de las paletas
PALETA_ANCHO = 10
PALETA_ALTURA = 50

PALETA_JUGADOR = pygame.Rect(ANCHO - 20, ALTURA // 2 - PALETA_ALTURA // 2, PALETA_ANCHO, PALETA_ALTURA)
PALETA_CPU = pygame.Rect(10, ALTURA // 2 - PALETA_ALTURA // 2, PALETA_ANCHO, PALETA_ALTURA)

# Configuración de la pelota
PELOTA_RADIO = 5
PELOTA_POSICION = (ANCHO // 2, ALTURA // 2)
PELOTA_VELOCIDAD = [random.choice([3, 4]), random.choice([3, 4])]

# Configuración de la puntuación
puntuacion_jugador = 0
puntuacion_cpu = 0
fuente = pygame.font.Font(None, 36)

# Bucle del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Movimiento de la pelota
    PELOTA_POSICION[1] += PELOTA_VELOCIDAD[1]

    # Colisión con las paredes
    if PELOTA_POSICION[1] <= PELOTA_RADIO or PELOTA_POSICION[1] >= ALTURA - PELOTA_RADIO:
        PELOTA_VELOCIDAD[1] = -PELOTA_VELOCIDAD[1]

    # Colisión con las paletas
    if (PELOTA_POSICION[0] >= ANCHO - 20 - PALETA_ANCHO - PELOTA_RADIO and
            PELOTA_POSICION[1] >= PALETA_JUGADOR.top and PELOTA_POSICION[1] <= PALETA_JUGADOR.bottom):
        PELOTA_VELOCIDAD[0] = -PELOTA_VELOCIDAD[0]
    elif (PELOTA_POSICION[0] <= 10 + PALETA_ANCHO + PELOTA_RADIO and
            PELOTA_POSICION[1] >= PALETA_CPU.top and PELOTA_POSICION[1] <= PALETA_CPU.bottom):
        PELOTA_VELOCIDAD[0] = -PELOTA_VELOCIDAD[0]
    elif PELOTA_POSICION[0] <= PELOTA_RADIO:
        puntuacion_cpu += 1
        PELOTA_POSICION = (ANCHO // 2, ALTURA // 2)
        PELOTA_VELOCIDAD = [random.choice([3, 4]), random.choice([3, 4])]
    elif PELOTA_POSICION[0] >= ANCHO - PELOTA_RADIO:

        PANTALLA.fill(NEGRO)
    pygame.draw.rect(PANTALLA, BLANCO, PALETA_JUGADOR)
    pygame.draw.rect(PANTALLA, BLANCO, PALETA_CPU)
    pygame.draw.circle(PANTALLA, BLANCO, PELOTA_POSICION, PELOTA_RADIO)

    # Movimiento de la paleta del jugador con las teclas
    teclas_pulsadas = pygame.key.get_pressed()
    if teclas_pulsadas[pygame.K_UP] and PALETA_JUGADOR.top > 0:
        PALETA_JUGADOR.move_ip(0, -5)
    if teclas_pulsadas[pygame.K_DOWN] and PALETA_JUGADOR.bottom < ALTURA:
        PALETA_JUGADOR.move_ip(0, 5)

    # Movimiento de la paleta de la CPU
    if PELOTA_VELOCIDAD[0] > 0 and PELOTA_POSICION[0] >= ANCHO // 2:
        if PALETA_CPU.centery < PELOTA_POSICION[1] and PALETA_CPU.bottom < ALTURA:
            PALETA_CPU.move_ip(0, 5)
        elif PALETA_CPU.centery > PELOTA_POSICION[1] and PALETA_CPU.top > 0:
            PALETA_CPU.move_ip(0, -5)

    # Actualización de la pantalla
    pygame.display.flip()

    # Dibujo de la puntuación
    texto_puntuacion = fuente.render(f'{puntuacion_jugador} - {puntuacion_cpu}', True, BLANCO)
    PANTALLA.blit(texto_puntuacion, (ANCHO // 2 - texto_puntuacion.get_width() // 2, 10))

    # Comprobación de fin de juego
    if puntuacion_jugador == 10:
        texto_fin = fuente.render('¡Has ganado!', True, BLANCO)
        PANTALLA.blit(texto_fin, (ANCHO // 2 - texto_fin.get_width() // 2, ALTURA // 2 - texto_fin.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        exit()
    elif puntuacion_cpu == 10:
        texto_fin = fuente.render('¡Has perdido!', True, BLANCO)
        PANTALLA.blit(texto_fin, (ANCHO // 2 - texto_fin.get_width() // 2, ALTURA // 2 - texto_fin.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        exit()
