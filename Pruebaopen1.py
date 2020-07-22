import sys
import os
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk


class ButtonsMenuInterfaz(tk.Toplevel):

	def __init__(self, master):
		master.title("Opciones")
		self.master = master
		self.labelTop = Label(text="Elija una de las Opciones:")
		self.labelTop.grid(row=2, column=0, sticky="e", padx=10, pady=10)
		self.labelTop.pack()
		self.b1 = Button(self.master, text="Enviar Comuncación", command=self.EnviarComunicación, padx=10, pady=10)
		self.b2 = Button(self.master, text="Agregar Registro de Alumno", command=self.NuevoRegistro, padx=10, pady=10)
		self.b3 = Button(self.master, text="Eliminar Alumno", command=self.elimAlumno, padx=10, pady=10)
		self.b1.pack()
		self.b2.pack()
		self.b3.pack()
		self.frame = Frame(self.master)
		self.frame.config(width=300, height=100)
		self.frame.pack()

	def EnviarComunicación(self):
		self.master.withdraw()
		self.master.title("Nuevo Registro")
		self.agregarAlumnoApoderado = Toplevel(self.master)
		self.agregarAlumnoApoderado.config(width=700, height=600)
		self.comboCargo = Combobox(self, master, state='readonly', values=["Director/a","Inspecto General","Jefe/a UTP"])
		self.comboCargo.print(dict(comboCargo))
		self.comboCargo.grid(column=1, row=1)
		self.comboCargo.current(0)
		self.textoComunicacion = Text(self, width=50, height=20)
		self.textoComunicacion.grid(row=4, column=2, padx=10, pady=10)

	def NuevoRegistro(self):
		self.master.withdraw()
		self.master.title("Nuevo Registro")
		self.agregarAlumnoApoderado = Toplevel(self.master)
		self.agregarAlumnoApoderado.config(width=700, height=600)
		self.master.textoPrueba = Label(self.master, text="Hola")
		self.master.textoPrueba.pack(anchor=CENTER)
		self.titulo3 = Label(self.master, text = "Texto prueba", padx=14, pady=14)
		self.titulo3.pack()



	def elimAlumno(self):
		self.master.withdraw()
		self.master.title("Eliminar Registro de Alumno")
		self.eliminarAlumno = Toplevel(self.master)
		self.eliminarAlumno.config(width=400, height=300)



if __name__ == '__main__':
	fcwp = Tk()
	b = ButtonsMenuInterfaz(master=fcwp)
	fcwp.mainloop()