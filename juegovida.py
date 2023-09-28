# Importar librerías
import pygame
import numpy as np
import time

# Inicializar pantalla
pygame.init()
width, height = 800, 800 # Tamaño de la pantalla
bg = 25, 25, 25 # Color de fondo
screen = pygame.display.set_mode((height, width)) # Crear ventana
screen.fill(bg) # Rellenar ventana con color

# Definir matriz de celdas
nxC, nyC = 50, 50 # Tamaño de la matriz
gameState = np.zeros((nxC, nyC)) # Estado inicial con todas las celdas muertas
# Asignar valores iniciales a algunas celdas
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

# Bucle principal
while True:

    # Copiar el estado actual del juego
    newGameState = np.copy(gameState)

    # Rellenar la pantalla con el color de fondo
    screen.fill(bg)

    # Recorrer cada celda y dibujarla en la pantalla
    for x in range(0, nxC):
        for y in range(0, nyC):

            # Calcular el número de vecinos vivos
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x)     % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, (y)     % nyC] + \
                      gameState[(x + 1) % nxC, (y)     % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[(x)     % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC]

            # Aplicar las reglas del juego de la vida
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1 # La celda revive
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0 # La celda muere

            # Calcular las coordenadas del rectángulo que representa la celda
            poly = [((x)   * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Dibujar el rectángulo con un color según el estado de la celda
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Actualizar el estado del juego
    gameState = np.copy(newGameState)

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar un tiempo entre cada iteración
    time.sleep(0.1)
