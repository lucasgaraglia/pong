import pong
from tkinter import *
from tkinter import font
from tkinter import ttk


#   ventana principal del menú
def ventana_principal():
    root = Tk()
    #   imagen de ícono
    root.iconbitmap("./icono/pong.ico")
    #   titulo ventana
    root.title("Pong")
    #   color de fondo
    root.config(bg="lightgrey")
    #   tamaño de ventana y posición (para resolución 1920x1080. en otro caso, sacar '+760+200')
    root.geometry("400x500+760+200")

    #   fuente default para la ventana
    root.defaultFont = font.nametofont("TkDefaultFont")
    root.defaultFont.configure(family="Verdana", size=14)

    #   título Pong
    titulo_pong = Label(root, text="Pong", bg="lightgrey", font=("Verdana", 22))
    titulo_pong.pack(pady=10, padx=0)

    #   función abrir juego
    def abrir_pong():
        root.withdraw()
        pong.main()
        ventana_principal()
            
        
    #   botón jugar
    boton_jugar = Button(root, text="Jugar", bg="lightgreen", width=16, height=1, command=abrir_pong, font=("Verdana", 14))
    boton_jugar.pack(pady=10, padx=0)

    #   función abrir ventana configuración
    def abrir_config():
        root.withdraw()
        ventana_configuracion()

    #   botón configuracion
    boton_config = Button(root, text="Configuración", bg="#e4eda1", width=16, height=1, command=abrir_config, font=("Verdana", 14))
    boton_config.pack(pady=10, padx=0)

    #   funcion abrir ventana tutorial
    def abrir_tutorial():
        root.withdraw()
        ventana_tutorial()

    #   botón tutorial
    boton_tuto = Button(root, text="Tutorial", bg="#d4a1ed", width=16, height=1, command=abrir_tutorial, font=("Verdana", 14))
    boton_tuto.pack(pady=10, padx=0)

    #   créditos
    creditos = Label(root, text="Pong.\nLucas Garaglia y Francisco Rocchi,\nSistemas Digitales I, 5to 3ra, EESTN1 VL.\nProf: Nicolás Salimbeni.", bg="lightgrey", font=("Verdana", 8))
    creditos.pack(pady=40, padx=0)





    root.mainloop()

#   ventana configuración
def ventana_configuracion():
    root_c = Tk()
    #   ícono
    root_c.iconbitmap("./icono/pong.ico")
    #   título
    root_c.title("Configuración")
    #   color de fondo
    root_c.config(bg="lightgrey")
    #   tamaño de ventana y posición (para resolución 1920x1080. en otro caso, sacar '+760+200')
    root_c.geometry("400x500+760+200")

    #   fuente default de la ventana
    root_c.defaultFont = font.nametofont("TkDefaultFont")
    root_c.defaultFont.configure(family="Verdana", size=18)

    #   titulo configuracion
    titulo_config = Label(root_c, text="Configuración", bg="lightgrey", font=("Verdana", 22))
    titulo_config.pack(pady=10, padx=0)


    #   título velocidad pelota
    titulo_velocidad = Label(root_c, text="Velocidad de la pelota", bg="lightgrey", font=("Verdana", 14))
    titulo_velocidad.pack(padx=10, pady=10)

    #   combobox velocidad
    combobox_velocidad = ttk.Combobox(root_c, state="readonly", values=["Lento", "Normal", "Rápido", "Muy Rápido"], font=("Verdana", 12))
    combobox_velocidad.current(1)
    combobox_velocidad.pack()

    #   título max score
    titulo_score = Label(root_c, text="Máximo score", bg="lightgrey", font=("Verdana", 14))
    titulo_score.pack(padx=10, pady=10)

    #   combobox max score
    combobox_score = ttk.Combobox(root_c, state="readonly", values=["3", "5", "10"], font=("Verdana", 12))
    combobox_score.current(0)
    combobox_score.pack()

    #   función guardar
    def submit():


        #   velocidad pelota
        if combobox_velocidad.get() == "Lento":
            pong.velocidad = 6
        elif combobox_velocidad.get() == "Normal":
            pong.velocidad = 9
        elif combobox_velocidad.get() == "Rápido":
            pong.velocidad = 12
        elif combobox_velocidad.get() == "Muy Rápido":
            pong.velocidad = 15
        else:
            pass
        
        
        #   score
        if combobox_score.get() == "3":
            pong.max_score = 3
        elif combobox_score.get() == "5":
            pong.max_score = 5
        elif combobox_score.get() == "10":
            pong.max_score = 10
        else:
            pass


    #   botón guardar
    boton_submit = Button(root_c, text="Guardar", width=15, font=("Verdana", 12), command=submit)
    boton_submit.pack(pady=30)

    #   función volver
    def volver():
        root_c.withdraw()
        ventana_principal()

    #   botón volver
    boton_volver = Button(root_c, text="Volver", width=15, font=("Verdana", 12), command=volver)
    boton_volver.pack(pady=0)



    root_c.mainloop()

#   ventana tutorial
def ventana_tutorial():

    root_t = Tk()
    #   ícono
    root_t.iconbitmap("./icono/pong.ico")
    #   título
    root_t.title("Tutorial")
    #   configuración
    root_t.config(bg="lightgrey")
    #   tamaño de ventana y posición (para resolución 1920x1080. en otro caso, sacar '+760+200')
    root_t.geometry("400x500+760+200")

    #   título jugador 1
    titulo_jugador1 = Label(root_t, text="Jugador 1", bg="lightgrey", font=("Verdana", 18), fg="red")
    titulo_jugador1.pack(pady=20)
    #   controles jugador 1
    controles_jugador1 = Label(root_t, text="W - arriba\nS - abajo", bg="lightgrey", font=("Verdana", 12))
    controles_jugador1.pack(pady=0)





    #   título jugador 2
    titulo_jugador2 = Label(root_t, text="Jugador 2", bg="lightgrey", font=("Verdana", 18), fg="red")
    titulo_jugador2.pack(pady=20)
    #   controles jugador 2
    controles_jugador2 = Label(root_t, text="↑ - arriba\n↓ - abajo", bg="lightgrey", font=("Verdana", 12))
    controles_jugador2.pack(pady=0)

    #   función volver
    def volver():
        root_t.withdraw()
        ventana_principal()

    #   botón volver
    boton_volver = Button(root_t, text="Volver", width=15, font=("Verdana", 12), command=volver)
    boton_volver.pack(pady=40)



    root_t.mainloop()

#   llamo a la función que contiene la ventana principal
while pong.close:
    ventana_principal()

