
from tkinter.ttk import Label, LabelFrame, Entry
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import *


from Clientes import *
from Conexion import *


class FormularioClientes:


# usamos la variable global para poder modificar los valores dentro de las funciones (  def Formulario(),
#                                                                                   def guardarRegistros(),            #                                                                               def actualizarTreeView(),
#                                                                                   def seleccionarRegistro(),            #                                                                               def eliminarRegistros(),
#                                                                                   def modificarRegistros())
    global base
    base = None

    global textBoxId
    textBoxId = None

    global textBoxNombres
    textBoxNombres = None

    global textBoxApellidos
    textBoxApellidos = None

    global combo
    combo = None

    global groupBox
    groupBox = None

    global tree
    tree = None


def Formulario():
    global textBoxId

    global textBoxNombres
    global textBoxApellidos

    global combo
    global groupBox

    global tree

    try:
        base = tk.Tk()
        base.geometry("1200x190")
        base.title("Formulario Python")
        groupBox = LabelFrame(base,
                              text="Datos del personal",
                              padx=5,
                              pady=5)
        groupBox.grid(row=0,
                      column=0,
                      pady=10,
                      padx=10)

        # Id
        # etiqueta Id

        labelId = Label(groupBox,
                        text="Id:",
                        width=13,
                        font=("arial", 12))

        # Mostramos por pantalla en el grid en columna
        labelId.grid(row=0,
                     column=0)
        # Configuramos la caja de entrada de datos
        textBoxId = Entry(groupBox)
        textBoxId.grid(row=0,
                       column=1)
        # NOMBRE
        # etiqueta nombres
        labelNombres = Label(groupBox,
                             text="Nombre:",
                             width=13,
                             font=("arial", 12))

        # Mostramos por pantalla en el grid en columna
        labelNombres.grid(row=1,
                          column=0)
        # Configuramos la caja de entrada de datos
        textBoxNombres = Entry(groupBox)
        textBoxNombres.grid(row=1,
                            column=1)
        # APELLIDOS
        # etiqueta apellidos
        labelApellidos = Label(groupBox,
                               text="Apellidos:",
                               width=13,
                               font=("arial", 12))

        # Mostramos por pantalla en el grid en columna
        labelApellidos.grid(row=2,
                            column=0)
        # Configuramos la caja de entrada de datos
        textBoxApellidos = Entry(groupBox)
        textBoxApellidos.grid(row=2,
                              column=1)
        # SEXO
        # etiqueta sexo
        labelSexo = Label(groupBox,
                          text="Sexo:",

                          width=13,
                          font=("arial", 12))

        # Mostramos por pantalla en el grid en columna
        labelSexo.grid(row=3,
                       column=0)
        # Para poder seleccionar el sexo de la persona (widget) usamos el paquete StringVar
        seleccionSexo = tk.StringVar()
        # usamos el combobox para tener un  panel desplegable, en este  caso para elegir si el genero es masc o fem
        combo = ttk.Combobox(groupBox,
                             values=["Masculino", "Femenino"],
                             textvariable=seleccionSexo)

        combo.grid(row=3,
                   column=1)

        seleccionSexo.set("Elige una opción")
        # Configuramos los botones Guardar/Modificar y Eliminar
        # GUARDAR
        botonGuardar = tk.Button(groupBox,

                                 text="Guardar",
                                 width=10,
                                 command=guardarRegistros)

        botonGuardar.grid(row=4, column=0)

        # MODIFICAR
        botonModificar = tk.Button(groupBox,
                                   text="Modificar",
                                   width=10,
                                   command=modificarRegistros)
        botonModificar.grid(row=4, column=1)

        # ELIMINAR
        botonEliminar = tk.Button(groupBox,
                                  text="Eliminar",
                                  width=10,
                                  command=eliminarRegistros)
        botonEliminar.grid(row=4, column=2)

        # creamos una caja en el que englobamos id,Nombre,Apellidos y sexo
        groupBox = LabelFrame(base, text="Lista del personal", padx=5, pady=5)
        groupBox.grid(row=0, column=1, padx=5, pady=5)
        # configuramos las columnas con treeview
        tree = ttk.Treeview(groupBox,
                            columns=("Id", "Nombres", "Apellidos", "Sexo"),
                            show='headings',
                            height=5, )
        # Aquí se configura la posición de los datos del dataview

        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Id")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Nombre/s")
        tree.column("#3", anchor=tk.CENTER)

        tree.heading("#3", text="Apellido/s")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Sexo")

        # agregamos los datos a la tabla
        # mostramos la tabla

        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)
        # Usamos el bind para enlazar eventos,

        # en este caso la configuración de columna en treeview (TreeviewSelect) y la funcion 'seleccionar registro'
        tree.pack()  # EL pack muestra lo correspondiente al tree que hemos escrito anteriormente

        base.mainloop()
        # Hay que tener en cuenta que el 'except' mostrado a continuación sería el similar al try-catch en Java y se


    # utiliza para manejar excepciones/errores que pueden ocurrir durante la ejecución del código
    except ValueError as error:
        print("Error al mostrar la interface,error {}".format(error))


def guardarRegistros():
    global textBoxNombres, textBoxApellidos, combo, groupBox

    try:
        # verificamos si los widgets estan incializados
        if textBoxNombres is None or textBoxApellidos is None or combo is None:
            print("Los widgets no están inicializados")
            return

        # Las siguientes variables (nombres, apellidos,sexo) obtienen cada uno de los campos correspondientes introducidos en el entry y los guarda
        nombres = textBoxNombres.get()
        apellidos = textBoxApellidos.get()
        sexo = combo.get()

        # Llamamos a la clase CClientes y a la función ingresarClientes mostrando por pantalla el mensaje 'Los datos fueron guardados'
        CClientes.ingresarClientes(nombres, apellidos, sexo)
        messagebox.showinfo("informacion", "Los datos fueron guardados")

        actualizarTreeView()

        # limpiamos los campos

        textBoxNombres.delete(0, END)
        textBoxApellidos.delete(0, END)

    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))


def actualizarTreeView():
    global tree
    try:
        #borramos todos los elementos actuales del treeView
        tree.delete(*tree.get_children())

        #obtenemos los nuevos datos que deseamos mostrar
        datos= CClientes.mostrarClientes()

        #Insertar los nuevos datos en el treeview
        for row in CClientes.mostrarClientes():
            tree.insert("","end",values = row)

    except ValueError as error:
        print("Error al actualizar la tabla {}".format(error))


def seleccionarRegistro(event):
    try:
        #obtenemos el ID del elemento seleccionado
        itemSeleccionado = tree.focus()

        if  itemSeleccionado:
            #obtenemos los valores por columna
            values = tree.item(itemSeleccionado)['values']

            #Mostramos los valores en los widgets Entry

            textBoxId.delete(0,END)
            textBoxId.insert(0,values[0])

            textBoxNombres.delete(0, END)
            textBoxNombres.insert(0, values[1])

            textBoxApellidos.delete(0, END)
            textBoxApellidos.insert(0, values[2])
            combo.set(values[3])

    except ValueError as error:
        print("Error al seleccionar el registro {}".format(error))


def modificarRegistros():
    global textBoxId,textBoxNombres, textBoxApellidos, combo, groupBox

    try:
        # verificamos si los widgets estan inicializados o no
        if textBoxId is None or textBoxNombres is None or textBoxApellidos is None or combo is None:
            print("Los widgets no están inicializados")
            return

        idUsuario = textBoxId.get()
        nombres = textBoxNombres.get()
        apellidos = textBoxApellidos.get()
        sexo = combo.get()

        # Llamamos a la clase CClientes y a la función ingresarClientes mostrando por pantalla el mensaje 'Los datos fueron actualizados'
        CClientes.modificarClientes(idUsuario,nombres,apellidos,sexo)
        messagebox.showinfo("informacion", "Los datos fueron actualizados")

        actualizarTreeView()


        textBoxId.delete(0,END)
        textBoxNombres.delete(0, END)
        textBoxApellidos.delete(0, END)

    except ValueError as error:
        print("Error al modificar los datos {}".format(error))

def eliminarRegistros():
    global textBoxId, textBoxNombres, textBoxApellidos

    try:
        # verificamos si los widgets estan inciializados
        if textBoxId is None:
            print("Los widgets no están inicializados")
            return

        idUsuario = textBoxId.get()


        CClientes.eliminarClientes(idUsuario)
        messagebox.showinfo("informacion", "Los datos fueron eliminados")

        actualizarTreeView()

        #
        textBoxId.delete(0,END)
        textBoxNombres.delete(0, END)
        textBoxApellidos.delete(0, END)

    except ValueError as error:
        print("Error al eliminar los datos {}".format(error))

Formulario()

