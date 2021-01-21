import pygame
import random
from pygame.locals import *


VENTANA_HORI = 800  # Ancho de la ventana
VENTANA_VERT = 600  # Alto de la ventana
INICIO_TABLERO = 20 # Inicio del tablero con respecto a la ventana
FIN_TABLERO = 580 # Fin del tablero con respecto a la ventana
LADO_CASILLA = 70 # Tamaño del lado de cada casilla
BORDE = 3 # Tamaño del borde de la casilla seleccionada
PASO_ATPC = 5
FONDO = (128, 128, 128)  # Color del fondo de la ventana (RGB)
BLANCO = (249, 247, 195)
NEGRO = (161, 100, 0)

class Tablero:
    def __init__(self, figuras_b, figuras_n):
        # --- Atributos de la Clase ---

        self.situacion = list (Nada for x in range (64))
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
        casilla = x + 8 * y
        self.situacion[casilla] = figura
        self.situacion[casilla].setPos_x( x )
        self.situacion[casilla].setPos_y( y )

class Pieza:
    def __init__(self, color, fichero_imagen ):
        self.color = color
        self.pos_x = -1
        self.pos_y = -1
        self.tipo = None
        self.mov_pos = ()
        self.verif_obst = False
        
        # Imagen de la pieza
        if fichero_imagen != "":
            self.imagen = pygame.image.load( fichero_imagen ).convert_alpha()

        # Dimensiones de la pieza
        if fichero_imagen != "":
            self.ancho, self.alto = (LADO_CASILLA, LADO_CASILLA)
    
    def getColor(self):
        return self.color

    def getAncho(self):
        return self.ancho

    def getAlto(self):
        return self.alto

    def setDimensiones(self, medidas):
        self.ancho, self.alto = medidas
        
    def setPos_x(self, x):
        self.pos_x = x
        
    def setPos_y(self, y):
        self.pos_y = y

    def setAncho(self, anchura):
        self.imagen.ancho = anchura

    def hay_obst (self, situacion, x, y):
        if x > self.pos_x :
            sentido_x = 1
        elif x < self.pos_x :
            sentido_x = -1
        else:
            sentido_x = 0
        if y > self.pos_y :
            sentido_y = 1
        elif y < self.pos_y :
            sentido_y = -1
        else:
            sentido_y = 0
        i = self.pos_x + sentido_x
        j = self.pos_y + sentido_y
        while (i,j) != (x,y) :
            if situacion[i + 8 * j].getTipo() != Nada :
                return True
            i += sentido_x
            j += sentido_y
        return False

    def chk_mov( self, situacion, x, y):
        destinos_posibles = list()
        for i in self.mov_pos :
            destinos_posibles.append((self.pos_x + i[0], self.pos_y + i[1]))  
        for i in destinos_posibles:
            if i[0] == x and i[1] == y: # si el destino está entre los posibles
                if i[0] in range(0,8) and i[1] in range(0,8): # verifico q el posible destino esté dentro del tablero
                    if self.verif_obst:
                        if self.hay_obst(situacion, x, y) : # si detecto obstaculos en trayectoria
                            return 4
                    if situacion[i[0] + 8 * i[1]].getColor() == self.color : # si en destino hay figura del mismo color
                        return 2
                    elif situacion[i[0] + 8 * i[1]].getColor() == "t" : # si en destino no hay pieza
                        return 1
                    else :  # si en destino hay pieza de color contrario ( se comerá la pieza en destino )
                        return 3
        return 9


class Nada(Pieza):
    def __init__(self):        
        super().__init__(color = "t", fichero_imagen = "" )
    
    def getTipo(self):
        return type(self)


class Torre(Pieza):
    def __init__(self, color, fichero_imagen ):
        super().__init__(color, fichero_imagen )
        self.mov_pos_gen = range(-7,8)
        self.mov_pos = []
        for i in self.mov_pos_gen:
            if i != 0:
                self.mov_pos.append([i,0])
                self.mov_pos.append([0,i])
        self.verif_obst = True
    
    def getTipo(self):
        return type(self)


class Caballo(Pieza):
    def __init__(self, color, fichero_imagen ):
        super().__init__(color, fichero_imagen )
        self.mov_pos = ([1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1])
        self.verif_obst = False
    
    def getTipo(self):
        return type(self)


class Alfil(Pieza):
    def __init__(self, color, fichero_imagen):
        super().__init__(color, fichero_imagen)
        self.mov_pos_gen = range(-7,8)
        self.mov_pos = []
        for i in self.mov_pos_gen:
            if i != 0:
                self.mov_pos.append([i,i])
                self.mov_pos.append([i,-1 * i])
        self.verif_obst = True
    
    def getTipo(self):
        return type(self)


class Rey(Pieza):
    def __init__(self, color, fichero_imagen):
        super().__init__(color, fichero_imagen)        
        self.mov_pos = ([1,1],[1,0],[1,-1],[-1,1],[-1,0],[-1,-1],[0,1],[0,-1])
        self.verif_obst = False
    
    def getTipo(self):
        return type(self)


class Reina(Pieza):
    def __init__(self, color, fichero_imagen):
        super().__init__(color, fichero_imagen)
        self.mov_pos_gen = range(-7,8)
        self.mov_pos = []
        for i in self.mov_pos_gen:
            if i != 0:
                self.mov_pos.append([i,i])
                self.mov_pos.append([i,-1 * i])
                self.mov_pos.append([i,0])
                self.mov_pos.append([0,i])
        self.verif_obst = True
    
    def getTipo(self):
        return type(self)


class Peon(Pieza):
    def __init__(self, color, fichero_imagen):
        super().__init__(color, fichero_imagen)
        self.mov_pos = ([0,1],[0,2],[1,1],[-1,1],[0,-1],[0,-2],[1,-1],[-1,-1])

    def getTipo(self):
        return type(self)

    def chk_mov( self, situacion, x, y):
        destinos_posibles = list()
        for i in self.mov_pos :
            if self.color == "b" :
                if i[1] > 0 :
                    destinos_posibles.append((self.pos_x + i[0], self.pos_y + i[1]))  
            else :
                if i[1] < 0 :
                    destinos_posibles.append((self.pos_x + i[0], self.pos_y + i[1]))  
        for i in destinos_posibles:
            if i[0] == x and i[1] == y: # si el destino está entre los posibles
                if i[0] in range(0,8) and i[1] in range(0,8): # verifico q el posible destino esté dentro del tablero
                    if ( self.pos_x != x ):     # si el movimiento es diagonal
                        if situacion[i[0] + 8 * i[1]].getColor() == self.color : # si en destino hay figura del mismo color
                            return 2
                        elif situacion[i[0] + 8 * i[1]].getColor() == "t" : # si en destino no hay pieza
                            return 9
                        else :  # si en destino hay pieza de color contrario ( se comerá la pieza en destino )
                            return 3
                    else :      # si el movimiento es vertical
                        if abs ( i[1] - self.pos_y ) == 2: # si el movimiento es doble
                            if self.color == "b" and self.pos_y == 1 : # si el movimiento doble es desde posicion inicial
                                if ( situacion[i[0] + 8 * ( i[1] - 1 )].getColor() != "t"):
                                    return 4                                
                            elif self.color == "n" and self.pos_y == 6 : # si el movimientodoble  es desde posicion inicial
                                if ( situacion[i[0] + 8 * ( i[1] + 1 )].getColor() != "t"):
                                    return 4
                            else: # si el movimiento doble NO es desde posicion inicial
                                return 9
                        if situacion[i[0] + 8 * i[1]].getColor() == self.color : # si en destino hay figura del mismo color
                            return 2
                        elif situacion[i[0] + 8 * i[1]].getColor() == "t" : # si en destino no hay pieza
                            return 1
                        else :  # si en destino hay pieza de color contrario ( movimiento no valido )
                            return 9                        
        return 9


