from tkinter import *
from tkinter import messagebox

def insertar():
    nombre = txt_nombre.get()
    print(f'Hola {nombre}')
    messagebox.showinfo("Saludo",f"Hola {nombre}")

#crear un objeto de clase Tk
app = Tk()
app.title("Gestión de alumnos")
app.geometry("300x150")

#agregar un objeto frame
frame = Frame(app)
frame.grid(row=8,column=3,columnspan=3,pady=20,padx=20)

#agregar un objeto label
lb_nombre = Label(frame,text='DNI: ')
lb_nombre.grid(row=1,column=0)
#agregar un objeto Entry
txt_nombre = Entry(frame)
txt_nombre.grid(row=1,column=1)
#agregar un objeto label
lb_nombre = Label(frame,text='NOMBRE: ')
lb_nombre.grid(row=2,column=0)
#agregar un objeto Entry
txt_nombre = Entry(frame)
txt_nombre.grid(row=2,column=1)
#agregar un objeto label
lb_nombre = Label(frame,text='EMAIL: ')
lb_nombre.grid(row=3,column=0)
#agregar un objeto Entry
txt_nombre = Entry(frame)
txt_nombre.grid(row=3,column=1)
#agregar un objeto Button
btn_saludar = Button(frame,text='Insertar Nuevo Alumno',command=insertar)
btn_saludar.grid(row=4,column=1,padx=10)
btn_saludar = Button(frame,text='Eliminar Alumno',command=insertar)
btn_saludar.grid(row=5,column=1,padx=10)
app.mainloop()