from Tkinter import *
from RadioInterface import *
ventana = Tk()
ventana.wm_title("SAGA 1 - Taller de Dise�o")
playList = PlayList()
radioInterface = RadioInterface(ventana, playList)
ventana.mainloop()
