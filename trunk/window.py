# -- coding: UTF-8 --
import wx
from wx import xrc
file = xrc.XmlResource("window.xrc")
# Načtení hlavního okénečka
frame = file.LoadFrame(None, "myframe")
# Vytvoření wx objektů(kvůli přístupu k vlastnostem, nebo kvůli navázání událostí)) 
policko = xrc.XRCCTRL(frame, "policko")
stav = xrc.XRCCTRL(frame, "stav")
stav.StatusText  =u"Řádek 1 sloupec 1"
# vytvoření menu
searchitem = frame.MenuBar.FindItemById(xrc.XRCID("search"))
