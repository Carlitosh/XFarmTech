#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#https://pythones.net
 
import sys #Importamos módulo sys
from PyQt5 import uic, QtWidgets #Importamos módulo uic y Qtwidgets
 
qtCreatorFile = "windows_principal.ui" # Nuestro archivo UI aquí.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) #El modulo ui carga
 
class XFarmTech(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self): #Constructor de la clase
        QtWidgets.QMainWindow.__init__(self) #Constructor
        Ui_MainWindow.__init__(self) #Constructor
        self.setupUi(self) # Método Constructor de la ventana
		
 

		
if __name__ == "__main__": #Condicional que comprueba si ha sido ejecutado o importado
		#NO importamos el módulo Sys
    app = QtWidgets.QApplication([]) #Creamos app y le pasamos una lista de argumentos vacíos
	#Borramos todo el resto del código y ahora vamos a instanciar nuestra clase MainWindow:
    screen = XFarmTech()
	#Ahora es hora de mostrar esta ventana:
    screen.show() 
	#Aquí creamos el bucle de ejecución
    app.exec_() #Usamos app.exec_() para crear el bucle de ejecución