# Modulos de Qt e importados

from PySide6.QtWidgets import *
from PySide6.QtCore    import *
from PySide6.QtGui     import *
from modulo            import *
from time              import sleep
import sys
import os


diccionario_agregar_cliente = {
    "Cliente":   "",
    "Teléfono":  "",
    "Dirección": "",
    "Email":     "",
}


diccionario_agregar_trabajo = {
    "Trabajo":      "",
    "Descripción":  "",
    "D. Vehículo":  "",
    "Precio":       "",
    "Fecha Inicio": "",
    "Fecha Final":  "",
    "Estatus":      "",
    "Prioridad":    "",
}


diccionario_agregar_producto = {
    "Nombre":      "",
    "Descripción": "",
    "Unidades":    "",
    "Estado":      "",
}


class CajaPrueba(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet("background-color: {}".format(color))


class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class Cliente:
    def __init__(self):
        self.nombre    = ""
        self.telefono  = ""
        self.email     = ""
        self.direccion = ""
        self.trabajos  = {}
        self.indicadorIngresar   = False
        self.indicadorTerminar   = False
        self.indicadorAgendar    = False        
        self.diccionarioIngresar = {
            "cliente":     "",
            "fecha":       "",
            "trabajo":     "",
            "descripcion": "",
        }
        self.diccionarioTerminar = {
            "clave":  "",
            "fecha":  "",
            "precio": "",
        }
        self.diccionarioAgendar  = {
            "clave":   "",
            "cliente": "",
            "fecha":   "",
            "trabajo": "",
        }
    
    def reiniciarClienteMetodo(self):
        self.nombre    = ""
        self.telefono  = ""
        self.email     = ""
        self.direccion = ""
        self.trabajos  = {}
        self.indicadorIngresar   = False
        self.indicadorTerminar   = False
        self.indicadorAgendar    = False
        self.diccionarioIngresar = {
            "cliente":     "",
            "fecha":       "",
            "trabajo":     "",
            "descripcion": "",
        }
        self.diccionarioTerminar = {
            "clave":  "",
            "fecha":  "",
            "precio": "",
        }
        self.diccionarioAgendar  = {
            "clave":   "",
            "cliente": "",
            "fecha":   "",
            "trabajo": "",
        }

    def cambiarIndicadorIngresarMetodo(self, valor):
        self.indicadorIngresar = valor

    def cambiarIndicadorTerminarMetodo(self, valor):
        self.indicadorTerminar = valor

    def cambiarIndicadorAgendarMetodo(self, valor):
        self.indicadorAgendar = valor
    
    def actualizarNombreMetodo(self, nombre):
        self.nombre = nombre

    def actualizarTelefonoMetodo(self, telefono):
        self.telefono = telefono

    def actualizarEmailMetodo(self, email):
        self.email = email

    def actualizarDireccionMetodo(self, direccion):
        self.direccion = direccion

    def actualizarTrabajoMetodo(self, trabajo):
        pass

    def actualizarDiccionarioIngresarMetodo(self, datos):
        for elemento in datos:
            self.diccionarioIngresar[elemento] = elemento

    def actualizarDiccionarioTerminarMetodo(self, datos):
        for elemento in datos:
            self.diccionarioTerminar[elemento] = elemento

    def actualizarDiccionarioAgendarMetodo(self, datos):
        for elemento in datos:  
            self.diccionarioAgendar[elemento] = elemento


# ********************    Cuadros de Dialogos    ********************

class CuadroMostrarTexto(QDialog):
    def __init__(self, mensaje, titulo, ancho, alto):
        super().__init__()
        self.resize(ancho, alto)
        self.setWindowTitle(titulo)
        contenedor = QVBoxLayout()
        cuadro     = QPlainTextEdit()
        contenedor.addWidget(cuadro)
        self.setLayout(contenedor)
        cuadro.setReadOnly(True)
        cuadro.setPlainText(mensaje)
        botones = QDialogButtonBox(QDialogButtonBox.Ok)
        botones.accepted.connect(self.accept)
        contenedor.addWidget(botones)


class CuadroAceptar(QDialog):
    def __init__(self, mensaje):
        super().__init__()
        self.resize(240, 120)
        self.setWindowTitle("Notificación")
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)
        contenedor.addWidget(QLabel(mensaje))
        botones = QDialogButtonBox(QDialogButtonBox.Ok)
        botones.accepted.connect(self.accept)
        contenedor.addWidget(botones)


class CuadroComprobar(QDialog):
    def __init__(self, mensaje):
        super().__init__()
        self.resize(300, 120)
        self.setWindowTitle("Notificación")
        contenedor = QVBoxLayout()
        self.setLayout(contenedor)
        contenedor.addWidget(QLabel(mensaje))
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        contenedor.addWidget(botones)


class CuadroAgregarCliente(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(500, 200)
        self.setWindowTitle("Agregar Cliente")
        self.contenedor = QVBoxLayout()
        self.formulario = QFormLayout()
        self.etiquetaTitulo           = QLabel("Ingresar Cliente")
        self.etiquetaAgregarCliente   = QLabel("Cliente: ")
        self.etiquetaAgregarTelefono  = QLabel("Teléfono: ")
        self.etiquetaAgregarDireccion = QLabel("Dirección: ")
        self.etiquetaAgregarEmail     = QLabel("Email: ")
        self.entradaAgregarCliente    = QLineEdit()
        self.entradaAgregarTelefono   = QLineEdit()
        self.entradaAgregarDireccion  = QLineEdit()
        self.entradaAgregarEmail      = QLineEdit()
        self.entradaAgregarCliente.textChanged.connect(lambda: self.cambiarCliente(self.entradaAgregarCliente.text()))  
        self.entradaAgregarTelefono.textChanged.connect(lambda: self.cambiarTelefono(self.entradaAgregarTelefono.text())) 
        self.entradaAgregarDireccion.textChanged.connect(lambda: self.cambiarDireccion(self.entradaAgregarDireccion.text()))
        self.entradaAgregarEmail.textChanged.connect(lambda: self.cambiarEmail(self.entradaAgregarEmail.text()))    
        self.formulario.addRow(self.etiquetaTitulo)
        self.formulario.addRow(QHLine())
        self.formulario.addRow(self.etiquetaAgregarCliente, self.entradaAgregarCliente)
        self.formulario.addRow(self.etiquetaAgregarTelefono, self.entradaAgregarTelefono)
        self.formulario.addRow(self.etiquetaAgregarDireccion, self.entradaAgregarDireccion)
        self.formulario.addRow(self.etiquetaAgregarEmail, self.entradaAgregarEmail)
        self.contenedor.addLayout(self.formulario)
        self.setLayout(self.contenedor)
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        self.contenedor.addWidget(botones)       
    
    def cambiarCliente(self, dato):
        diccionario_agregar_cliente["Cliente"] = dato

    def cambiarTelefono(self, dato):
        diccionario_agregar_cliente["Teléfono"] = dato

    def cambiarDireccion(self, dato):
        diccionario_agregar_cliente["Dirección"] = dato

    def cambiarEmail(self, dato):
        diccionario_agregar_cliente["Email"] = dato


class CuadroEditarCliente(QDialog):
    def __init__(self, datos):
        super().__init__()
        self.resize(500, 200)
        self.setWindowTitle("Editar Cliente")
        self.contenedor = QVBoxLayout()
        self.formulario = QFormLayout()
        self.etiquetaTitulo           = QLabel("Ingresar Cliente")
        self.etiquetaAgregarCliente   = QLabel("Cliente: ")
        self.etiquetaAgregarTelefono  = QLabel("Teléfono: ")
        self.etiquetaAgregarDireccion = QLabel("Dirección: ")
        self.etiquetaAgregarEmail     = QLabel("Email: ")
        self.entradaAgregarCliente    = QLineEdit()
        self.entradaAgregarTelefono   = QLineEdit()
        self.entradaAgregarDireccion  = QLineEdit()
        self.entradaAgregarEmail      = QLineEdit()
        diccionario_agregar_cliente["Cliente"]   = str(datos[0])
        diccionario_agregar_cliente["Teléfono"]  = str(datos[1])
        diccionario_agregar_cliente["Dirección"] = str(datos[2])
        diccionario_agregar_cliente["Email"]     = str(datos[3])
        self.entradaAgregarCliente.setText(datos[0])  
        self.entradaAgregarTelefono.setText(datos[1]) 
        self.entradaAgregarDireccion.setText(datos[2])
        self.entradaAgregarEmail.setText(datos[3])    
        self.entradaAgregarCliente.textChanged.connect(lambda: self.cambiarCliente(self.entradaAgregarCliente.text()))  
        self.entradaAgregarTelefono.textChanged.connect(lambda: self.cambiarTelefono(self.entradaAgregarTelefono.text())) 
        self.entradaAgregarDireccion.textChanged.connect(lambda: self.cambiarDireccion(self.entradaAgregarDireccion.text()))
        self.entradaAgregarEmail.textChanged.connect(lambda: self.cambiarEmail(self.entradaAgregarEmail.text()))    
        self.formulario.addRow(self.etiquetaTitulo)
        self.formulario.addRow(QHLine())
        self.formulario.addRow(self.etiquetaAgregarCliente, self.entradaAgregarCliente)
        self.formulario.addRow(self.etiquetaAgregarTelefono, self.entradaAgregarTelefono)
        self.formulario.addRow(self.etiquetaAgregarDireccion, self.entradaAgregarDireccion)
        self.formulario.addRow(self.etiquetaAgregarEmail, self.entradaAgregarEmail)
        self.contenedor.addLayout(self.formulario)
        self.setLayout(self.contenedor)
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        self.contenedor.addWidget(botones)       

    def cambiarCliente(self, dato):
        if str(dato) != "":
            diccionario_agregar_cliente["Cliente"] = str(dato)
        else:
            diccionario_agregar_cliente["Cliente"] = str(datos[0])

    def cambiarTelefono(self, dato):
        if str(dato) != "":
            diccionario_agregar_cliente["Teléfono"] = dato
        else:
            diccionario_agregar_cliente["Teléfono"] = str(datos[1])
        
    def cambiarDireccion(self, dato):
        if str(dato) != "":
            diccionario_agregar_cliente["Dirección"] = dato
        else:
            diccionario_agregar_cliente["Dirección"] = str(datos[2])

    def cambiarEmail(self, dato):
        if str(dato) != "":
            diccionario_agregar_cliente["Email"] = dato
        else:
            diccionario_agregar_cliente["Email"] = str(datos[3])


class CuadroEditarTrabajo(QDialog):
    def __init__(self, datos):
        super().__init__()
        self.resize(500, 350)
        self.setWindowTitle("Editar Trabajo")
        self.contenedor = QVBoxLayout()
        self.formulario = QFormLayout()
        self.etiquetaTitulo             = QLabel("Editar Trabajo")
        self.etiquetaAgregarTrabajo     = QLabel("Trabajo: ")
        self.etiquetaAgregarDescripcion = QLabel("Descripción: ")
        self.etiquetaAgregarDVehiculo   = QLabel("D. Vehículo: ")
        self.etiquetaAgregarPrecio      = QLabel("Precio: ")
        self.etiquetaAgregarFechaInicio = QLabel("Fecha Inicio: ")
        self.etiquetaAgregarFechaFinal  = QLabel("Fecha Final: ")
        self.etiquetaAgregarEstatus     = QLabel("Estatus")         
        self.etiquetaAgregarPrioridad   = QLabel("Prioridad")         
        self.entradaAgregarTrabajo      = QLineEdit()
        self.entradaAgregarDescripcion  = QPlainTextEdit()
        self.entradaAgregarDVehiculo    = QPlainTextEdit()
        self.entradaAgregarPrecio       = QLineEdit()
        self.entradaAgregarFechaInicio  = QDateEdit()
        self.entradaAgregarFechaFinal   = QDateEdit()
        self.entradaAgregarEstatus      = QComboBox()
        self.entradaAgregarPrioridad    = QComboBox()
        self.entradaAgregarEstatus.addItems(["Agendado", "En Proceso", "Terminado"])
        self.entradaAgregarPrioridad.addItems(["Sin Prisa", "Urgente"])
        diccionario_agregar_trabajo["Trabajo"]      = str(datos[0])
        diccionario_agregar_trabajo["Descripción"]  = str(datos[1])
        diccionario_agregar_trabajo["D. Vehículo"]  = str(datos[2])
        diccionario_agregar_trabajo["Precio"]       = str(datos[3])
        diccionario_agregar_trabajo["Fecha Inicio"] = str(datos[4])
        diccionario_agregar_trabajo["Fecha Final"]  = str(datos[5])
        diccionario_agregar_trabajo["Estatus"]      = str(datos[6])
        diccionario_agregar_trabajo["Prioridad"]    = str(datos[7])
        self.entradaAgregarTrabajo.setText(datos[0])
        self.entradaAgregarDescripcion.setPlainText(datos[1])
        self.entradaAgregarDVehiculo.setPlainText(datos[2])
        self.entradaAgregarPrecio.setText(datos[3])
        if datos[4] != "":
            fecha_inicio = QDate.fromString(recuperar_fecha(datos[4],"/"), "dd-MM-yyyy")
        else: 
            fecha_inicio = QDate.fromString(recuperar_fecha("01/01/2000","/"), "dd-MM-yyyy")
        self.entradaAgregarFechaInicio.setDate(fecha_inicio)
        if datos[5] != "":
            fecha_final = QDate.fromString(recuperar_fecha(datos[5],"/"), "dd-MM-yyyy")
        else:
            fecha_final = QDate.fromString(recuperar_fecha("01/01/2000","/"), "dd-MM-yyyy")        
        self.entradaAgregarFechaFinal.setDate(fecha_final)
        if datos[6] == "Agendado":
            self.entradaAgregarEstatus.setCurrentIndex(0)
        elif datos[6] == "En Proceso":
            self.entradaAgregarEstatus.setCurrentIndex(1)
        elif datos[6] == "Terminado":
            self.entradaAgregarEstatus.setCurrentIndex(2)
        if datos[7] == "Urgente":
            self.entradaAgregarPrioridad.setCurrentIndex(1)
        self.entradaAgregarTrabajo.textChanged.connect(lambda: self.cambiarTrabajo(self.entradaAgregarTrabajo.text()))
        self.entradaAgregarDescripcion.textChanged.connect(lambda: self.cambiarDescripcion(self.entradaAgregarDescripcion.toPlainText()))
        self.entradaAgregarDVehiculo.textChanged.connect(lambda: self.cambiarDVehiculo(self.entradaAgregarDVehiculo.toPlainText()))
        self.entradaAgregarPrecio.textChanged.connect(lambda: self.cambiarPrecio(self.entradaAgregarPrecio.text()))
        self.entradaAgregarFechaInicio.dateChanged.connect(lambda: self.cambiarFechaInicio(self.entradaAgregarFechaInicio.date()))
        self.entradaAgregarFechaFinal.dateChanged.connect(lambda: self.cambiarFechaFinal(self.entradaAgregarFechaFinal.date()))
        self.entradaAgregarEstatus.currentIndexChanged.connect(lambda: self.cambiarEstatus(self.entradaAgregarEstatus.currentText()))
        self.entradaAgregarPrioridad.currentIndexChanged.connect(lambda: self.cambiarPrioridad(self.entradaAgregarPrioridad.currentText()))
        self.formulario.addRow(self.etiquetaTitulo)
        self.formulario.addRow(QHLine())
        self.formulario.addRow(self.etiquetaAgregarTrabajo, self.entradaAgregarTrabajo)
        self.formulario.addRow(self.etiquetaAgregarDescripcion, self.entradaAgregarDescripcion)
        self.formulario.addRow(self.etiquetaAgregarDVehiculo, self.entradaAgregarDVehiculo)        
        self.formulario.addRow(self.etiquetaAgregarPrecio, self.entradaAgregarPrecio)
        if datos[3] != "":
            self.formulario.addRow(self.etiquetaAgregarFechaInicio, self.entradaAgregarFechaInicio)
        if datos[4] != "":
            self.formulario.addRow(self.etiquetaAgregarFechaFinal, self.entradaAgregarFechaFinal)        
        self.formulario.addRow(self.etiquetaAgregarPrioridad, self.entradaAgregarPrioridad)
        self.formulario.addRow(self.etiquetaAgregarEstatus, self.entradaAgregarEstatus)        
        self.contenedor.addLayout(self.formulario)
        self.setLayout(self.contenedor)
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        self.contenedor.addWidget(botones)       

    def cambiarTrabajo(self, dato):
        if str(dato) != "":
            diccionario_agregar_trabajo["Trabajo"] = str(dato)
        else:
            diccionario_agregar_trabajo["Trabajo"] = str(datos[0])

    def cambiarDescripcion(self, dato):
        if str(dato) != "":
            diccionario_agregar_trabajo["Descripción"] = str(dato)
        else:
            diccionario_agregar_trabajo["Descripción"] = str(datos[1])

    def cambiarDVehiculo(self, dato):
        if str(dato) != "":
            diccionario_agregar_trabajo["D. Vehículo"] = str(dato)
        else:
            diccionario_agregar_trabajo["D. Vehículo"] = str(datos[2])

    def cambiarPrecio(self, dato):
        if str(dato) != "":
            diccionario_agregar_trabajo["Precio"] = str(dato)
        else:
            diccionario_agregar_trabajo["Precio"] = str(datos[3])

    def cambiarFechaInicio(self, dato):
        fecha_objeto = dato
        fecha        = procesar_fecha(str(fecha_objeto.toPython()), "-")     
        diccionario_agregar_trabajo["Fecha Inicio"] = fecha
    
    def cambiarFechaFinal(self, dato):
        fecha_objeto = dato
        fecha        = procesar_fecha(str(fecha_objeto.toPython()), "-")     
        diccionario_agregar_trabajo["Fecha Final"] = fecha

    def cambiarEstatus(self, dato):
        if str(dato) != "":
            diccionario_agregar_trabajo["Estatus"] = str(dato)
        else:
            diccionario_agregar_trabajo["Estatus"] = str(datos[6])

    def cambiarPrioridad(self, dato):
        if str(dato) != "":
            diccionario_agregar_trabajo["Prioridad"] = str(dato)
        else:
            diccionario_agregar_trabajo["Prioridad"] = str(datos[7])


class CuadroMostrarClientes(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(380, 600)
        self.setWindowTitle("Clientes")
        contenedor     = QVBoxLayout()
        contenedor.addWidget(QLabel("Clave\t\tCliente"))
        contenedor.addWidget(QHLine())
        clientes_lista = consultar_clientes()
        mensaje        = ""
        for elemento in clientes_lista:
            mensaje_linea = "\n\n  {}\t{}".format(elemento[0], elemento[1])
            mensaje       = mensaje + mensaje_linea
        self.visor = QPlainTextEdit()
        self.visor.insertPlainText(mensaje)
        self.visor.setReadOnly(True)
        contenedor.addWidget(self.visor)
        self.setLayout(contenedor)
        botones = QDialogButtonBox(QDialogButtonBox.Ok)
        botones.accepted.connect(self.accept)
        contenedor.addWidget(botones)


class CuadroMostrarArticulosLista(QDialog):
    def __init__(self, indicador):
        super().__init__()
        self.resize(380, 600)
        self.indicador = indicador
        lista   = []
        mensaje = ""        
        if self.indicador == "Herramientas":
            lista = consultar_herramientas()
            titulo = self.indicador
            for elemento in lista:
                mensaje_linea = "\n\n  {}\t{}".format(elemento[0], elemento[1])
                mensaje       = mensaje + mensaje_linea
        elif self.indicador == "Refacciones":
            lista = consultar_inventarios()
            titulo = self.indicador
            for elemento in lista:
                mensaje_linea = "\n\n  {}\t{}".format(elemento[0], elemento[1])
                mensaje       = mensaje + mensaje_linea
        self.setWindowTitle(titulo)
        contenedor = QVBoxLayout()
        if self.indicador == "Herramientas":
            contenedor.addWidget(QLabel("Clave\t\tHerramientas"))
        elif self.indicador == "Refacciones":
            contenedor.addWidget(QLabel("Clave\t\tRefacciones"))
        contenedor.addWidget(QHLine())
        self.visor = QPlainTextEdit()
        self.visor.insertPlainText(mensaje)
        self.visor.setReadOnly(True)
        contenedor.addWidget(self.visor)
        self.setLayout(contenedor)
        botones = QDialogButtonBox(QDialogButtonBox.Ok)
        botones.accepted.connect(self.accept)
        contenedor.addWidget(botones)


class CuadroAnadirArticulos(QDialog):
    def __init__(self, indicador):
        super().__init__()
        self.resize(500, 200)
        if indicador == "Herramientas":
            self.setWindowTitle("Agregar Herramienta")
        elif indicador == "Refacciones":
            self.setWindowTitle("Agregar Refacción")        
        self.contenedor = QVBoxLayout()
        self.formulario = QFormLayout()
        if indicador == "Herramientas":
            self.etiquetaTitulo        = QLabel("Ingresar Herramienta")
            self.etiquetaAgregarNombre = QLabel("Herramienta: ")
        elif indicador == "Refacciones":
            self.etiquetaTitulo        = QLabel("Ingresar Refacción")
            self.etiquetaAgregarNombre = QLabel("Refacción: ")
        self.etiquetaAgregarDetalle  = QLabel("Descripción: ")
        self.etiquetaAgregarUnidades = QLabel("Unidades: ")
        self.etiquetaAgregarEstado   = QLabel("Estado: ")
        self.entradaTitulo           = QLineEdit()
        self.entradaAgregarNombre    = QLineEdit()
        self.entradaAgregarDetalle   = QPlainTextEdit()
        self.entradaAgregarUnidades  = QSpinBox()
        self.entradaAgregarEstado    = QComboBox()
        self.entradaAgregarUnidades.setMinimum(1)
        self.entradaAgregarEstado.addItems(["Bueno", "Regular", "Malo"])
        self.entradaAgregarEstado.setCurrentIndex(0)
        self.formulario.addRow(self.etiquetaTitulo)
        self.formulario.addRow(QHLine())
        self.formulario.addRow(self.etiquetaAgregarNombre, self.entradaAgregarNombre)
        self.formulario.addRow(self.etiquetaAgregarDetalle, self.entradaAgregarDetalle)
        self.formulario.addRow(self.etiquetaAgregarUnidades, self.entradaAgregarUnidades)
        self.formulario.addRow(self.etiquetaAgregarEstado, self.entradaAgregarEstado)
        self.contenedor.addLayout(self.formulario)
        self.setLayout(self.contenedor)
        self.entradaAgregarNombre.textChanged.connect(lambda: self.cambiarNombre(self.entradaAgregarNombre.text()))  
        self.entradaAgregarDetalle.textChanged.connect(lambda: self.cambiarDetalle(self.entradaAgregarDetalle.toPlainText())) 
        self.entradaAgregarUnidades.valueChanged.connect(lambda: self.cambiarUnidades(str(self.entradaAgregarUnidades.value())))
        self.entradaAgregarEstado.currentIndexChanged.connect(lambda: self.cambiarEstado(self.entradaAgregarEstado.currentText()))    
        diccionario_agregar_producto["Estado"]   = "Bueno"
        diccionario_agregar_producto["Unidades"] = "1"
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        self.contenedor.addWidget(botones)       
    
    def cambiarNombre(self, dato):
        diccionario_agregar_producto["Nombre"] = dato

    def cambiarDetalle(self, dato):
        diccionario_agregar_producto["Descripción"] = dato

    def cambiarUnidades(self, dato):
        diccionario_agregar_producto["Unidades"] = dato

    def cambiarEstado(self, dato):
        diccionario_agregar_producto["Estado"] = dato


class CuadroEditarArticulos(QDialog):
    def __init__(self, indicador, datos):
        super().__init__()
        self.resize(500, 200)
        if indicador == "Herramientas":
            self.setWindowTitle("Editar Herramienta")
        elif indicador == "Refacciones":
            self.setWindowTitle("Editar Refacción")        
        self.contenedor = QVBoxLayout()
        self.formulario = QFormLayout()
        if indicador == "Herramientas":
            self.etiquetaTitulo        = QLabel("Ingresar Herramienta")
            self.etiquetaAgregarNombre = QLabel("Herramienta: ")
        elif indicador == "Refacciones":
            self.etiquetaTitulo        = QLabel("Ingresar Refacción")
            self.etiquetaAgregarNombre = QLabel("Refacción: ")
        self.etiquetaAgregarDetalle  = QLabel("Descripción: ")
        self.etiquetaAgregarUnidades = QLabel("Unidades: ")
        self.etiquetaAgregarEstado   = QLabel("Estado: ")
        self.entradaTitulo           = QLineEdit()
        self.entradaAgregarNombre    = QLineEdit()
        self.entradaAgregarDetalle   = QPlainTextEdit()
        self.entradaAgregarUnidades  = QSpinBox()
        self.entradaAgregarEstado    = QComboBox()
        self.entradaAgregarEstado.addItems(["Bueno", "Regular", "Malo"])
        diccionario_agregar_producto["Nombre"]      = datos[0]
        diccionario_agregar_producto["Descripción"] = datos[1]
        diccionario_agregar_producto["Unidades"]    = datos[2]
        diccionario_agregar_producto["Estado"]      = datos[3]
        self.entradaAgregarNombre.setText(diccionario_agregar_producto["Nombre"])
        self.entradaAgregarDetalle.setPlainText(diccionario_agregar_producto["Descripción"])
        self.entradaAgregarUnidades.setValue(int(diccionario_agregar_producto["Unidades"]))
        if datos[3] == "Bueno":
            self.entradaAgregarEstado.setCurrentIndex(0)
        elif datos[3] == "Regular":
            self.entradaAgregarEstado.setCurrentIndex(1)
        elif datos[3] == "Malo":
            self.entradaAgregarEstado.setCurrentIndex(2)
        self.formulario.addRow(self.etiquetaTitulo)
        self.formulario.addRow(QHLine())
        self.formulario.addRow(self.etiquetaAgregarNombre, self.entradaAgregarNombre)
        self.formulario.addRow(self.etiquetaAgregarDetalle, self.entradaAgregarDetalle)
        self.formulario.addRow(self.etiquetaAgregarUnidades, self.entradaAgregarUnidades)
        self.formulario.addRow(self.etiquetaAgregarEstado, self.entradaAgregarEstado)
        self.contenedor.addLayout(self.formulario)
        self.setLayout(self.contenedor)
        self.entradaAgregarNombre.textChanged.connect(lambda: self.cambiarNombre(self.entradaAgregarNombre.text()))  
        self.entradaAgregarDetalle.textChanged.connect(lambda: self.cambiarDetalle(self.entradaAgregarDetalle.toPlainText())) 
        self.entradaAgregarUnidades.valueChanged.connect(lambda: self.cambiarUnidades(str(self.entradaAgregarUnidades.value())))
        self.entradaAgregarEstado.currentIndexChanged.connect(lambda: self.cambiarEstado(self.entradaAgregarEstado.currentText()))    
        diccionario_agregar_producto["Estado"]   = "Bueno"
        diccionario_agregar_producto["Unidades"] = "1"
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        self.contenedor.addWidget(botones)       
    
    def cambiarNombre(self, dato):
        diccionario_agregar_producto["Nombre"] = dato

    def cambiarDetalle(self, dato):
        diccionario_agregar_producto["Descripción"] = dato

    def cambiarUnidades(self, dato):
        diccionario_agregar_producto["Unidades"] = dato

    def cambiarEstado(self, dato):
        diccionario_agregar_producto["Estado"] = dato


class CuadroMostrarTrabajosLista(QDialog):
    def __init__(self, indicador):
        super().__init__()
        self.resize(400, 600)
        self.indicador = indicador
        trabajos_lista = consultar_trabajos()
        mensaje        = ""        
        if self.indicador == "En Proceso":
            mensaje_titulo = "Trabajos en Proceso"
            for elemento in trabajos_lista:
                if elemento[7] == "En Proceso":
                    mensaje_linea = "\n\n  {}\t{}\t{}".format(elemento[0], elemento[8], elemento[1])
                    mensaje       = mensaje + mensaje_linea
        elif self.indicador == "Agendado":
            mensaje_titulo = "Trabajos Agendados"
            for elemento in trabajos_lista:
                if elemento[7] == "Agendado":
                    mensaje_linea = "\n\n  {}\t{}\t{}".format(elemento[0], elemento[8], elemento[1])
                    mensaje       = mensaje + mensaje_linea
        elif self.indicador == "Terminado":
            mensaje_titulo = "Trabajos Terminados"
            for elemento in trabajos_lista:
                if elemento[7] == "Terminado":
                    mensaje_linea = "\n\n  {}\t{}".format(elemento[0], elemento[1])
                    mensaje       = mensaje + mensaje_linea
        self.setWindowTitle(mensaje_titulo)
        contenedor     = QVBoxLayout()
        if self.indicador == "Terminado":
            contenedor.addWidget(QLabel("Clave\t            Trabajo"))
        else:
            contenedor.addWidget(QLabel("Clave\t            Prioridad\t      Trabajo"))
        contenedor.addWidget(QHLine())
        self.visor = QPlainTextEdit()
        self.visor.insertPlainText(mensaje)
        self.visor.setReadOnly(True)
        contenedor.addWidget(self.visor)
        self.setLayout(contenedor)
        botones = QDialogButtonBox(QDialogButtonBox.Ok)
        botones.accepted.connect(self.accept)
        contenedor.addWidget(botones)


class CuadroMostrarTrabajo(QDialog):
    def __init__(self, mensaje):
        super().__init__()
        self.resize(400, 380)
        self.setWindowTitle("Trabajo")
        contenedor = QVBoxLayout()
        self.visor = QPlainTextEdit()
        self.visor.insertPlainText(mensaje)
        self.visor.setReadOnly(True)
        contenedor.addWidget(self.visor)
        self.setLayout(contenedor)
        botones = QDialogButtonBox(QDialogButtonBox.Ok)
        botones.accepted.connect(self.accept)
        contenedor.addWidget(botones)

# **********************************************************************************
# ******************************    Primer Pestaña    ******************************
# **********************************************************************************    

class WidgetNuevoTrabajo(QWidget):
    """ Este pestaña requiere la entrada de un objeto cliente """
    def __init__(self, cliente):
        super().__init__()
            # Layouts Contenedores
        self.contenedorVertical = QVBoxLayout()
        self.contenedorSuperior = QHBoxLayout()
        self.contenedorInferior = QVBoxLayout()
        # Formularios
        self.ingresarTrabajo = QFormLayout()
        self.terminarTrabajo = QFormLayout()
        self.agendarTrabajo  = QFormLayout()
        # Formulario Ingresar Trabajo
        self.lineaIngresarTrabajo    = QHLine()
        self.lineaBusquedaI          = QHLine()
        self.etiquetaIngresarTrabajo = QLabel("Ingresar Trabajo")
        self.etiquetaClienteI        = QLabel("Cliente")
        self.etiquetaFechaI          = QLabel("Fecha")
        self.etiquetaTrabajoI        = QLabel("Trabajo")
        self.etiquetaDescripcionI    = QLabel("Descripción")
        self.etiquetaDVehiculoI      = QLabel("D. Vehículo")
        self.etiquetaPrioridadI      = QLabel("Prioridad")
        self.etiquetaBusquedaI       = QLabel("Buscar por Clave")
        self.entradaClienteI         = QLineEdit()
        self.entradaTrabajoI         = QLineEdit()
        self.entradaClaveI           = QLineEdit()
        self.entradaFechaI           = QDateEdit()
        self.entradaDescripcionI     = QPlainTextEdit()        
        self.entradaDVehiculoI       = QPlainTextEdit()
        self.entradaPrioridadI       = QComboBox()
        self.entradaPrioridadI.addItems(["Sin Prisa", "Urgente"])
        self.entradaPrioridadI.setCurrentIndex(0)
        self.entradaDescripcionI.setObjectName("DescripcionIngresar")
        self.entradaDVehiculoI.setObjectName("DescripcionIngresar")
        self.ingresarTrabajo.addRow(self.etiquetaIngresarTrabajo)
        self.ingresarTrabajo.addRow(self.lineaIngresarTrabajo)
        self.ingresarTrabajo.addRow(self.etiquetaClienteI, self.entradaClienteI)
        self.ingresarTrabajo.addRow(self.etiquetaFechaI, self.entradaFechaI)
        self.ingresarTrabajo.addRow(self.etiquetaTrabajoI, self.entradaTrabajoI)
        self.ingresarTrabajo.addRow(self.etiquetaDescripcionI, self.entradaDescripcionI)
        self.ingresarTrabajo.addRow(self.etiquetaDVehiculoI, self.entradaDVehiculoI)
        self.ingresarTrabajo.addRow(self.etiquetaPrioridadI, self.entradaPrioridadI)
        self.ingresarTrabajo.addRow(self.lineaBusquedaI)
        self.ingresarTrabajo.addRow(self.etiquetaBusquedaI, self.entradaClaveI)
        # Formulario Terminar Trabajo
        self.lineaTerminarTrabajo    = QHLine()
        self.etiquetaTerminarTrabajo = QLabel("Terminar Trabajo")
        self.etiquetaClaveT          = QLabel("Clave")
        self.etiquetaClienteT        = QLabel("Cliente")
        self.etiquetaTrabajoT        = QLabel("Trabajo")
        self.etiquetaFechaT          = QLabel("Fecha")
        self.etiquetaPrecioT         = QLabel("Precio")
        self.entradaClaveT           = QLineEdit()
        self.entradaClienteT         = QLineEdit()
        self.entradaTrabajoT         = QLineEdit()
        self.entradaPrecioT          = QLineEdit()
        self.entradaFechaT           = QDateEdit()
        self.entradaClienteT.setReadOnly(True)
        self.entradaTrabajoT.setReadOnly(True)
        self.terminarTrabajo.addRow(self.etiquetaTerminarTrabajo)
        self.terminarTrabajo.addRow(self.lineaTerminarTrabajo)
        self.terminarTrabajo.addRow(self.etiquetaClaveT, self.entradaClaveT)
        self.terminarTrabajo.addRow(self.etiquetaClienteT, self.entradaClienteT)
        self.terminarTrabajo.addRow(self.etiquetaTrabajoT, self.entradaTrabajoT)
        self.terminarTrabajo.addRow(self.etiquetaFechaT, self.entradaFechaT)
        self.terminarTrabajo.addRow(self.etiquetaPrecioT, self.entradaPrecioT)
        # Formulario Agendar Trabajo
        self.lineaAgendarTrabajo    = QHLine()
        self.etiquetaAgendarTrabajo = QLabel("Agendar Trabajo")
        self.etiquetaClienteA       = QLabel("Cliente")
        self.etiquetaFechaA         = QLabel("Fecha")        
        self.etiquetaTrabajoA       = QLabel("Trabajo")        
        self.etiquetaPrioridadA     = QLabel("Prioridad")
        self.entradaClienteA        = QLineEdit()
        self.entradaTrabajoA        = QLineEdit()
        self.entradaFechaA          = QDateEdit()
        self.entradaPrioridadA      = QComboBox()
        self.entradaPrioridadA.addItems(["Sin Prisa", "Urgente"])
        self.entradaPrioridadA.setCurrentIndex(0)
        self.agendarTrabajo.addRow(self.etiquetaAgendarTrabajo)
        self.agendarTrabajo.addRow(self.lineaAgendarTrabajo)
        self.agendarTrabajo.addRow(self.etiquetaClienteA, self.entradaClienteA)
        self.agendarTrabajo.addRow(self.etiquetaFechaA, self.entradaFechaA)
        self.agendarTrabajo.addRow(self.etiquetaTrabajoA, self.entradaTrabajoA)
        self.agendarTrabajo.addRow(self.etiquetaPrioridadA, self.entradaPrioridadA)
        # Formulario Estatus Trabajo
        self.lineaEstatus        = QHLine()
        self.etiquetaEstatus     = QLabel("Controles y Mensajes")
        self.contenedorEstatus   = QHBoxLayout()
        self.contenedorBotones   = QFormLayout()
        self.botonAgregarCliente = QPushButton("+ Agregar Cliente")        
        self.botonIngresar       = QPushButton("Ingresar")
        self.botonTerminar       = QPushButton("Terminar")
        self.botonAgendar        = QPushButton("Agendar")
        self.visor               = QPlainTextEdit()   
        self.etiquetaEstatus.setObjectName("ControlesMensajes")
        self.visor.setObjectName("CuadroVisor")
        self.visor.setReadOnly(True)
        self.contenedorBotones.addRow(self.botonAgregarCliente)
        self.contenedorBotones.addRow(self.botonIngresar)        
        self.contenedorBotones.addRow(self.botonTerminar)
        self.contenedorBotones.addRow(self.botonAgendar)
        self.contenedorEstatus.addLayout(self.contenedorBotones)        
        self.contenedorEstatus.addWidget(self.visor)
        # Agregar widgets en los contenedores
        self.contenedorSuperior.addLayout(self.ingresarTrabajo)
        self.contenedorSuperior.addLayout(self.terminarTrabajo)
        self.contenedorSuperior.addLayout(self.agendarTrabajo)
        self.contenedorInferior.addLayout(self.contenedorEstatus)
        self.contenedorVertical.addLayout(self.contenedorSuperior)
        self.contenedorVertical.addWidget(self.etiquetaEstatus)
        self.contenedorVertical.addWidget(self.lineaEstatus)        
        self.contenedorVertical.addLayout(self.contenedorInferior)        
        self.espacio = QHBoxLayout()
        self.espacio.addWidget(QLabel(""))        
        self.contenedorVertical.addLayout(self.espacio)
        # Agregar el contenedor principal        
        self.setLayout(self.contenedorVertical)
        # Agregar Funciones
        self.botonAgregarCliente.clicked.connect(lambda: self.agregarClienteMetodo(cliente))
        self.botonIngresar.clicked.connect(lambda: self.ingresarTrabajoMetodo(cliente))
        self.botonTerminar.clicked.connect(lambda: self.terminarTrabajoMetodo(cliente))  
        self.botonAgendar.clicked.connect(lambda: self.agendarTrabajoMetodo(cliente))
        self.entradaClienteI.textChanged.connect(lambda: self.comprobarClienteMetodo(cliente))
        self.entradaClaveI.textChanged.connect(lambda: self.comprobarTrabajoMetodo(cliente, "En Proceso"))
        self.entradaClaveT.textChanged.connect(lambda: self.comprobarTrabajoMetodo(cliente, "Terminado"))
        self.entradaClienteA.textChanged.connect(lambda: self.comprobarClienteMetodo(cliente))
        
    def agregarClienteMetodo(self, cliente):
        ventana   = CuadroAgregarCliente()
        respuesta = ventana.exec_()
        if respuesta:
            mensaje_formato = """{}\n
                                 \tNombre:  \t{}
                                 \tTelefono:  \t{}
                                 \tDirección:  \t{}
                                 \tEmail:  \t\t{} \n"""            
            mensaje_confirmacion = mensaje_formato.format("Se introducirán los datos del siguiente cliente:",                                                          
                                                          diccionario_agregar_cliente["Cliente"], 
                                                          diccionario_agregar_cliente["Teléfono"], 
                                                          diccionario_agregar_cliente["Dirección"], 
                                                          diccionario_agregar_cliente["Email"])
            confirmacion           = CuadroComprobar(mensaje_confirmacion)
            respuesta_confirmacion = confirmacion.exec_()
            if respuesta_confirmacion:
                mensaje_formato = """{}\n
                                     \tClave: \t\t{}
                                     \tNombre:  \t{}
                                     \tTelefono:  \t{}
                                     \tDirección:  \t{}
                                     \tEmail:  \t\t{} \n"""
                resultado = ingresar_cliente(diccionario_agregar_cliente["Cliente"], 
                                             diccionario_agregar_cliente["Teléfono"], 
                                             diccionario_agregar_cliente["Dirección"], 
                                             diccionario_agregar_cliente["Email"])
                mensaje_cliente_nuevo = mensaje_formato.format("Se ha introducido en la base de datos al siguiente cliente:",
                                                               str(resultado[0]),
                                                               diccionario_agregar_cliente["Cliente"], 
                                                               diccionario_agregar_cliente["Teléfono"], 
                                                               diccionario_agregar_cliente["Dirección"], 
                                                               diccionario_agregar_cliente["Email"])
                self.escribirMensajeMetodo([mensaje_cliente_nuevo])

    def comprobarClienteMetodo(self, cliente):
        texto   = ""        
        modo    = ""
        mensaje = """\n\t\t\t\t\t*********************************
                     \n\t\t\t\t\t  CLIENTE NO ENCONTRADO
                     \n\t\t\t\t\t*********************************"""        
        if self.entradaClienteI.text() != "":
            texto = self.entradaClienteI.text()
            modo  = "En Proceso"
            self.entradaClienteA.setText("")
        elif self.entradaClienteA.text() != "":
            texto = self.entradaClienteA.text()
            modo  = "Agendado"
            self.entradaClienteI.setText("")
        lista = buscar_cliente(texto)        
        if ((len(lista) == 0) or (len(lista) > 1)):            
            self.escribirMensajeMetodo([mensaje])
            if modo == "En Proceso":
                cliente.cambiarIndicadorIngresarMetodo(False)
            elif modo == "Agendado":
                cliente.cambiarIndicadorAgendarMetodo(False)
            if len(texto) == 0:
                self.escribirMensajeMetodo([""])
        if len(lista) == 1:
            if modo == "En Proceso":
                cliente.cambiarIndicadorIngresarMetodo(True)
            elif modo == "Agendado":
                cliente.cambiarIndicadorAgendarMetodo(True)
            self.escribirMensajeMetodo([""])
                        
    def comprobarTrabajoMetodo(self, cliente, modo):        
        mensaje = """\n\t\t\t\t\t*********************************
                     \n\t\t\t\t\t  {}
                     \n\t\t\t\t\t*********************************"""            
        if modo == "En Proceso":
            filtro = self.entradaClaveI.text()
        elif modo == "Terminado":
            filtro = self.entradaClaveT.text()        
        if  filtro == "":
            self.escribirMensajeMetodo([""])
            if modo == "En Proceso":
                self.limpiarCamposMetodo(True, False, False)
            elif modo == "Terminado":
                self.limpiarCamposMetodo(False, True, False)
        else:
            if buscar_trabajo(filtro) == []:
                if self.entradaClaveI.text() != "":
                    self.entradaClienteI.setText("")
                    fecha = QDate.fromString("01-01-2000", "MM-dd-yyyy")
                    self.entradaFechaI.show()
                    self.entradaFechaI.setDate(fecha)
                    self.entradaTrabajoI.setText("")
                    self.entradaDescripcionI.clear()
                    self.entradaDVehiculoI.clear()            
                    self.entradaPrioridadI.setCurrentIndex(0)
                    mensaje_terminado = mensaje.format("TRABAJO NO ENCONTRADO")
                    self.escribirMensajeMetodo([mensaje_terminado])            
                if self.entradaClaveT.text() != "":
                    cliente.cambiarIndicadorTerminarMetodo(False)
                    self.entradaClienteT.setText("")
                    self.entradaTrabajoT.setText("")
                    fecha = QDate.fromString("01-01-2000", "MM-dd-yyyy")
                    self.entradaFechaT.setDate(fecha)
                    self.entradaFechaT.show()
                    mensaje_terminado = mensaje.format("TRABAJO NO ENCONTRADO")
                    self.escribirMensajeMetodo([mensaje_terminado])     
            else:
                if modo ==  "En Proceso":            
                    consulta = consultar_trabajo(filtro)                
                    estatus  = consulta[7]
                    if estatus == "Terminado":
                        self.entradaClienteI.setText("")
                        fecha = QDate.fromString("01-01-2000", "MM-dd-yyyy")
                        self.entradaFechaI.show()
                        self.entradaFechaI.setDate(fecha)
                        self.entradaTrabajoI.setText("")
                        self.entradaDescripcionI.clear()
                        self.entradaDVehiculoI.clear()            
                        self.entradaPrioridadI.setCurrentIndex(0)
                        mensaje_agenda = """\n\t\t\t\t\t*************************************************
                                            \n\t\t\t\t\t  ESTE TRABAJO SE ENCUENTRA TERMINADO
                                            \n\t\t\t\t\t*************************************************"""
                        self.escribirMensajeMetodo([mensaje_agenda])
                    elif estatus == "En Proceso":
                        self.entradaClienteI.setText("")
                        fecha = QDate.fromString("01-01-2000", "MM-dd-yyyy")
                        self.entradaFechaI.show()
                        self.entradaFechaI.setDate(fecha)
                        self.entradaTrabajoI.setText("")
                        self.entradaDescripcionI.clear()
                        self.entradaDVehiculoI.clear()            
                        self.entradaPrioridadI.setCurrentIndex(0)                        
                        mensaje_agenda = """\n\t\t\t\t\t*************************************************
                                            \n\t\t\t\t\t  ESTE TRABAJO SE ENCUENTRA EN CURSO
                                            \n\t\t\t\t\t*************************************************"""
                        self.escribirMensajeMetodo([mensaje_agenda])
                    elif estatus == "Agendado":
                        self.entradaClienteI.setText(consultar_cliente(str(consulta[9]))[1])                    
                        fecha = QDate.fromString(recuperar_fecha(consulta[5],"/"), "dd-MM-yyyy")
                        self.entradaFechaI.setDate(fecha)
                        self.entradaFechaI.show()
                        self.entradaTrabajoI.setText(consulta[1])
                        if consulta[8] == "Urgente":
                            self.entradaPrioridadI.setCurrentIndex(1)
                        """REVISION"""
                        # cliente.cambiarIndicadorTerminarMetodo(True)                        
                elif modo ==  "Terminado":                            
                    if self.entradaClaveT.text() == "":
                        cliente.cambiarIndicadorTerminarMetodo(False)
                        self.escribirMensajeMetodo([""])
                        self.entradaClienteT.setText("")
                        self.entradaTrabajoT.setText("")            
                    else:                    
                        consulta         = consultar_trabajo(self.entradaClaveT.text())
                        cliente_consulta = consultar_cliente(consulta[9])                    
                        if consulta[7] == 'Agendado' or consulta[7] == 'En Proceso':                
                            self.entradaClienteT.setText(cliente_consulta[1])
                            self.entradaTrabajoT.setText(consulta[1])
                            cliente.cambiarIndicadorTerminarMetodo(True)
                            self.escribirMensajeMetodo([""])
                        elif consulta[7] == 'Terminado':
                            self.entradaClienteT.setText("")
                            self.entradaTrabajoT.setText("")  
                            mensaje_terminado = mensaje.format("     TRABAJO TERMINADO")
                            self.escribirMensajeMetodo([mensaje_terminado])              

    def ingresarTrabajoMetodo(self, cliente):        
        self.comprobarTrabajoMetodo(cliente, "Terminado")
        if cliente.indicadorIngresar == False:
            notificacion = CuadroAceptar("No se puede completar el registro.\nEl cliente no existe.")
            notificacion.exec_()
        else:
            fecha_objeto    = self.entradaFechaI.date() 
            fecha           = procesar_fecha(str(fecha_objeto.toPython()), "-")            
            mensaje_formato = """{}\n
                                 \tCliente:     \t {}
                                 \tFecha:       \t {}
                                 \tTrabajo:     \t {}
                                 \tDescripción: \t {}
                                 \tD. Vehículo: \t {}
                                 \tPrioridad:   \t {} \n"""
            mensaje_comprobacion = mensaje_formato.format("Se introducirá el siguiente trabajo:",
                                                          self.entradaClienteI.text(), 
                                                          fecha,
                                                          self.entradaTrabajoI.text(),
                                                          self.entradaDescripcionI.toPlainText(),
                                                          self.entradaDVehiculoI.toPlainText(),
                                                          self.entradaPrioridadI.currentText())
            notificacion = CuadroComprobar(mensaje_comprobacion)
            respuesta    = notificacion.exec_()
            if respuesta:
                mensaje_formato = """{}\n
                                     \tClave:       \t {}
                                     \tCliente:     \t {}
                                     \tFecha:       \t {}
                                     \tTrabajo:     \t {}
                                     \tDescripción: \t {}
                                     \tD. Vehículo: \t {}
                                     \tPrioridad:   \t {} \n"""
                cliente_consulta      = buscar_cliente(self.entradaClienteI.text())
                cliente_identificador = cliente_consulta[0][0]  
                if self.entradaClaveI.text() == "":
                    respuesta = ingresar_trabajo(self.entradaTrabajoI.text(), 
                                                 self.entradaDescripcionI.toPlainText(),
                                                 self.entradaDVehiculoI.toPlainText(), 
                                                 "", 
                                                 fecha.replace(" de ", "/"), 
                                                 "", 
                                                 "En Proceso", 
                                                 self.entradaPrioridadI.currentText(),
                                                 cliente_identificador)
                    clave = str(respuesta[0])
                else:           
                    actualizar_trabajo("trabajos_descripcion", self.entradaDescripcionI.toPlainText(), self.entradaClaveI.text())
                    actualizar_trabajo("trabajos_auto", self.entradaDVehiculoI.toPlainText(), self.entradaClaveI.text())   
                    actualizar_trabajo("trabajos_estatus", "En Proceso", self.entradaClaveI.text())                
                    actualizar_trabajo("trabajos_prioridad", self.entradaPrioridadI.currentText(), self.entradaClaveI.text())                
                    actualizar_trabajo("trabajos_clientes", str(cliente_identificador), self.entradaClaveI.text())                
                    clave = self.entradaClaveI.text()
                mensaje_estatus = mensaje_formato.format("Se ha registrado el trabajo:",
                                                         clave,
                                                         self.entradaClienteI.text(), 
                                                         fecha,
                                                         self.entradaTrabajoI.text(),
                                                         self.entradaDescripcionI.toPlainText(),
                                                         self.entradaDVehiculoI.toPlainText(),
                                                         self.entradaPrioridadI.currentText())
                cliente.reiniciarClienteMetodo()                        
                self.limpiarCamposMetodo(True, True, True)
                self.escribirMensajeMetodo([mensaje_estatus])

    def terminarTrabajoMetodo(self, cliente):
        self.comprobarTrabajoMetodo(cliente, "Terminado")
        if cliente.indicadorTerminar == False:
            notificacion = CuadroAceptar("No se puede completar el registro.\nEl trabajo no existe.")
            notificacion.exec_()
        else:
            consulta         = consultar_trabajo(self.entradaClaveT.text())
            fecha_objeto     = self.entradaFechaT.date()   
            fecha_inicial    = procesar_fecha(recuperar_fecha(consulta[5], "/"), "-")
            fecha_final      = procesar_fecha(str(fecha_objeto.toPython()), "-")     
            consulta_cliente = consultar_cliente(consulta[9])       
            cliente_nombre   = consulta_cliente[1]            
            mensaje_formato  = """{}\n
                                  \tCliente:\t {}
                                  \tFecha:\t Del {} al {}
                                  \tTrabajo:\t {}
                                  \tPrecio:\t {} \n"""
            mensaje_comprobacion = mensaje_formato.format(
                                          "Se terminará el siguiente trabajo:",
                                          cliente_nombre, 
                                          fecha_inicial,
                                          fecha_final,
                                          consulta[1],
                                          self.entradaPrecioT.text())
            notificacion = CuadroComprobar(mensaje_comprobacion)
            respuesta    = notificacion.exec_()                        
            if respuesta:
                mensaje_estatus = mensaje_formato.format(
                                          "Se terminó el siguiente trabajo:",
                                          cliente_nombre,                   
                                          fecha_inicial,
                                          fecha_final,
                                          consulta[1],
                                          self.entradaPrecioT.text())
                cliente.reiniciarClienteMetodo()   
                actualizar_trabajo("trabajos_precio", self.entradaPrecioT.text(), self.entradaClaveT.text())
                actualizar_trabajo("trabajos_final", fecha_final.replace(" de ", "/"), self.entradaClaveT.text())
                actualizar_trabajo("trabajos_estatus", "Terminado", self.entradaClaveT.text())
                self.limpiarCamposMetodo(False, True, False)                
                self.escribirMensajeMetodo([""])
                self.escribirMensajeMetodo([mensaje_estatus])

    def agendarTrabajoMetodo(self, cliente):
        self.comprobarClienteMetodo(cliente)
        if cliente.indicadorAgendar == False:
            notificacion = CuadroAceptar("No se puede agendar el trabajo.\nEl cliente no existe.")
            notificacion.exec_()
        else:
            fecha_objeto    = self.entradaFechaA.date() 
            fecha           = procesar_fecha(str(fecha_objeto.toPython()), "-")            
            mensaje_formato = """{}\n
                                 \tCliente:   \t {}
                                 \tFecha:     \t {}
                                 \tTrabajo:   \t {}
                                 \tPrioridad: \t {} \n"""
            mensaje_comprobacion = mensaje_formato.format("Se agendará el siguiente trabajo:",
                                                          self.entradaClienteA.text(), 
                                                          fecha,
                                                          self.entradaTrabajoA.text(),
                                                          self.entradaPrioridadA.currentText())
            notificacion = CuadroComprobar(mensaje_comprobacion)
            respuesta    = notificacion.exec_()
            if respuesta:
                mensaje_formato = """{}\n
                                     \tClave:     \t\t {}
                                     \tCliente:   \t\t {}
                                     \tFecha:     \t\t {}
                                     \tTrabajo:   \t {} 
                                     \tPrioridad: \t {} \n"""                
                cliente.reiniciarClienteMetodo()                        
                busqueda  = buscar_cliente(self.entradaClienteA.text())
                resultado = ingresar_trabajo(self.entradaTrabajoA.text(), 
                                             "", 
                                             "", 
                                             "", 
                                             fecha.replace(" de ", "/"), 
                                             "", 
                                             "Agendado", 
                                             self.entradaPrioridadA.currentText(), 
                                             busqueda[0][0])
                mensaje_estatus = mensaje_formato.format("Se ha agendado el trabajo:",
                                                         resultado[0],
                                                         self.entradaClienteA.text(), 
                                                         fecha,
                                                         self.entradaTrabajoA.text(),
                                                         self.entradaPrioridadA.currentText())
                self.limpiarCamposMetodo(False, False, True)
                self.escribirMensajeMetodo([""])
                self.escribirMensajeMetodo([mensaje_estatus])

    def limpiarCamposMetodo(self, indicador_uno, indicador_dos, indicador_tres):
        """Limpia todos los campos de los formularios."""        
        if indicador_uno:
            # Limpiar formulario ingresar
            self.entradaClienteI.setText("")
            fecha = QDate.fromString("01-01-2000", "MM-dd-yyyy")
            self.entradaFechaI.show()
            self.entradaFechaI.setDate(fecha)
            self.entradaTrabajoI.setText("")
            self.entradaDescripcionI.clear()
            self.entradaDVehiculoI.clear()
            self.entradaClaveI.setText("")
            self.entradaPrioridadI.setCurrentIndex(0)
        if indicador_dos:
            # Limpiar formulario terminar
            self.entradaClaveT.setText("")
            self.entradaClienteT.setText("")
            self.entradaTrabajoT.setText("")
            self.entradaPrecioT.setText("")
            fecha = QDate.fromString("01-01-2000", "MM-dd-yyyy")
            self.entradaFechaT.setDate(fecha)
            self.entradaFechaT.show()
        if indicador_tres:
            # Limpiar formulario agendar
            self.entradaClienteA.setText("")
            fecha = QDate.fromString("01-01-2000", "MM-dd-yyyy")
            self.entradaFechaA.setDate(fecha)
            self.entradaFechaA.show()
            self.entradaTrabajoA.setText("")

    def escribirMensajeMetodo(self, mensaje):
        self.visor.clear()
        for elemento in mensaje:
            self.visor.insertPlainText("{}\n".format(str(elemento)))     


# ***********************************************************************************
# ******************************    Segunda Pestaña    ******************************
# ***********************************************************************************

class WidgetConsultaClientes(QWidget):
    def __init__(self, cliente):
        super().__init__()
        # Layouts Contenedores
        self.contenedorHorizontal = QHBoxLayout()
        # Formularios
        self.contenedorCliente = QFormLayout()
        self.contenedorTrabajo = QFormLayout()
        # Formulario Cliente
        self.etiquetaCliente       = QLabel("Buscar Cliente")
        self.informacionCliente    = QLabel("Cliente")
        self.lineaCliente          = QHLine()
        self.entradaCliente        = QLineEdit()
        self.descripcionCliente    = QPlainTextEdit()
        self.botonVerTodos         = QPushButton("Ver Todos")
        self.botonAgregarCliente   = QPushButton("+ Agregar Cliente")
        self.botonContactarCliente = QPushButton("Contactar Cliente")
        self.botonEditarCliente    = QPushButton("Editar Cliente")
        self.botonVerTodos.setObjectName("VerTodos")
        self.botonAgregarCliente.setObjectName("AgregarCliente")
        self.descripcionCliente.setReadOnly(True)
        self.contenedorCliente.addRow(self.etiquetaCliente)
        self.contenedorCliente.addRow(self.lineaCliente)
        self.contenedorCliente.addRow(self.entradaCliente)
        self.contenedorCliente.addRow(self.botonVerTodos)
        self.contenedorCliente.addRow(self.botonAgregarCliente)
        self.contenedorCliente.addRow(self.informacionCliente)
        self.contenedorCliente.addRow(QHLine())
        self.contenedorCliente.addRow(self.descripcionCliente)
        self.contenedorCliente.addRow(QLabel("\n"))
        self.contenedorCliente.addRow(self.botonContactarCliente)
        self.contenedorCliente.addRow(self.botonEditarCliente)
        self.contenedorCliente.addRow(QLabel(""))
        # Formulario Trabajo
        self.etiquetaTrabajo    = QLabel("Trabajos")
        self.lineaTrabajo       = QHLine()
        self.listaTrabajo       = QListWidget()
        self.botonVerTrabajo    = QPushButton("Ver Trabajo")
        self.botonEditarTrabajo = QPushButton("Editar Trabajo")        
        self.contenedorTrabajo.addRow(self.etiquetaTrabajo)
        self.contenedorTrabajo.addRow(self.lineaTrabajo)
        self.contenedorTrabajo.addRow(QLabel("Clave\tCliente\t       Prioridad\t     Estatus\t        Trabajo"))
        self.contenedorTrabajo.addRow(self.listaTrabajo)
        self.contenedorTrabajo.addRow(QLabel("\n"))
        self.contenedorTrabajo.addRow(self.botonVerTrabajo)
        self.contenedorTrabajo.addRow(self.botonEditarTrabajo)
        self.contenedorTrabajo.addRow(QLabel(""))
        # Introducir Formularios
        self.contenedorHorizontal.addLayout(self.contenedorCliente)
        self.contenedorHorizontal.addLayout(self.contenedorTrabajo)
        self.setLayout(self.contenedorHorizontal)
        # Agregar Funciones
        self.entradaCliente.textChanged.connect(self.comprobarClienteMetodo)
        self.botonVerTodos.clicked.connect(self.verTodosMetodo)
        self.botonAgregarCliente.clicked.connect(lambda: self.agregarClienteMetodo(cliente))
        self.botonEditarCliente.clicked.connect(lambda: self.editarClienteMetodo(cliente))
        self.listaTrabajo.itemDoubleClicked.connect(lambda: self.verTrabajoMetodo(self.listaTrabajo.selectedItems()))
        self.botonVerTrabajo.clicked.connect(lambda: self.verTrabajoMetodo(self.listaTrabajo.selectedItems()))
        self.botonEditarTrabajo.clicked.connect(lambda: self.editarTrabajoMetodo(self.listaTrabajo.selectedItems()))

    def editarTrabajoMetodo(self, seleccionados):
        lista        = seleccionados
        eleccion     = lista[0].text()
        letras       = eleccion.split()
        clave        = letras[0]
        trabajo      = consultar_trabajo(clave)
        datos        = [trabajo[1], trabajo[2], trabajo[3], trabajo[4], trabajo[5], trabajo[6], trabajo[7], trabajo[8]]        
        ventana      = CuadroEditarTrabajo(datos)
        resultado    = ventana.exec_()
        mensaje_uno  = "Se actualizará el trabajo con los siguientes datos: \n\n"
        mensaje_dos  = """\tTrabajo:  \t\t{}\n\tDescripción:  \t{}\n\tD. Vehículo:  \t{}\n\tPrecio:  \t\t{}\n\tFecha Inicio:  \t{}\n\tFecha Final:  \t{}\n\tPrioridad:  \t{}\n\tEstatus:  \t\t{}\n"""
        mensaje_tres = mensaje_dos.format(diccionario_agregar_trabajo["Trabajo"],
                                          diccionario_agregar_trabajo["Descripción"],
                                          diccionario_agregar_trabajo["D. Vehículo"],
                                          diccionario_agregar_trabajo["Precio"],
                                          diccionario_agregar_trabajo["Fecha Inicio"],
                                          diccionario_agregar_trabajo["Fecha Final"],
                                          diccionario_agregar_trabajo["Prioridad"],
                                          diccionario_agregar_trabajo["Estatus"])
        mensaje = mensaje_uno + mensaje_tres
        if resultado:        
            comprobar     = CuadroComprobar(mensaje)
            resultado_dos = comprobar.exec_()
            if resultado_dos:
                actualizar_vector_trabajo(diccionario_agregar_trabajo["Trabajo"], 
                                          diccionario_agregar_trabajo["Descripción"],
                                          diccionario_agregar_trabajo["D. Vehículo"], 
                                          diccionario_agregar_trabajo["Precio"], 
                                          diccionario_agregar_trabajo["Fecha Inicio"].replace(" de ", "/"), 
                                          diccionario_agregar_trabajo["Fecha Final"].replace(" de ", "/"), 
                                          diccionario_agregar_trabajo["Estatus"],
                                          diccionario_agregar_trabajo["Prioridad"],
                                          clave)        

    def verTrabajoMetodo(self, seleccionados):
        lista    = seleccionados
        eleccion = lista[0].text()
        letras   = eleccion.split()
        clave    = letras[0]
        trabajo  = consultar_trabajo(clave)
        vector   = consultar_cliente(trabajo[9])
        nombre   = vector[1]
        mensaje  = """\n    {}\n    __________________________________________________________________    \n                      
                      Clave:        \t{}\n
                      Cliente:      \t{}\n
                      Estatus:      \t{}\n
                      Prioridad:    \t{}\n
                      Descripción:  \t{}\n
                      D. Vehículo:  \t{}\n
                      Fecha Inicio: \t{}\n
                      Fecha Final:  \t{}\n
                      Precio:       \t{}\n""".format(trabajo[1].upper(), 
                                                     str(trabajo[0]),
                                                     nombre + "  (" + str(trabajo[9]) + ")",
                                                     trabajo[7],
                                                     trabajo[8], 
                                                     trabajo[2], 
                                                     trabajo[3], 
                                                     trabajo[5].replace("/", " de "), 
                                                     trabajo[6].replace("/", " de "), 
                                                     trabajo[4])
        ventana  = CuadroMostrarTrabajo(mensaje)
        ventana.exec_()

    def comprobarClienteMetodo(self):
        texto   = str(self.entradaCliente.text())
        mensaje = """\n\t\t  **********************************
                     \n\t\t      CLIENTE NO ENCONTRADO
                     \n\t\t  **********************************"""       
        mensaje_cliente = "" 
        error_cliente   = False
        vector_cliente  = procesar_texto_clientes(texto)    
        if vector_cliente == 0:
            self.escribirMensajeMetodo([mensaje])
            self.listaTrabajo.clear()
        else:
            mensaje_cliente = """\nClave: \t\t{}\n\nNombre: \t{}\n\nTeléfono: \t{}\n\nDirección: \t{}\n\nCorreo: \t{}
            """.format(vector_cliente[0], vector_cliente[1], vector_cliente[2], vector_cliente[3], vector_cliente[4])
            self.escribirMensajeMetodo([mensaje_cliente])            
            self.verTrabajosMetodo(vector_cliente[0])            
        if texto == "":
            self.listaTrabajo.clear()
            self.escribirMensajeMetodo([""])        

    def verTodosMetodo(self):
        ventana = CuadroMostrarClientes()
        ventana.exec_()

    def agregarClienteMetodo(self, cliente):
        ventana   = CuadroAgregarCliente()
        respuesta = ventana.exec_()
        if respuesta:
            mensaje_formato = """{}\n
                                 \tNombre:    \t{}
                                 \tTelefono:  \t{}
                                 \tDirección: \t{}
                                 \tEmail:     \t\t{} \n"""            
            mensaje_confirmacion = mensaje_formato.format("Se introducirán los datos del siguiente cliente:",
                             diccionario_agregar_cliente["Cliente"], 
                             diccionario_agregar_cliente["Teléfono"], 
                             diccionario_agregar_cliente["Dirección"], 
                             diccionario_agregar_cliente["Email"])
            confirmacion           = CuadroComprobar(mensaje_confirmacion)
            respuesta_confirmacion = confirmacion.exec_()
            if respuesta_confirmacion:
                mensaje_formato = """{}\n
                                     Clave:     \t\t{}
                                     Nombre:    \t{}
                                     Telefono:  \t{}
                                     Dirección: \t{}
                                     Email:     \t\t{} \n"""            
                respuesta = ingresar_cliente(diccionario_agregar_cliente["Cliente"], 
                                             diccionario_agregar_cliente["Teléfono"], 
                                             diccionario_agregar_cliente["Dirección"], 
                                             diccionario_agregar_cliente["Email"])
                mensaje_cliente_nuevo = mensaje_formato.format("Se ha introducido en la base de datos al siguiente cliente:",
                                                                str(respuesta[0]),
                                                                diccionario_agregar_cliente["Cliente"], 
                                                                diccionario_agregar_cliente["Teléfono"], 
                                                                diccionario_agregar_cliente["Dirección"], 
                                                                diccionario_agregar_cliente["Email"])
                self.escribirMensajeMetodo([mensaje_cliente_nuevo])

    def editarClienteMetodo(self, cliente):
        texto         = str(self.entradaCliente.text())
        vector        = procesar_texto_clientes(texto)    
        identificador = vector[0]
        datos         = [vector[1], vector[2], vector[3], vector[4]]
        ventana       = CuadroEditarCliente(datos)
        respuesta     = ventana.exec_()
        if respuesta:
            mensaje_formato = """{}\n
                                 \tNombre:    \t{}
                                 \tTelefono:  \t{}
                                 \tDirección: \t{}
                                 \tEmail:     \t\t{} \n"""            
            mensaje_confirmacion = mensaje_formato.format("Se actualizarán los datos del cliente:",
                                                          diccionario_agregar_cliente["Cliente"], 
                                                          diccionario_agregar_cliente["Teléfono"], 
                                                          diccionario_agregar_cliente["Dirección"], 
                                                          diccionario_agregar_cliente["Email"])
            confirmacion           = CuadroComprobar(mensaje_confirmacion)
            respuesta_confirmacion = confirmacion.exec_()
            if respuesta_confirmacion:
                mensaje_formato = """{}\n\n\tNombre:    \t{}\n\n\tTelefono:  \t{}\n\n\tDirección: \t{}\n\n\tEmail:     \t\t{} \n""" 
                actualizar_vector_cliente(diccionario_agregar_cliente["Cliente"], 
                                          diccionario_agregar_cliente["Teléfono"], 
                                          diccionario_agregar_cliente["Dirección"], 
                                          diccionario_agregar_cliente["Email"],
                                          identificador)
                mensaje_cliente_nuevo = mensaje_formato.format("Se han actualizado los datos del cliente:",
                                                               diccionario_agregar_cliente["Cliente"], 
                                                               diccionario_agregar_cliente["Teléfono"], 
                                                               diccionario_agregar_cliente["Dirección"], 
                                                               diccionario_agregar_cliente["Email"])
                self.escribirMensajeMetodo([mensaje_cliente_nuevo])

    def verTrabajosMetodo(self, identificador):
        consulta  = consultar_trabajos()        
        trabajos  = []
        renglones = []
        buscador  = str(identificador)
        for elemento in consulta:
            if str(elemento[len(elemento) - 1]) == buscador:
                trabajos.append(elemento)
        for elemento in trabajos:
            mensaje_renglon = "   {}         {}            {}        {}          {}"
            renglones.append(mensaje_renglon.format(elemento[0], 
                                                    elemento[len(elemento) - 1], 
                                                    elemento[len(elemento) - 2], 
                                                    elemento[len(elemento) - 3], 
                                                    elemento[1]))
        self.listaTrabajo.clear()
        self.listaTrabajo.addItems(renglones)

    def escribirMensajeMetodo(self, mensaje):
        self.descripcionCliente.clear()
        for elemento in mensaje:
            self.descripcionCliente.insertPlainText("{}\n".format(str(elemento)))
    

# **********************************************************************************
# ******************************    Tercer Pestaña    ******************************
# **********************************************************************************

class WidgetConsultaTrabajos(QWidget):
    def __init__(self):
        super().__init__()
        contadores = contar_trabajos()
        # Layouts Contenedores
        self.contenedorHorizontal = QHBoxLayout()
        # Formularios
        self.contenedorEstatus = QFormLayout()
        self.contenedorTrabajo = QFormLayout()
        # Formulario Estatus
        self.etiquetaEnProceso  = QLabel("Trabajos en Proceso")
        self.etiquetaAgendado   = QLabel("Trabajos Agendados")
        self.etiquetaTerminado  = QLabel("Trabajos Terminados")        
        self.entradaEnProceso   = QLineEdit()
        self.entradaAgendado    = QLineEdit()
        self.entradaTerminado   = QLineEdit()
        self.botonEnProceso     = QPushButton("Ver Trabajos")
        self.botonAgendado      = QPushButton("Ver Trabajos")
        self.botonTerminado     = QPushButton("Ver Trabajos")
        self.botonActualizar    = QPushButton("Actualizar")
        self.entradaEnProceso.setReadOnly(True)
        self.entradaAgendado.setReadOnly(True)
        self.entradaTerminado.setReadOnly(True)
        self.entradaEnProceso.setObjectName("EntradaConsulta")
        self.entradaAgendado.setObjectName("EntradaConsulta")
        self.entradaTerminado.setObjectName("EntradaConsulta")
        self.botonEnProceso.setObjectName("BotonConsulta")
        self.botonAgendado.setObjectName("BotonConsulta")
        self.botonTerminado.setObjectName("BotonConsulta")
        self.botonActualizar.setObjectName("BotonActualizar")
        self.entradaEnProceso.setText(str(contadores[2]))
        self.entradaAgendado.setText(str(contadores[0]))
        self.entradaTerminado.setText(str(contadores[1]))        
        self.contenedorEstatus.addRow(self.etiquetaEnProceso)
        self.contenedorEstatus.addRow(QHLine())
        self.contenedorEstatus.addRow(self.entradaEnProceso, self.botonEnProceso)
        self.contenedorEstatus.addRow(QLabel("\n\n"))
        self.contenedorEstatus.addRow(self.etiquetaAgendado)
        self.contenedorEstatus.addRow(QHLine())
        self.contenedorEstatus.addRow(self.entradaAgendado, self.botonAgendado)
        self.contenedorEstatus.addRow(QLabel("\n\n"))
        self.contenedorEstatus.addRow(self.etiquetaTerminado)
        self.contenedorEstatus.addRow(QHLine())
        self.contenedorEstatus.addRow(self.entradaTerminado, self.botonTerminado)
        self.contenedorEstatus.addRow(QLabel("\n\n"))
        self.contenedorEstatus.addRow(self.botonActualizar)
        # Formulario Trabajo
        self.etiquetaTrabajo    = QLabel("Buscar Trabajo")
        self.informacionTrabajo = QLabel("Trabajo")
        self.lineaTrabajo       = QHLine()
        self.entradaTrabajo     = QLineEdit()
        self.visorTrabajo       = QPlainTextEdit()
        self.botonEditarTrabajo = QPushButton("Editar Trabajo")
        self.visorTrabajo.setReadOnly(True)
        self.contenedorTrabajo.addRow(self.etiquetaTrabajo)
        self.contenedorTrabajo.addRow(self.lineaTrabajo)
        self.contenedorTrabajo.addRow(self.entradaTrabajo)
        self.contenedorTrabajo.addRow(QLabel("\n\n"))
        self.contenedorTrabajo.addRow(self.informacionTrabajo)
        self.contenedorTrabajo.addRow(QHLine())
        self.contenedorTrabajo.addRow(self.visorTrabajo)
        self.contenedorTrabajo.addRow(QLabel("\n"))
        self.contenedorTrabajo.addRow(self.botonEditarTrabajo)
        self.contenedorTrabajo.addRow(QLabel(""))
        # Introducir Formularios
        self.contenedorHorizontal.addLayout(self.contenedorEstatus)
        self.contenedorHorizontal.addLayout(self.contenedorTrabajo)
        self.setLayout(self.contenedorHorizontal)
        # Funciones
        self.botonActualizar.clicked.connect(self.actualizarContadoresMetodo)
        self.botonEnProceso.clicked.connect(lambda: self.mostrarTrabajosListaMetodo("En Proceso"))
        self.botonAgendado.clicked.connect(lambda: self.mostrarTrabajosListaMetodo("Agendado"))
        self.botonTerminado.clicked.connect(lambda: self.mostrarTrabajosListaMetodo("Terminado"))
        self.entradaTrabajo.textChanged.connect(lambda: self.buscarTrabajoMetodo(self.entradaTrabajo.text()))
        self.botonEditarTrabajo.clicked.connect(lambda: self.editarTrabajoMetodo(self.entradaTrabajo.text()))

    def editarTrabajoMetodo(self, clave):
        clave        = clave.strip()
        lista        = buscar_trabajo(str(clave))        
        trabajo      = lista[0]
        datos        = [trabajo[1], trabajo[2], trabajo[3], trabajo[4], trabajo[5], trabajo[6], trabajo[7], trabajo[8]]        
        ventana      = CuadroEditarTrabajo(datos)
        resultado    = ventana.exec_()        
        mensaje_uno  = "Se actualizará el trabajo con los siguientes datos: \n\n"
        mensaje_dos  = """\tTrabajo:  \t\t{}\n\tDescripción:  \t{}\n\tD. Vehículo:  \t{}\n\tPrecio:  \t\t{}\n\tFecha Inicio:  \t{}\n\tFecha Final:  \t{}\n\tPrioridad:  \t{}\n\tEstatus:  \t\t{}\n"""
        mensaje_tres = mensaje_dos.format(diccionario_agregar_trabajo["Trabajo"],
                                          diccionario_agregar_trabajo["Descripción"],
                                          diccionario_agregar_trabajo["D. Vehículo"],
                                          diccionario_agregar_trabajo["Precio"],
                                          diccionario_agregar_trabajo["Fecha Inicio"],
                                          diccionario_agregar_trabajo["Fecha Final"],
                                          diccionario_agregar_trabajo["Prioridad"],
                                          diccionario_agregar_trabajo["Estatus"])
        mensaje = mensaje_uno + mensaje_tres
        if resultado:        
            comprobar     = CuadroComprobar(mensaje)
            resultado_dos = comprobar.exec_()
            if resultado_dos:
                actualizar_vector_trabajo(diccionario_agregar_trabajo["Trabajo"], 
                                          diccionario_agregar_trabajo["Descripción"],
                                          diccionario_agregar_trabajo["D. Vehículo"], 
                                          diccionario_agregar_trabajo["Precio"], 
                                          diccionario_agregar_trabajo["Fecha Inicio"].replace(" de ", "/"), 
                                          diccionario_agregar_trabajo["Fecha Final"].replace(" de ", "/"), 
                                          diccionario_agregar_trabajo["Estatus"],
                                          diccionario_agregar_trabajo["Prioridad"],
                                          clave)        

    def buscarTrabajoMetodo(self, clave):        
        clave   = clave.strip()
        mensaje = """\n\t\t\t\t\t*********************************
                     \n\t\t\t\t\t  CLIENTE NO ENCONTRADO
                     \n\t\t\t\t\t*********************************"""   
        if clave.isdigit():
            lista = buscar_trabajo(str(clave))
            vector   = consultar_cliente(lista[0][9])
            nombre   = vector[1]
            if lista != None and lista != []:
                mensaje  = """\n    {}\n    __________________________________________________________________    \n                      
                              Clave:        \t{}\n
                              Cliente:      \t{}\n
                              Estatus:      \t{}\n
                              Prioridad:    \t{}\n
                              Descripción:  \t{}\n
                              D. Vehículo:  \t{}\n
                              Fecha Inicio: \t{}\n
                              Fecha Final:  \t{}\n
                              Precio:       \t{}\n""".format(lista[0][1].upper(), 
                                                             str(lista[0][0]),
                                                             nombre + "  (" + str(lista[0][9]) + ")",
                                                             lista[0][7],
                                                             lista[0][8], 
                                                             lista[0][2], 
                                                             lista[0][3], 
                                                             lista[0][5].replace("/", " de "), 
                                                             lista[0][6].replace("/", " de "), 
                                                             lista[0][4])
        if clave == "":
            mensaje = ""
        self.escribirMensajeMetodo([mensaje])


    def escribirMensajeMetodo(self, mensaje):
        self.visorTrabajo.clear()
        for elemento in mensaje:
            self.visorTrabajo.insertPlainText("{}\n".format(str(elemento)))     

    def mostrarTrabajosListaMetodo(self, indicador): 
        ventana = CuadroMostrarTrabajosLista(indicador)
        ventana.exec_()

    def actualizarContadoresMetodo(self):
        contadores = contar_trabajos()
        self.entradaEnProceso.setText(str(contadores[2]))
        self.entradaAgendado.setText(str(contadores[0]))
        self.entradaTerminado.setText(str(contadores[1]))        


# **********************************************************************************
# ******************************    Cuarta Pestaña    ******************************
# **********************************************************************************

class WidgetInventarios(QWidget):
    def __init__(self):
        super().__init__()
        self.contenedor             = QHBoxLayout()
        # Contenedores
        self.contenedorHerramientas = QFormLayout()        
        self.contenedorRefacciones  = QFormLayout()
        # Herramientas
        self.etiquetaHerramientas        = QLabel("Herramientas")
        self.etiquetaBuscarHerramienta   = QLabel("Buscar")
        self.entradaBuscarHerremienta    = QLineEdit()
        self.visorDescripcionHerramienta = QPlainTextEdit()
        self.botonVerTodoHerramienta     = QPushButton("Ver Todo")
        self.botonAnadirHerramienta      = QPushButton("Añadir")
        self.botonEditarHerramienta      = QPushButton("Editar")
        self.botonEliminarHerramienta    = QPushButton("Eliminar")       
        self.botonVerTodoHerramienta.setObjectName("VerTodo") 
        self.visorDescripcionHerramienta.setReadOnly(True)
        self.contenedorHerramientas.addRow(self.etiquetaHerramientas)
        self.contenedorHerramientas.addRow(QHLine())
        self.contenedorHerramientas.addRow(self.etiquetaBuscarHerramienta, self.entradaBuscarHerremienta)
        self.contenedorHerramientas.addRow(self.botonVerTodoHerramienta)
        self.contenedorHerramientas.addRow(self.visorDescripcionHerramienta)
        self.contenedorHerramientas.addRow(self.botonAnadirHerramienta)
        self.contenedorHerramientas.addRow(self.botonEditarHerramienta)
        self.contenedorHerramientas.addRow(self.botonEliminarHerramienta)
        self.contenedorHerramientas.addRow(QLabel(""))
        # Refacciones
        self.etiquetaRefacciones         = QLabel("Refacciones")
        self.etiquetaBuscarRefacciones   = QLabel("Buscar")
        self.entradaBuscarRefacciones    = QLineEdit()
        self.visorDescripcionRefacciones = QPlainTextEdit()
        self.botonVerTodoRefacciones     = QPushButton("Ver Todo")
        self.botonAnadirRefacciones      = QPushButton("Añadir")
        self.botonEditarRefacciones      = QPushButton("Editar")
        self.botonEliminarRefacciones    = QPushButton("Eliminar")        
        self.botonVerTodoRefacciones.setObjectName("VerTodo")
        self.visorDescripcionRefacciones.setReadOnly(True)
        self.contenedorRefacciones.addRow(self.etiquetaRefacciones)
        self.contenedorRefacciones.addRow(QHLine())
        self.contenedorRefacciones.addRow(self.etiquetaBuscarRefacciones, self.entradaBuscarRefacciones)
        self.contenedorRefacciones.addRow(self.botonVerTodoRefacciones)
        self.contenedorRefacciones.addRow(self.visorDescripcionRefacciones)
        self.contenedorRefacciones.addRow(self.botonAnadirRefacciones)
        self.contenedorRefacciones.addRow(self.botonEditarRefacciones)
        self.contenedorRefacciones.addRow(self.botonEliminarRefacciones)        
        self.contenedorRefacciones.addRow(QLabel(""))
        # Formularios
        self.contenedor.addLayout(self.contenedorHerramientas)
        self.contenedor.addLayout(self.contenedorRefacciones)
        self.setLayout(self.contenedor)
        # Funciones
        self.entradaBuscarHerremienta.textChanged.connect(lambda: self.buscarHerramientaMetodo(self.entradaBuscarHerremienta.text()))
        self.entradaBuscarRefacciones.textChanged.connect(lambda: self.buscarRefaccionesMetodo(self.entradaBuscarRefacciones.text()))
        self.botonVerTodoHerramienta.clicked.connect(lambda: self.verTodoMetodo("Herramientas"))
        self.botonVerTodoRefacciones.clicked.connect(lambda: self.verTodoMetodo("Refacciones"))
        self.botonAnadirHerramienta.clicked.connect(lambda: self.anadirMetodo("Herramientas"))
        self.botonAnadirRefacciones.clicked.connect(lambda: self.anadirMetodo("Refacciones"))
        self.botonEditarHerramienta.clicked.connect(lambda: self.editarMetodo("Herramientas"))
        self.botonEditarRefacciones.clicked.connect(lambda: self.editarMetodo("Refacciones"))        
        self.botonEliminarHerramienta.clicked.connect(lambda: self.eliminarMetodo("Herramientas"))
        self.botonEliminarRefacciones.clicked.connect(lambda: self.eliminarMetodo("Refacciones"))        

    def editarMetodo(self, indicador):
        identificador = ""
        if indicador == "Herramientas":
            consulta      = consultar_herramienta(self.entradaBuscarHerremienta.text())
            identificador = self.entradaBuscarHerremienta.text()
        elif indicador == "Refacciones":
            consulta      = consultar_inventario(self.entradaBuscarRefacciones.text())        
            identificador = self.entradaBuscarRefacciones.text()
        datos            = [consulta[1], consulta[2], consulta[3], consulta[4]]
        ventana          = CuadroEditarArticulos(indicador, datos)
        respuesta        = ventana.exec_()
        mensaje_formato  = """Se actualizará la siguiente {}:\n
                              \t{}:\t {}
                              \tDescripción:\t {}
                              \tCantidad:\t {} unidades
                              \tEstado:\t\t {} \n"""
        if respuesta:
            if indicador == "Herramientas":
                mensaje = mensaje_formato.format("Herramienta",
                                                 "Herramienta", 
                                                 diccionario_agregar_producto["Nombre"],
                                                 diccionario_agregar_producto["Descripción"],
                                                 diccionario_agregar_producto["Unidades"],
                                                 diccionario_agregar_producto["Estado"])
            elif indicador == "Refacciones":
                mensaje = mensaje_formato.format("Refacción",
                                                 "Refacción",
                                                 diccionario_agregar_producto["Nombre"],
                                                 diccionario_agregar_producto["Descripción"],
                                                 diccionario_agregar_producto["Unidades"],
                                                 diccionario_agregar_producto["Estado"])
            notificacion           = CuadroComprobar(mensaje)
            notificacion_respuesta = notificacion.exec_()
            if notificacion_respuesta: 
                if indicador == "Herramientas":
                    actualizar_vector_herramienta(diccionario_agregar_producto["Nombre"], 
                                                  diccionario_agregar_producto["Descripción"],  
                                                  str(diccionario_agregar_producto["Unidades"]), 
                                                  diccionario_agregar_producto["Estado"], 
                                                  identificador)
                elif indicador == "Refacciones":
                    actualizar_vector_inventario(diccionario_agregar_producto["Nombre"], 
                                                 diccionario_agregar_producto["Descripción"], 
                                                 str(diccionario_agregar_producto["Unidades"]), 
                                                 diccionario_agregar_producto["Estado"], 
                                                 identificador)
                if indicador == "Herramientas":
                    consulta = consultar_herramienta(self.entradaBuscarHerremienta.text())
                elif indicador == "Refacciones":
                    consulta = consultar_inventario(self.entradaBuscarRefacciones.text())        
                mensaje = """\n    {}\n    __________________________________________________________________    \n                      
                            Clave: \t{}\n
                            Detalle: \t{}\n
                            Número de Unidades: \t{}\n
                            Estado: \t{}\n""".format(consulta[1].upper(), 
                                                     consulta[0],
                                                     consulta[2], 
                                                     consulta[3], 
                                                     consulta[4])
                if indicador == "Herramientas":
                    self.escribirMensajeHerramientaMetodo([mensaje])
                elif indicador == "Refacciones":
                    self.escribirMensajeRefaccionesMetodo([mensaje])

    def eliminarMetodo(self, modo):
        mensaje      = "Se eliminará el elemento seleccionado"
        notificacion = CuadroComprobar(mensaje)
        respuesta    = notificacion.exec_()
        if respuesta:
            if modo == "Herramientas":
                eliminar_dato("herramientas", self.entradaBuscarHerremienta.text())
            elif modo == "Refacciones":
                eliminar_dato("inventario", self.entradaBuscarRefacciones.text())

    def anadirMetodo(self, indicador):
        ventana          = CuadroAnadirArticulos(indicador)
        respuesta        = ventana.exec_()
        mensaje_formato  = """Se agregará la siguiente {}:\n
                              \t{}:\t {}
                              \tDescripción:\t {}
                              \tCantidad:\t {} unidades
                              \tEstado:\t\t {} \n"""
        if respuesta:
            if indicador == "Herramientas":
                mensaje = mensaje_formato.format("Herramienta",
                                                 "Herramienta", 
                                                 diccionario_agregar_producto["Nombre"],
                                                 diccionario_agregar_producto["Descripción"],
                                                 diccionario_agregar_producto["Unidades"],
                                                 diccionario_agregar_producto["Estado"])
            elif indicador == "Refacciones":
                mensaje = mensaje_formato.format("Refacción",
                                                 "Refacción",
                                                 diccionario_agregar_producto["Nombre"],
                                                 diccionario_agregar_producto["Descripción"],
                                                 diccionario_agregar_producto["Unidades"],
                                                 diccionario_agregar_producto["Estado"])
            notificacion           = CuadroComprobar(mensaje)
            notificacion_respuesta = notificacion.exec_()
            if notificacion_respuesta: 
                if indicador == "Herramientas":
                    ingresar_herramienta(diccionario_agregar_producto["Nombre"], 
                                         diccionario_agregar_producto["Descripción"], 
                                         str(diccionario_agregar_producto["Unidades"]), 
                                         diccionario_agregar_producto["Estado"])
                elif indicador == "Refacciones":
                    ingresar_inventario(diccionario_agregar_producto["Nombre"], 
                                        diccionario_agregar_producto["Descripción"], 
                                        str(diccionario_agregar_producto["Unidades"]), 
                                        diccionario_agregar_producto["Estado"])


    def verTodoMetodo(self, indicador):
        ventana = CuadroMostrarArticulosLista(indicador)
        ventana.exec_()

    def buscarRefaccionesMetodo(self, clave):        
        clave   = clave.strip()
        mensaje = """\n\t\t***************************************
                     \n\t\t  ARTÍCULO NO ENCONTRADO
                     \n\t\t***************************************"""   
        if clave.isdigit():
            lista = buscar_inventario(str(clave))
            if lista != None and lista != []:
                mensaje  = """\n    {}\n    __________________________________________________________________    \n                      
                              Clave: \t{}\n
                              Detalle: \t{}\n
                              Número de Unidades: \t{}\n
                              Estado: \t{}\n""".format(lista[0][1].upper(), 
                                                       lista[0][0],
                                                       lista[0][2], 
                                                       lista[0][3], 
                                                       lista[0][4])
        if clave == "":
            mensaje = ""
        self.escribirMensajeRefaccionesMetodo([mensaje])

    def buscarHerramientaMetodo(self, clave):        
        clave   = clave.strip()
        mensaje = """\n\t\t***************************************
                     \n\t\t  HERRAMIENTA NO ENCONTRADA
                     \n\t\t***************************************"""   
        if clave.isdigit():
            lista = buscar_herramienta(str(clave))
            if lista != None and lista != []:
                mensaje  = """\n    {}\n    __________________________________________________________________    \n                      
                              Clave: \t{}\n
                              Detalle: \t{}\n
                              Número de Unidades: \t{}\n
                              Estado: \t{}\n""".format(lista[0][1].upper(), 
                                                       lista[0][0],
                                                       lista[0][2], 
                                                       lista[0][3], 
                                                       lista[0][4])
        if clave == "":
            mensaje = ""
        self.escribirMensajeHerramientaMetodo([mensaje])

    def escribirMensajeHerramientaMetodo(self, mensaje):
        self.visorDescripcionHerramienta.clear()
        for elemento in mensaje:
            self.visorDescripcionHerramienta.insertPlainText("{}\n".format(str(elemento)))

    def escribirMensajeRefaccionesMetodo(self, mensaje):
        self.visorDescripcionRefacciones.clear()
        for elemento in mensaje:
            self.visorDescripcionRefacciones.insertPlainText("{}\n".format(str(elemento)))


# **********************************************************************************
# ******************************    Quinta Pestaña    ******************************
# **********************************************************************************

class WidgetRecibos(QWidget):
    def __init__(self):
        super().__init__()
        self.contenedorVertical = QVBoxLayout()
        self.contenedorSuperior = QHBoxLayout()
        self.contenedorInferior = QVBoxLayout()
        self.widgetUno    = CajaPrueba("orange")
        self.widgetDos    = CajaPrueba("green")
        self.widgetTres   = CajaPrueba("blue")
        self.widgetCuatro = CajaPrueba("aqua")
        self.contenedorSuperior.addWidget(self.widgetUno)
        self.contenedorSuperior.addWidget(self.widgetDos)
        self.contenedorSuperior.addWidget(self.widgetTres)
        self.contenedorInferior.addWidget(self.widgetCuatro)
        self.contenedorVertical.addLayout(self.contenedorSuperior)
        self.contenedorVertical.addLayout(self.contenedorInferior)
        self.setLayout(self.contenedorVertical)


# ************************************************************************************
# ******************************    Widget Principal    ******************************
# ************************************************************************************

class WidgetPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.cliente             = Cliente()
        self.clienteVector       = [self.cliente]
        self.contenedorPrincipal = QVBoxLayout()
        self.contenedorPestanias = QTabWidget()
        self.NuevoTrabajo        = WidgetNuevoTrabajo(self.clienteVector[0])
        self.ConsultaClientes    = WidgetConsultaClientes(self.clienteVector[0])
        self.ConsultaTrabajos    = WidgetConsultaTrabajos()
        self.Inventarios         = WidgetInventarios()
        self.Recibos             = WidgetRecibos()        
        self.contenedorPestanias.addTab(self.NuevoTrabajo, "Nuevo Trabajo")
        self.contenedorPestanias.addTab(self.ConsultaClientes, "Consulta Clientes")
        self.contenedorPestanias.addTab(self.ConsultaTrabajos, "Consulta Trabajos")
        self.contenedorPestanias.addTab(self.Inventarios, "Inventarios")
        self.contenedorPestanias.addTab(self.Recibos, "Recibos")
        self.contenedorPestanias.setMovable(True)
        self.contenedorPrincipal.addWidget(self.contenedorPestanias)
        self.setLayout(self.contenedorPrincipal)


class EditorQSS(QWidget):
    def __init__(self, padre):
        super().__init__()
        self.padre = padre
        self.resize(480, 320)
        self.setWindowTitle("Editor QSS")
        self.editor = QPlainTextEdit()
        self.editor.setStyleSheet(
            """background-color: #212121; 
               color: #e9e9e9; 
               font-family: Consolas; 
               font-size: 16px; """
               )
        self.editor.setFont("Consolas")
        self.editor.textChanged.connect(self.actualizarEstilos)
        contenedor = QVBoxLayout()
        contenedor.addWidget(self.editor)
        self.setLayout(contenedor)
        self.show()

    def actualizarEstilos(self):
        qss = self.editor.toPlainText()
        try:
            self.padre.setStyleSheet(qss)
        except:
            pass


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle("Taller Mecanico")
        self.widgetPrincipal = WidgetPrincipal()        
        self.setCentralWidget(self.widgetPrincipal)
        # self.editorQSS = EditorQSS(self)
        self.cargarQSS()
        self.ConstruirMenu()

    def cargarQSS(self):
        fichero = "{}\\Estilos.qss".format(os.getcwd())
        try:
            with open(fichero) as styles:
                self.setStyleSheet(styles.read())
        except:
            print("Error al intentar leer \n\t {}".format(fichero))

    def ConstruirMenu(self):
        menu              = self.menuBar()
        # menuConfiguracion = menu.addMenu("&Configuración")
        menuAyuda         = menu.addMenu("A&yuda")
        # menuConfiguracion.addAction("Cambiar Base de Datos")        
        licencia = QAction("Licencia", self)
        version  = QAction("Versión", self)
        licencia.triggered.connect(self.verLicencia)
        version.triggered.connect(self.verVersion)
        menuAyuda.addAction(licencia)
        menuAyuda.addAction(version)

    def verLicencia(self):
        ventana = CuadroMostrarTexto(LICENCIA, "Licencia", 720, 400)
        ventana.exec_()

    def verVersion(self):
        mensaje = "\n\tTALLER MECÁNICO\n  _______________________________________________  \n\n\t        Version    0"
        ventana = CuadroMostrarTexto(mensaje, "Version", 280, 160)
        ventana.exec_()