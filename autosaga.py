import datos
import contratos
import funciones
import manodeobrabonificada
import tkinter as tk
from datetime import datetime
from tkinter import ttk
import json
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoSAGA 2.0")
        self.root.geometry("250x440")
        # self.time_label = tk.Label(root, text="Tiempo restante: ")
        # self.target_date = datetime(2023, 10, 15, 23, 59, 59)  # Target date and time (adjust as needed)
        
        self.panel = ttk.Notebook(self.root)
        self.panel.pack(fill="both", expand="yes")
        self.tab1 = ttk.Frame(self.panel)
        self.panel.add(self.tab1, text="Carga unitaria")
        self.tab2 = ttk.Frame(self.panel)
        self.panel.add(self.tab2, text="Carga multiple")
        
        
        self.ordenlabel = tk.Label(self.tab1, text='Orden')
        self.ordenlabel.pack()
        self.ordentexto = tk.Entry(self.tab1, justify = 'center')
        self.ordentexto.pack()

        self.chasislabel = tk.Label(self.tab1, text='Chasis')
        self.chasislabel.pack()
        self.chasistexto = tk.Entry(self.tab1, justify = 'center')
        self.chasistexto.pack()

        self.recepcionlabel = tk.Label(self.tab1, text='Fecha recepción')
        self.recepcionlabel.pack()
        self.recepciontexto = tk.Entry(self.tab1, justify = 'center')
        self.recepciontexto.pack()

        self.kilometrajelabel = tk.Label(self.tab1, text='Kilometraje')
        self.kilometrajelabel.pack()
        self.kilometrajetexto = tk.Entry(self.tab1, justify = 'center')
        self.kilometrajetexto.pack()

        self.reparacionlabel = tk.Label(self.tab1, text='Fecha reparación')
        self.reparacionlabel.pack()
        self.reparaciontexto = tk.Entry(self.tab1, justify = 'center')
        self.reparaciontexto.pack()

        self.codigolabel = tk.Label(self.tab1, text='Código')
        self.codigolabel.pack()
        self.codigotexto = tk.Entry(self.tab1, justify = 'center')
        self.codigotexto.pack()
        self.errorlabel = tk.Label(self.tab1)
        self.errorlabel.pack()

        self.botonreclamar = tk.Button(self.tab1, text='Reclamar', command= self.reclamar)
        self.botonreclamar.pack(pady=5)
        self.botonborrar = tk.Button(self.tab1, text='Borrar', command= self.borrar)
        self.botonborrar.pack(pady=5)

        # self.time_label.pack(pady=10)#linea agregada
        

        copyright = u"\u00A9"
        self.copyrightlabel = tk.Label(self.tab1, text=copyright + " JPsoft")
        self.copyrightlabel.pack(pady=10)

        self.tab2label = tk.Label(self.tab2, text='Atención!\n Carga múltiple desde el archivo data.json')
        self.tab2label.pack()
        
        self.botonreclamarvarios = tk.Button(self.tab2, text='Reclamar', command= self.reclamar)
        self.botonreclamarvarios.pack(pady=5)
        # self.update_timer() 

        # Traer templates desde mongo
        uri = "mongodb+srv://pablomar04:auster1900@cluster0.g0ktnap.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        # Obtener json
        db = client['work']
        self.coleccion = db.get_collection('templates')
        #self.templates = coleccion.find({})
        #client.close()

        
    """"
    def update_timer(self):
        current_date = datetime.now()
        remaining_time = self.target_date - current_date

        if remaining_time.total_seconds() <= 0:
            self.show_expired_message()
        else:
            days, seconds = remaining_time.days, remaining_time.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            time_string = "{:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds)
            self.time_label.config(text="Tiempo restante: {}".format(time_string))
            self.root.after(1000, self.update_timer)
j
    def show_expired_message(self):
        self.time_label.config(text="Tiempo expirado! Cerrando la app...")
        self.root.after(2000, self.root.destroy)  # Close the app after 2 seconds """

    def borrar (self):   
        self.ordentexto.delete(0,'end')
        self.chasistexto.delete(0,'end')
        self.recepciontexto.delete(0,'end')
        self.kilometrajetexto.delete(0,'end')
        self.reparaciontexto.delete(0,'end')
        self.codigotexto.delete(0,'end')
        self.errorlabel.config(text = "")

    def error(self):
        self.errorlabel.config(text = "No existe código")
    
    def armarJson(self):        
        f = open('template.json')
        datos = json.load(f)
        for i in datos['data']:
            print(i)
        f.close

    def reclamar(self):
        #self.errorlabel.config(text="Se hizo clic en Reclamar")
        #controlar que ninguno es vacio
        
        orden_texto = self.ordentexto.get()
        chasis_texto = self.chasistexto.get()
        recepcion_texto = self.recepciontexto.get()
        kilometraje_texto = self.kilometrajetexto.get()
        reparacion_texto = self.reparaciontexto.get()
        codigo_texto = self.codigotexto.get()

        if(funciones.existeCodigo(codigo_texto,self.coleccion)):
            funciones.cargarCabecera(orden_texto, chasis_texto, recepcion_texto, kilometraje_texto, reparacion_texto, codigo_texto, self.coleccion)
        

 

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    #app.time_label = tk.Label(root, text="Time remaining: --")
    #app.time_label.pack(pady=10)
    root.mainloop()

