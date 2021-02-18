from juego import *
import pygame_textinput

DIM_VENTANA_INI = (400,225)  # Dimensiones de la ventana
DIM_CUADRO_BLANCAS = ( 50, 50, 200, 25)
DIM_CUADRO_NEGRAS = (50, 150, 200, 25)
DIM_BOTON = (300, 50, 50, 125)
BLANCO_INI = (255, 255, 255)
NEGRO_INI = (0,0,0)
BLANCO_INI_SEL = (249, 247, 195)
FUENTE = 'freesansbold.ttf'

def leer_texto ( superficie, caja, dimensiones):
    print("Escribiendo ")
    escribiendo = True
    while escribiendo:
        events = pygame.event.get()
        for evento in events:
            if evento.type == pygame.QUIT:
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == BUTTON_LEFT:
                escribiendo = False

        if caja.update(events):
            escribiendo = False
        pygame.draw.rect ( superficie, BLANCO_INI_SEL, dimensiones)
        superficie.blit(caja.get_surface(), (dimensiones[0] + 5, dimensiones[1]))
        pygame.display.update()
    return caja.get_text()  

def main():

    pygame.init()

    ventana_ini = pygame.display.set_mode(DIM_VENTANA_INI)    
    clock = pygame.time.Clock()

    pygame.display.set_caption("Ajedrez")

    ti_nombre_b = pygame_textinput.TextInput(font_family=FUENTE,max_string_length=8)
    ti_nombre_n = pygame_textinput.TextInput(font_family=FUENTE,max_string_length=8)
    ventana_ini.fill(FONDO)

    fuente = pygame.font.Font(FUENTE, 20)
    lbl_blancas = fuente.render('Jugador con blancas', True, NEGRO_INI, FONDO)
    lbl_negras = fuente.render('Jugador con negras', True, NEGRO_INI, FONDO)
    caja_blancas = pygame.draw.rect(ventana_ini, BLANCO_INI, DIM_CUADRO_BLANCAS)
    caja_negras = pygame.draw.rect ( ventana_ini, BLANCO_INI, DIM_CUADRO_NEGRAS)
    caja_boton = pygame.draw.rect ( ventana_ini, BLANCO_INI, DIM_BOTON)
    
    configurando = True
    a_jugar = False
    while configurando:
        ventana_ini.blit ( lbl_blancas, (50,25))
        ventana_ini.blit ( lbl_negras, (50,125))
        pygame.draw.rect ( ventana_ini, BLANCO_INI, caja_blancas)
        pygame.draw.rect ( ventana_ini, BLANCO_INI, caja_negras)
        pygame.draw.rect ( ventana_ini, BLANCO_INI, caja_boton)
        ventana_ini.blit ( ti_nombre_b.get_surface(), (55, DIM_CUADRO_BLANCAS[1]))
        ventana_ini.blit ( ti_nombre_n.get_surface(), (55, DIM_CUADRO_NEGRAS[1]))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                configurando = False  
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == BUTTON_LEFT:
                if caja_blancas.collidepoint(event.pos[0], event.pos[1]):
                    print(leer_texto(ventana_ini, ti_nombre_b,DIM_CUADRO_BLANCAS))
                if caja_negras.collidepoint(event.pos[0], event.pos[1]):
                    print(leer_texto(ventana_ini, ti_nombre_n,DIM_CUADRO_NEGRAS))
                if caja_boton.collidepoint(event.pos[0], event.pos[1]):
                    if ti_nombre_b.get_text() != "" and ti_nombre_n.get_text() != "":
                        configurando = False
                        a_jugar = True

    if a_jugar:
        jugar(ti_nombre_b.get_text(), ti_nombre_n.get_text())


if __name__ == "__main__":
    main()
