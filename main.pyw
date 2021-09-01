# Modulos de Qt e importados

from PySide6.QtWidgets import *
from PySide6.QtCore    import *
from PySide6.QtGui     import *
from modulo            import *
from componentes       import *
from time              import sleep
import sys


# Ejecución del Programa

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    aplicacion.setStyle("Fusion")
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(aplicacion.exec_())