from tkinter import *
from tkinter import messagebox
import sqlite3 

def conexionBBDD():

	miConexion=sqlite3.connect("Clientes")

	miCursor=miConexion.cursor()

	try:

		miCursor.execute(''' 
			CREATE TABLE DATOSCLIENTES (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRES VARCHAR(50),
			APELLIDOS VARCHAR(50),
			TELÉFONO VARCHAR(10),
			DIRECCIÓN VARCHAR(50),
			CONTACTO VARCHAR(100))
			''')

		messagebox.showinfo("BBDD", "BBDD creada con exito")

	except:

		messagebox.showwarning("Atencion!", "La BBDD ya existe")

def salirAplicacion():

	valor=messagebox.askquestion("Salir", "Deseas salir de la aplicacion?")

	if valor=="yes":
		root.destroy()

def limpiarCampos():

	miId.set("")
	miNombre.set("")
	miApellido.set("")
	miTelefono.set("")
	miDireccion.set("")
	textoContacto.delete(1.0, END)

def crear():

	miConexion=sqlite3.connect("Clientes")

	miCursor=miConexion.cursor()

	datos=miNombre.get(),miApellido.get(),miTelefono.get(),miDireccion.get(),textoContacto.get("1.0",END)

	miCursor.execute("INSERT INTO DATOSCLIENTES VALUES(NULL,?,?,?,?,?)",(datos))	

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con exito")

def leer():

	miConexion=sqlite3.connect("Clientes")

	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOSCLIENTES WHERE ID=" + miId.get())

	elCliente=miCursor.fetchall()

	for cliente in elCliente:

		miId.set(cliente[0])
		miNombre.set(cliente[1])
		miApellido.set(cliente[2])
		miTelefono.set(cliente[3])
		miDireccion.set(cliente[4])
		textoContacto.insert(1.0, cliente[5])

	miConexion.commit()

def actualizar():

	miConexion=sqlite3.connect("Clientes")

	miCursor=miConexion.cursor()

	datos=miNombre.get(),miApellido.get(),miTelefono.get(),miDireccion.get(),textoContacto.get("1.0",END)

	miCursor.execute("UPDATE DATOSCLIENTES SET NOMBRES=?,APELLIDOS=?,TELÉFONO=?,DIRECCIÓN=?,CONTACTO=?"+
		"WHERE ID="	+ miId.get(),(datos))

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro actualizado con éxito")

def eliminar():

	miConexion=sqlite3.connect("Clientes")

	miCursor=miConexion.cursor()

	miCursor.execute("DELETE FROM DATOSCLIENTES WHERE ID=" + miId.get())

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro borrado con exito")

root=Tk()
root.title("ABC S.A.")
root.resizable(0,0)
root.iconbitmap("icono.ico")

fondo=PhotoImage(file="fondo.gif")
fondoLabel=Label(root, image=fondo).place(x=0,y=0)

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miTelefono=StringVar()
miDireccion=StringVar()

cuadroID=Entry(root, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(fg="black",cursor="hand2",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

cuadroNombre=Entry(root, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(cursor="hand2",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

cuadroApellido=Entry(root, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(cursor="hand2",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

cuadroTelefono=Entry(root, textvariable=miTelefono)
cuadroTelefono.grid(row=3, column=1, padx=10, pady=10)
cuadroTelefono.config(cursor="hand2",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

cuadroDireccion=Entry(root, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)
cuadroDireccion.config(cursor="hand2",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

textoContacto=Text(root, width=20, height=5)
textoContacto.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(root, command=textoContacto.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoContacto.config(yscrollcommand=scrollVert.set,cursor="hand2",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

idLabel=Label(root, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
idLabel.config(bg="black",fg="white",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

nombreLabel=Label(root, text="NOMBRES:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
nombreLabel.config(bg="black",fg="white",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

apellidoLabel=Label(root, text="APELLIDOS:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
apellidoLabel.config(bg="black",fg="white",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

telefonoLabel=Label(root, text="TELÉFONO:")
telefonoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
telefonoLabel.config(bg="black",fg="white",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

direccionLabel=Label(root, text="DIRECCIÓN:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)
direccionLabel.config(bg="black",fg="white",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

contactoLabel=Label(root, text="CONTACTO:")
contactoLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)
contactoLabel.config(bg="black",fg="white",relief="sunken",bd=5,font=("Times New Roman",12,"bold italic"))

botonlimpiar=Button(root, text="LIMPIAR CAMPOS", command=limpiarCampos)
botonlimpiar.grid(row=6, column=1, padx=10, pady=10)
botonlimpiar.config(justify="center", bg="black", fg="white",cursor="hand2",relief="groove",bd=10,font=("Times New Roman",12,"bold italic"))

root.mainloop()