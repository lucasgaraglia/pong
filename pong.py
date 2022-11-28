import pygame, random

#   tamaño de la ventana
window_size = (800, 600)
#   colores predefinidos
white = (255, 255, 255)
black = (0, 0, 0)
#   defino el reloj
clock = pygame.time.Clock()
#   fps (uso esta variable al final, cuando llamo al objeto clock)
fps = 60
#   ícono de la ventana
icono = pygame.image.load("./icono/pong.png")
#   fondo de la ventana
background = pygame.image.load("./background/espacio_background.png")
#   valores predefinidos; velocidad y score máximo
velocidad = 9
max_score = 3

#   clase: pelota
class PelotaPong:

    #   constructor
    def __init__(self):
        #   posición de spawn de la pelota
        self.x = window_size[0] / 2
        self.y = window_size[1] / 2
        #   radio y diámetro de la pelota (los uso luego para verificar colisiones y rebotes)
        self.diameter = 10
        self.radius = self.diameter / 2
        #   al no depender de ningún evento, la velocidad X de la pelota se asigna desde el principio,
        #   acompañada del módulo random para no generar preferencias.
        self.x_vel = random.choice([velocidad * (-1), velocidad])
        #   para no dificultar el saque, la pelota irá recta por el eje X (velocidad Y = 0)
        self.y_vel = 0

    #   método movimiento
    def movimiento(self):

        #   posición + velocidad = nueva posición.
        self.x += self.x_vel
        self.y += self.y_vel
    
    #   método reiniciar y acumular score
    def reiniciar(self, sc_j1, sc_j2):
        #   verifico si la pelota rebalsó el tamaño de la pantalla y reinicio su posición.
        #   además, cuento el score del respectivo jugador
        if self.x > 800:
            self.x = window_size[0] / 2
            self.y = window_size[1] / 2
            self.x_vel *= -1
            self.y_vel = 0

            sc_j1 += 1
        elif self.x < 0:
            self.x = window_size[0] / 2
            self.y = window_size[1] / 2
            self.x_vel *= -1
            self.y_vel = 0

            sc_j2 += 1
        
        return sc_j1, sc_j2

    #   método rebotar
    def rebotar(self, jugador1, jugador2):

        #   rebote con el techo
        if self.y > window_size[1] - self.radius or self.y < self.radius:
            self.y_vel *= -1
        
        #   colisiones con los jugadores + cálculo de intensidad del rebote con respecto
        #   al ángulo del choque
        if self.x_vel < 0:
            if self.y >= jugador1.y and self.y <= jugador1.y + jugador1.height:
                if self.x - self.radius <= jugador1.x + jugador1.width:
                    self.x_vel *= -1

                    mitad_y = jugador1.y + jugador1.height / 2
                    diferencia_y = mitad_y - self.y
                    factor_reduccion = (jugador1.height / 2) / velocidad
                    y_vel = diferencia_y / factor_reduccion
                    self.y_vel = y_vel * -1

        else:
            if self.y >= jugador2.y and self.y <= jugador2.y + jugador2.height:
                if self.x + self.radius >= jugador2.x:
                    self.x_vel *= -1

                    mitad_y = jugador2.y + jugador2.height / 2
                    diferencia_y = mitad_y - self.y
                    factor_reduccion = (jugador2.height / 2) / velocidad
                    y_vel = diferencia_y / factor_reduccion
                    self.y_vel = y_vel * -1

    #   método dibujar
    def dibujar(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.diameter)



#   clase: jugador
class JugadorPong:

    #   constructor
    def __init__(self, x):
        #   tamaño del jugador
        self.width = 20
        self.height = 160
        #   la coordenada X se pasa después, ya que cada jugador estará en una posición distinta
        self.x = x
        self.y = window_size[1] / 2 - self.height / 2
        #   velocidad default = 0
        self.y_vel = 0

    #   método movimiento
    def movimiento(self):
        #   el único movimiento del jugador es sobre el eje Y. posición + velocidad = nueva posición
        self.y += self.y_vel

        #   limito el movimiento con los bordes de la pantalla
        if self.y < 0:
            self.y = 0
        if (self.y + self.height) > window_size[1]:
            self.y = window_size[1] - self.height
    
    #   método dibujar
    def dibujar(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
    

#   verificar score y mostrar texto
def check_score(screen, sc_j1, sc_j2, score_font, pelota, close):

    #   si el score del jugador llega al score máximo, congelar la pelota y mostrar
    #   la pantalla en negro, seguido de un texto que contiene el ganador y los
    #   controles pertinentes a la desición de continuación del juego.
    #   La verificación de las teclas están junto a las demás, ya que no encontraba
    #   solución al error causado al verificarlas acá
    if sc_j1 >= max_score:
        ganador = "Jugador 1"
        ganador_text = score_font.render(f"Ganador: {ganador}", True, white)
        opciones = score_font.render("R: reiniciar, Q: Salir", True, white)

        pelota.x_vel = 0
        pelota.y_vel = 0

        screen.fill(black)
        screen.blit(ganador_text, (window_size[0] / 2 - ganador_text.get_width() / 2, 20))
        screen.blit(opciones, (window_size[0] / 2 - opciones.get_width() / 2, 100))
        
    if sc_j2 >= max_score:
        ganador = "Jugador 2"
        ganador_text = score_font.render(f"Ganador: {ganador}", True, white)
        opciones = score_font.render("R: reiniciar, Q: Salir", True, white)

        pelota.x_vel = 0
        pelota.y_vel = 0

        screen.fill(black)
        screen.blit(ganador_text, (window_size[0] / 2 - ganador_text.get_width() / 2, 20))
        screen.blit(opciones, (window_size[0] / 2 - opciones.get_width() / 2, 100))

#   función programa principal
def main():
    #   inicializo el módulo pygame
    pygame.init()
    #   defino la ventana
    screen = pygame.display.set_mode(window_size)
    #   condición del bucle while
    close = False
    #   titulo e ícono de la ventana
    pygame.display.set_caption("Pong.")
    pygame.display.set_icon(icono)

    #   defino fuente para la impresión del score
    score_font = pygame.font.SysFont("comicsans", 50)

    #   defino los objetos
    pelota = PelotaPong()
    jugador1 = JugadorPong(20)
    jugador2 = JugadorPong(760)

    #   defino los scores
    sc_j1 = 0
    sc_j2 = 0


    #   bucle de ejecución del juego
    while not close:

        #   llamo a todos los métodos de los objetos
        pelota.movimiento()
        pelota.rebotar(jugador1, jugador2)
        jugador1.movimiento()
        jugador2.movimiento()
        #   la función reiniciar la llamo en las variables de los scores para acumular
        sc_j1, sc_j2 = pelota.reiniciar(sc_j1, sc_j2)

        #   texto del score del jugador. dentro del while para que se actualice
        jugador1_score_text = score_font.render(f"{sc_j1}", True, white)
        jugador2_score_text = score_font.render(f"{sc_j2}", True, white)



        #   detecto teclas
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
            
            #   mientras se mantiene la tecla
            if event.type == pygame.KEYDOWN:

                #   Jugador 1
                if event.key == pygame.K_w:
                    jugador1.y_vel = -7
                if event.key == pygame.K_s:
                    jugador1.y_vel = 7

                #   Jugador 2
                if event.key == pygame.K_UP:
                    jugador2.y_vel = -7
                if event.key == pygame.K_DOWN:
                    jugador2.y_vel = 7
                
                #   teclas de continuación. se habilitan al terminar la partida
                if sc_j1 >= max_score or sc_j2 >= max_score:
                    if event.key == pygame.K_r:
                        close = True
                        main()
                    if event.key == pygame.K_q:
                        close = True
            
            #   cuando se suelta la tecla
            if event.type == pygame.KEYUP:

                #   Jugador 1
                if event.key == pygame.K_w:
                    jugador1.y_vel = 0
                if event.key == pygame.K_s:
                    jugador1.y_vel = 0

                #   Jugador 2
                if event.key == pygame.K_UP:
                    jugador2.y_vel = 0
                if event.key == pygame.K_DOWN:
                    jugador2.y_vel = 0


        
        #   impresiones
        #       fondo
        screen.blit(background, [0, 0])
        #       score jugador 1
        screen.blit(jugador1_score_text, (window_size[0] / 4 - jugador1_score_text.get_width() / 2, 20))
        #       score jugador 2
        screen.blit(jugador2_score_text, (window_size[0] * (3/4) - jugador2_score_text.get_width() / 2, 20))
        #       pelota
        pelota.dibujar(screen, white)
        #       jugador 1
        jugador1.dibujar(screen, white)
        #       jugador 2
        jugador2.dibujar(screen, white)

        #   llamo a la función check score
        check_score(screen, sc_j1, sc_j2, score_font, pelota, close)
        
        #   actualizo la pantalla
        pygame.display.flip()
        #   defino el ciclo del reloj
        clock.tick(fps)
    
    pygame.quit()

