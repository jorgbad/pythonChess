from clases import *

FPS = 60  # Fotogramas por segundo

def main():
    # Inicializacion de Pygame
    pygame.init()
    # Inicializacion de la superficie de dibujo (display surface)
    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))
    pygame.display.set_caption("Ajedrez")

    figuras_b = list(Nada for x in range (16))
    figuras_b[0] = Torre("b","ajedrez/img/torre_b.png")
    figuras_b[1] = Caballo("b","ajedrez/img/caballo_b.png")
    figuras_b[2] = Alfil("b","ajedrez/img/alfil_b.png")
    figuras_b[3] = Rey("b","ajedrez/img/rey_b.png")
    figuras_b[4] = Reina("b","ajedrez/img/reina_b.png")
    figuras_b[5] = Alfil("b","ajedrez/img/alfil_b.png")
    figuras_b[6] = Caballo("b","ajedrez/img/caballo_b.png")
    figuras_b[7] = Torre("b","ajedrez/img/torre_b.png")
    figuras_b[8] = Peon("b","ajedrez/img/peon_b.png")
    figuras_b[9] = Peon("b","ajedrez/img/peon_b.png")
    figuras_b[10] = Peon("b","ajedrez/img/peon_b.png")
    figuras_b[11] = Peon("b","ajedrez/img/peon_b.png")
    figuras_b[12] = Peon("b","ajedrez/img/peon_b.png")
    figuras_b[13] = Peon("b","ajedrez/img/peon_b.png")
    figuras_b[14] = Peon("b","ajedrez/img/peon_b.png")
    figuras_b[15] = Peon("b","ajedrez/img/peon_b.png")

    figuras_n = list(Nada for x in range (16))
    figuras_n[0] = Torre("n","ajedrez/img/torre_n.png")
    figuras_n[1] = Caballo("n","ajedrez/img/caballo_n.png")
    figuras_n[2] = Alfil("n","ajedrez/img/alfil_n.png")
    figuras_n[3] = Rey("n","ajedrez/img/rey_n.png")
    figuras_n[4] = Reina("n","ajedrez/img/reina_n.png")
    figuras_n[5] = Alfil("n","ajedrez/img/alfil_n.png")
    figuras_n[6] = Caballo("n","ajedrez/img/caballo_n.png")
    figuras_n[7] = Torre("n","ajedrez/img/torre_n.png")
    figuras_n[8] = Peon("n","ajedrez/img/peon_n.png")
    figuras_n[9] = Peon("n","ajedrez/img/peon_n.png")
    figuras_n[10] = Peon("n","ajedrez/img/peon_n.png")
    figuras_n[11] = Peon("n","ajedrez/img/peon_n.png")
    figuras_n[12] = Peon("n","ajedrez/img/peon_n.png")
    figuras_n[13] = Peon("n","ajedrez/img/peon_n.png")
    figuras_n[14] = Peon("n","ajedrez/img/peon_n.png")
    figuras_n[15] = Peon("n","ajedrez/img/peon_n.png")

    situacion = Tablero(figuras_b, figuras_n)
    situacion.pintar( ventana )
    pygame.display.flip()
    
    # Bucle principal
    figura_mov = Nada()
    jugando = True
    while jugando :
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False  
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = (event.pos[0]-INICIO_TABLERO)//LADO_CASILLA
                y = (event.pos[1]-INICIO_TABLERO)//LADO_CASILLA
                sel = (x, y)
                if (event.pos[0] in range(INICIO_TABLERO, FIN_TABLERO) and event.pos[1] in range(INICIO_TABLERO, FIN_TABLERO)):
                    print(f"boton pulsado en casilla {sel}")
                    rect_x = INICIO_TABLERO + LADO_CASILLA*((event.pos[0]-INICIO_TABLERO)//LADO_CASILLA) # calculo la x del origen de la casilla en la que está el ratón  
                    rect_y = INICIO_TABLERO + LADO_CASILLA*((event.pos[1]-INICIO_TABLERO)//LADO_CASILLA) # calculo la y del origen de la casilla en la que está el ratón  
                    figura_mov = situacion[sel[0] + 8 * sel[1]]
                    situacion.modificar(Nada(), sel[0], sel[1])
                    situacion.pintar(ventana)
                    pygame.draw.rect(ventana, FONDO, (rect_x, rect_y , LADO_CASILLA , LADO_CASILLA), BORDE) # rectangular (height, width), (30, 30)
                    pygame.display.flip()
                else:
                    print ("Pulsacion fuera del tablero")

            if event.type == pygame.MOUSEBUTTONUP:
                x = (event.pos[0]-INICIO_TABLERO)//LADO_CASILLA
                y = (event.pos[1]-INICIO_TABLERO)//LADO_CASILLA
                des = (x, y)
                if (event.pos[0] in range(INICIO_TABLERO, FIN_TABLERO) and event.pos[1] in range(INICIO_TABLERO, FIN_TABLERO)):
                    print(f"Movimiento desde {sel} hasta {des}")
                    if ( figura_mov.getTipo() != Nada ):
                        situacion.modificar(figura_mov, des[0], des[1])   
                else :
                    print ("Soltado fuera del tablero")
                    situacion.modificar(figura_mov, sel[0], sel[1])
                figura_mov = Nada()
                situacion.pintar(ventana) 
                pygame.display.flip()

            if event.type == pygame.MOUSEMOTION:
                x = (event.pos[0] - LADO_CASILLA / 2)
                y = (event.pos[1] - LADO_CASILLA / 2)
                pos = (x, y)
                if ( figura_mov.getTipo() != Nada ):
                    situacion.pintar(ventana)
                    ventana.blit(figura_mov.imagen, pos)
                    pygame.draw.rect(ventana, FONDO, (pos[0], pos[1], LADO_CASILLA, LADO_CASILLA), BORDE) # rectangular (height, width), (30, 30)
                    pygame.display.flip()              
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

