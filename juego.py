from clases import *

FPS = 60  # Fotogramas por segundo

def jugar(nombre_b, nombre_n):
    pygame.init()

    ventana = pygame.display.set_mode((VENTANA_HORI, VENTANA_VERT))

    pygame.display.set_caption("Ajedrez")

    juego = Partida(nombre_b, nombre_n)
    juego.situacion.pintar( ventana )
    juego.pintar_datos(ventana)
    pygame.display.flip()

    jugando = True
    figura_mov = Nada()
    sel = (-1,-1)
    while jugando :
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False  
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == BUTTON_LEFT:
                x = (event.pos[0]-INICIO_TABLERO)//LADO_CASILLA
                y = (event.pos[1]-INICIO_TABLERO)//LADO_CASILLA
                sel = (x, y)
                if (event.pos[0] in range(INICIO_TABLERO, FIN_TABLERO) and event.pos[1] in range(INICIO_TABLERO, FIN_TABLERO)):
                    if juego.situacion[sel[0] + 8 * sel[1]].getTipo() != Nada:
                        rect_x = INICIO_TABLERO + LADO_CASILLA*((event.pos[0]-INICIO_TABLERO)//LADO_CASILLA) # calculo la x del origen de la casilla en la que está el ratón  
                        rect_y = INICIO_TABLERO + LADO_CASILLA*((event.pos[1]-INICIO_TABLERO)//LADO_CASILLA) # calculo la y del origen de la casilla en la que está el ratón  
                        if (juego.jugador_b.turno and juego.situacion[sel[0] + 8 * sel[1]].getColor() == "b") or (juego.jugador_n.turno and juego.situacion[sel[0] + 8 * sel[1]].getColor() == "n"):
                            figura_mov = juego.situacion[sel[0] + 8 * sel[1]]
                            juego.situacion.modificar(Nada(), sel[0], sel[1])
                            juego.situacion.pintar(ventana)
                            juego.pintar_datos(ventana)
                            pygame.draw.rect(ventana, FONDO, (rect_x, rect_y , LADO_CASILLA , LADO_CASILLA), BORDE) # rectangular (height, width), (30, 30)
                            pygame.display.flip()
                        else:
                            print ("Pieza del color incorrecto")
                            sel = (-1,-1)
                    else:
                        print ("No hay pieza en la casilla")
                        sel = (-1,-1)
                else:
                    print ("Pulsacion fuera del tablero")
                    sel = (-1,-1)

            if event.type == pygame.MOUSEBUTTONUP and event.button == BUTTON_LEFT:
                if sel != (-1,-1) :
                    x = (event.pos[0]-INICIO_TABLERO)//LADO_CASILLA
                    y = (event.pos[1]-INICIO_TABLERO)//LADO_CASILLA
                    des = (x, y)
                    if ( event.pos[0] in range(INICIO_TABLERO, FIN_TABLERO) and event.pos[1] in range(INICIO_TABLERO, FIN_TABLERO)): 
                        resul_mov = figura_mov.chk_mov(juego.situacion, des[0], des[1]) 
                        if resul_mov == 1 :     
                            print("en destino no hay pieza")      
                            juego.situacion.modificar(figura_mov, des[0], des[1]) 
                            juego.cambia_turno()
                        elif resul_mov == 2 :
                            print ("en destino hay figura del mismo color")
                            juego.situacion.modificar(figura_mov, sel[0], sel[1])
                        elif resul_mov == 3 :
                            print ("en destino hay pieza de color contrario")
                            if juego.situacion[x + 8 * y].getTipo() == Rey:
                                jugando = False
                            juego.situacion.modificar(figura_mov, des[0], des[1]) 
                            if jugando:
                                juego.cambia_turno()
                            else:
                                if juego.jugador_b.turno:
                                    juego.ganado("b")
                                else:
                                    juego.ganado("n")
                        elif resul_mov == 4 :
                            print ("Pieza encontrada en el camino, movimiento no valido")
                            juego.situacion.modificar(figura_mov, sel[0], sel[1])
                        elif resul_mov == 9 :
                            print ("Movimiento ilegal para esa pieza")
                            juego.situacion.modificar(figura_mov, sel[0], sel[1])
                    else :
                        print ("Soltado fuera del tablero!")
                        juego.situacion.modificar(figura_mov, sel[0], sel[1])
                    figura_mov = Nada()
                    juego.situacion.pintar(ventana) 
                    juego.pintar_datos(ventana)
                    pygame.display.flip()
                else :
                    print ("No se había cogido pieza")

            if event.type == pygame.MOUSEMOTION:
                x = (event.pos[0] - LADO_CASILLA / 2)
                y = (event.pos[1] - LADO_CASILLA / 2)
                pos = (x, y)
                if ( figura_mov.getTipo() != Nada ):
                    juego.situacion.pintar(ventana)
                    juego.pintar_datos(ventana)
                    ventana.blit(figura_mov.imagen, pos)
                    pygame.draw.rect(ventana, FONDO, (pos[0], pos[1], LADO_CASILLA, LADO_CASILLA), BORDE)
                    pygame.display.flip()              
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


