# Aplicación CRUD  (Create, Read, Update, Delete) conectado a una base de datos 

from tkinter import END, Button, Label, StringVar, Tk 
from tkinter import ttk
from tkinter import Menu
import sys
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import usuarios 


class Usuarios:

    def __init__(self):
        self.root = Tk()
        self.conexion_usuario = usuarios.Usuario()
        self.root.title("Aplicación Registro Turismo")
        menubar = Menu(self.root, tearoff=0)
        self.root.config(menu = menubar)

        agregar_menu = Menu(menubar,tearoff=0)
        agregar_menu.add_command(label="600x500", command=self.pequeña)
        agregar_menu.add_command(label="800x800", command=self.grande)
        menubar.add_cascade(label="Tamaño",menu=agregar_menu)

        agregar_menu2 = Menu(menubar,tearoff=0)
        agregar_menu2.add_command(label="Gris", command=self.color_gris)
        agregar_menu2.add_command(label="Verde", command=self.color_verde)
        menubar.add_cascade(label="Colores",menu=agregar_menu2)

        agregar_menu3 = Menu(menubar, tearoff=0)
        agregar_menu3.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Salir",menu=agregar_menu3)


        self.cuaderno = ttk.Notebook(self.root)
        self.crear_usuario()
        self.consultar_usuario_codigo()
        self.recuperar_todo()
        self.borrar()
        self.modificar()
        self.cuaderno.grid(column=0,row=0, padx=10, pady=10)
        
        self.root.mainloop()

    def crear_usuario(self):
        self.pagina1 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina1, text="Carga de Usuario")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Turista")
        self.labelframe1.grid(column=0,row=0,padx=10, pady= 10)  

        self.dato_nombre1 = StringVar()
        self.etiqueta_nombre1 = Label(self.labelframe1, text="Nombre: ")
        self.etiqueta_nombre1.grid(column=0,row=2)
        self.entry_nombre1 = ttk.Entry(self.labelframe1, textvariable= self.dato_nombre1)
        self.entry_nombre1.grid(column=1,row=2, padx=10, pady=10)

        self.dato_nal1 = StringVar()
        self.etiqueta_country1 = Label(self.labelframe1, text="Nacionalidad: ")
        self.etiqueta_country1.grid(column=0,row=3)
        self.entry_country1 = ttk.Entry(self.labelframe1, textvariable= self.dato_nal1)
        self.entry_country1.grid(column=1,row=3, padx=10, pady=10)

        self.dato_estadia1 = StringVar()
        self.etiqueta_estadia1 = Label(self.labelframe1, text="Estadia / días: ")
        self.etiqueta_estadia1.grid(column=0,row=4)
        self.entry_estadia1 = ttk.Entry(self.labelframe1, textvariable= self.dato_estadia1)
        self.entry_estadia1.grid(column=1,row=4, padx=10, pady=10)

        self.dato_adquirido1 = StringVar()
        self.etiqueta_adquirido1 = Label(self.labelframe1, text="Servicio adquirido: ")
        self.etiqueta_adquirido1.grid(column=0,row=5)
        self.entry_adquirido1 = ttk.Entry(self.labelframe1, textvariable= self.dato_adquirido1)
        self.entry_adquirido1.grid(column=1,row=5, padx=10, pady=10)

        self.boton_crear = Button(self.labelframe1, text="Registrar", command=self.agregar)
        self.boton_crear.grid(column=0, row=6, padx=10, pady=10, sticky="we", columnspan=2)
    
    def agregar(self):
        """Conexión a la base de datos crear usuarios turistas"""

        datos = (self.dato_nombre1.get(), self.dato_nal1.get(),self.dato_estadia1.get(),self.dato_adquirido1.get())
        self.conexion_usuario.añadir_usuario(datos)
        messagebox.showwarning("Información", "Se ha registrado un nuevo visitante en la base de datos")
        self.dato_nombre1.set("")
        self.dato_nal1.set("")
        self.dato_estadia1.set("")
        self.dato_adquirido1.set("")

    def consultar_usuario_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina2, text="Consultar Usuario")
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Turista")
        self.labelframe2.grid(column=0,row=0,padx=10, pady= 10)  

        self.dato_codigo = StringVar()
        self.etiqueta_codigo = Label(self.labelframe2, text="Código: ")
        self.etiqueta_codigo.grid(column=0,row=1)
        self.entry_codigo = ttk.Entry(self.labelframe2, textvariable= self.dato_codigo)
        self.entry_codigo.grid(column=1,row=1, padx=10, pady=10)

        self.dato_nombre2 = StringVar()
        self.etiqueta_nombre2 = Label(self.labelframe2, text="Nombre: ")
        self.etiqueta_nombre2.grid(column=0,row=2)
        self.entry_nombre2 = ttk.Entry(self.labelframe2, textvariable= self.dato_nombre2, state="readonly")
        self.entry_nombre2.grid(column=1,row=2, padx=10, pady=10)

        self.dato_nal2 = StringVar()
        self.etiqueta_country2 = Label(self.labelframe2, text="Nacionalidad: ")
        self.etiqueta_country2.grid(column=0,row=3)
        self.entry_country2 = ttk.Entry(self.labelframe2, textvariable= self.dato_nal2, state="readonly")
        self.entry_country2.grid(column=1,row=3, padx=10, pady=10)

        self.dato_estadia2 = StringVar()
        self.etiqueta_estadia2 = Label(self.labelframe2, text="Estadia / días: ")
        self.etiqueta_estadia2.grid(column=0,row=4)
        self.entry_estadia2 = ttk.Entry(self.labelframe2, textvariable= self.dato_estadia2, state="readonly")
        self.entry_estadia2.grid(column=1,row=4, padx=10, pady=10)

        self.dato_adquirido2 = StringVar()
        self.etiqueta_adquirido2 = Label(self.labelframe2, text="Servicio adquirido: ")
        self.etiqueta_adquirido2.grid(column=0,row=5)
        self.entry_adquirido2 = ttk.Entry(self.labelframe2, textvariable= self.dato_adquirido2, state="readonly")
        self.entry_adquirido2.grid(column=1,row=5, padx=10, pady=10)

        self.boton_consultar_c = Button(self.labelframe2, text="Consultar", command=self.consulta)
        self.boton_consultar_c.grid(column=0, row=6, padx=10, pady=10, sticky="we", columnspan=2)
    
    def consulta(self):
        datos = (self.dato_codigo.get(), )
        respuesta = (self.conexion_usuario.ver_usuario(datos))

        if len(respuesta) > 0:
            self.dato_nombre2.set(respuesta[0][0])
            self.dato_nal2.set(respuesta[0][1])
            self.dato_estadia2.set(respuesta[0][2])
            self.dato_adquirido2.set(respuesta[0][3])
        else:
            messagebox.showinfo("Importante","El viajero que esta buscando no existe en la base de datos")


    def recuperar_todo(self):
        self.pagina3 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina3, text="Consultar Todos")
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Turista")
        self.labelframe3.grid(column=0,row=0)
        self.boton_crear = Button(self.labelframe3, text="Recuperar", command=self.imprimir_todo)
        self.boton_crear.grid(column=0, row=0, padx=10, pady=10, sticky="we", columnspan=2)
        self.scrolltext1 = ScrolledText(self.labelframe3, width=50, height = 10)
        self.scrolltext1.grid(column=0,row=1)

    def imprimir_todo(self):
        respuesta = self.conexion_usuario.recuperar_todo()        
        self.scrolltext1.delete(1.0, END)
        for fila in respuesta:
            
            self.scrolltext1.insert(END, "Código: "+ str(fila[0])+ "\nNombre: "+str(fila[1])+"\nNacionalidad: "+ str(fila[2])+ "\nEstancia: "+str(fila[3])+"\nProducto Adquirido: "+str(fila[4])+"\n\n")

    def borrar(self):
        self.pagina4 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina4,text="Eliminar Usuario")
        self.labelframe4 = ttk.LabelFrame(self.pagina4,text="Turista")
        self.labelframe4.grid(column=0, row=0, padx=10, pady=10)

        self.dato_codigo_b = StringVar()
        self.etiqueta_codigo_b = Label(self.labelframe4, text="Código: ")
        self.etiqueta_codigo_b.grid(column=0,row=1)
        self.entry_codigo_b = ttk.Entry(self.labelframe4, textvariable= self.dato_codigo_b)
        self.entry_codigo_b.grid(column=1,row=1, padx=10, pady=10)

        self.boton_borrar = Button(self.labelframe4, text="Eliminar", command=self.eliminar)
        self.boton_borrar.grid(column=0,row=2, padx=10, pady=10, sticky="we")
        
    def eliminar(self):
        datos = (self.dato_codigo_b.get(), )
        self.conexion_usuario.borrar_usuario(datos)
        messagebox.showinfo("Exitoso","El viajero registrado en la base de datos ha sido eliminado")
        self.dato_codigo_b.set("")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina5, text="Modificar Usuario")
        self.labelframe5 = ttk.LabelFrame(self.pagina5, text="Turista")
        self.labelframe5.grid(column=0,row=0,padx=10, pady= 10)  

        self.dato_codigo5 = StringVar()
        self.etiqueta_codigo5 = Label(self.labelframe5, text="Código: ")
        self.etiqueta_codigo5.grid(column=0,row=1)
        self.entry_codigo5 = ttk.Entry(self.labelframe5, textvariable= self.dato_codigo5)
        self.entry_codigo5.grid(column=1,row=1, padx=10, pady=10)

        self.dato_nombre5 = StringVar()
        self.etiqueta_nombre5 = Label(self.labelframe5, text="Nombre: ")
        self.etiqueta_nombre5.grid(column=0,row=2)
        self.entry_nombre5 = ttk.Entry(self.labelframe5, textvariable= self.dato_nombre5)
        self.entry_nombre5.grid(column=1,row=2, padx=10, pady=10)

        self.dato_nal5 = StringVar()
        self.etiqueta_country5 = Label(self.labelframe5, text="Nacionalidad: ")
        self.etiqueta_country5.grid(column=0,row=3)
        self.entry_country5 = ttk.Entry(self.labelframe5, textvariable= self.dato_nal5)
        self.entry_country5.grid(column=1,row=3, padx=10, pady=10)

        self.dato_estadia5 = StringVar()
        self.etiqueta_estadia5 = Label(self.labelframe5, text="Estadia / días: ")
        self.etiqueta_estadia5.grid(column=0,row=4)
        self.entry_estadia5 = ttk.Entry(self.labelframe5, textvariable= self.dato_estadia5)
        self.entry_estadia5.grid(column=1,row=4, padx=10, pady=10)

        self.dato_adquirido5 = StringVar()
        self.etiqueta_adquirido5 = Label(self.labelframe5, text="Servicio adquirido: ")
        self.etiqueta_adquirido5.grid(column=0,row=5)
        self.entry_adquirido5 = ttk.Entry(self.labelframe5, textvariable= self.dato_adquirido5)
        self.entry_adquirido5.grid(column=1,row=5, padx=10, pady=10)

        self.boton_consultar_mc = Button(self.labelframe5, text="Consultar", command=self.consulta_mod)
        self.boton_consultar_mc.grid(column=0, row=6, padx=10, pady=10 )
        self.boton_consultar_m = Button(self.labelframe5, text="Modificar", command=self.modificar_conexion)
        self.boton_consultar_m.grid(column=1, row=6, padx=10, pady=10 )
    
    def consulta_mod(self):
        datos = (self.dato_codigo5.get(),)
        respuesta = self.conexion_usuario.ver_usuario(datos)

        if len(respuesta)>0:
            
            self.dato_nombre5.set(respuesta[0][0])
            self.dato_nal5.set(respuesta[0][1])
            self.dato_estadia5.set(respuesta[0][2])
            self.dato_adquirido5.set(respuesta[0][3])
        else:
            messagebox.showinfo("Ooops!","El viajero que desea modificar no se encuentra, intente nuevamente.")

    def modificar_conexion(self):
        datos = (self.dato_nombre5.get(),self.dato_nal5.get(),self.dato_estadia5.get(),
                self.dato_adquirido5.get(),self.dato_codigo5.get())
        respuesta = self.conexion_usuario.modificar_usuario(datos)
        if respuesta==1:
            messagebox.showinfo("Información", "Se modificó la información del viajero")
            self.dato_codigo5.set("")
            self.dato_nombre5.set("")
            self.dato_nal5.set("")
            self.dato_estadia5.set("")
            self.dato_adquirido5.set("")
        else:
            messagebox.showinfo("Información", "No existe un turista con dicho código")
        


    def pequeña(self):
        self.root.geometry("600x500")
    def grande(self):
        self.root.geometry("800x800")
    def color_gris(self):
        self.root.config(bg="#878E88")
    def color_verde(self):
        self.root.config(bg="#C4EBC8")
    def salir(self):
        sys.exit(0)

  
        
usuario1 = Usuarios()