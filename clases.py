import pygame
from pygame.locals import *


VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
INICIO_TABLERO = 20 # Inicio del tablero con respecto a la ventana
FIN_TABLERO = 580 # Fin del tablero con respecto a la ventana
LADO_CASILLA = 70 # Tamaño del lado de cada casilla
BORDE = 3 # Tamaño del borde de la casilla seleccionada
FONDO = (128, 128, 128)  # Color del fondo de la ventana (RGB)
BLANCO = (249, 247, 195)
NEGRO = (161, 100, 0)

class Tablero:
    def __init__(self, figuras_b, figuras_n):
        # --- Atributos de la Clase ---

        self.situacion = list (Nada() for x in range (64))
        self.reset ( figuras_b, figuras_n )
        
    def __getitem__(self, indice):
        return self.situacion[indice]

    def pintar (self, lienzo):
        # pinto damero
        lienzo.fill(FONDO)
        x = y = INICIO_TABLERO
        for j in range (8) :
            for i in range (8) : 
                if j % 2 == 0 :
                    if i % 2 == 0 :
                        color = BLANCO
                    else :
                        color = NEGRO
                else :
                    if i % 2 == 0 :
                        color = NEGRO
                    else :
                        color = BLANCO

                pygame.draw.rect ( lienzo, color, [x, y, LADO_CASILLA, LADO_CASILLA])
                if self.situacion[i + 8 * j].getTipo() != Nada :
                    lienzo.blit(self.situacion[i + 8 * j].imagen, (x, y))
                x += LADO_CASILLA
            y += LADO_CASILLA
            x = INICIO_TABLERO
        return 0

    def reset ( self, figuras_b, figuras_n ):
        for x in range(8) : 
            self.situacion[x] = figuras_b[x] 
            self.situacion[x].setPos_x (x)
            self.situacion[x].setPos_y (0)
            self.situacion[x+8] = figuras_b[8 + x]
            self.situacion[x+8].setPos_x (x)
            self.situacion[x+8].setPos_y (1)
            self.situacion[x+16] = Nada()
            self.situacion[x+16].setPos_x (x)
            self.situacion[x+16].setPos_y (2)
            self.situacion[x+24] = Nada()
            self.situacion[x+24].setPos_x (x)
            self.situacion[x+24].setPos_y (3)
            self.situacion[x+32] = Nada()
            self.situacion[x+32].setPos_x (x)
            self.situacion[x+32].setPos_y (4)
            self.situacion[x+40] = Nada()
            self.situacion[x+40].setPos_x (x)
            self.situacion[x+40].setPos_y (5)
            self.situacion[x+48] = figuras_n[-1 * (x + 1) ] 
            self.situacion[x+48].setPos_x (x)
            self.situacion[x+48].setPos_y (6)
            self.situacion[x+56] = figuras_n[ 8 + ( -1 * (x + 1))]   
            self.situacion[x+56].setPos_x (x)
            self.situacion[x+56].setPos_y (7)    

    def modificar ( self, figura, x, y):
        self.situacion[x + 8 * y] = figura
        self.situacion[x + 8 * y].setPos_x = x
        self.situacion[x + 8 * y].setPos_y = y
        print(self.situacion[x + 8 * y].getTipo())   

class Pieza:
    def __init__(self, color, fichero_imagen ):
        self.color = color
        pos_x = -1
        pos_y = -1

        # Imagen de la pieza
        if fichero_imagen != "":
            self.imagen = pygame.image.load( fichero_imagen ).convert_alpha()

        # Dimensiones de la pieza
        if fichero_imagen != "":
            self.ancho, self.alto = self.imagen.get_size()
    
    def getColor(self):
        return self.color

    def getSelected(self):
        return self.selected

    def getDestino(self):
        return self.destino

    def setSelected(self, seleccionado):
        self.selected = seleccionado
        
    def setPos_x(self, x):
        self.pos_x = x
        
    def setPos_y(self, y):
        self.pos_y = y

    def setDestino(self, destino):
        self.destino = destino


class Nada(Pieza):
    def __init__(self):        
        super().__init__(color = "t", fichero_imagen = "" )
    
    def getTipo(self):
        return type(self)


class Torre(Pieza):
    def __init__(self, color, fichero_imagen ):
        super().__init__(color, fichero_imagen )
    
    def getTipo(self):
        return type(self)


class Caballo(Pieza):
    def __init__(self, color, fichero_imagen ):
        super().__init__(color, fichero_imagen )
    
    def getTipo(self):
        return type(self)



class Alfil(Pieza):
    def __init__(self, color, fichero_imagen):
        super().__init__(color, fichero_imagen)
    
    def getTipo(self):
        return type(self)


class Rey(Pieza):
    def __init__(self, color, fichero_imagen):
        super().__init__(color, fichero_imagen)
    
    def getTipo(self):
        return type(self)


class Reina(Pieza):
    def __init__(self, color, fichero_imagen):
        super().__init__(color, fichero_imagen)
    
    def getTipo(self):
        return type(self)


class Peon(Pieza):
    def __init__(self, color, fichero_imagen):
        super().__init__(color, fichero_imagen)
    
    def getTipo(self):
        return type(self)