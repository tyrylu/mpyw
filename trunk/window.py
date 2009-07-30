# -- coding: UTF-8 --
import wx
from wx import xrc
import globals
globals.file = xrc.XmlResource("window.xrc")
# Načtení hlavního okénečka
globals.frame = globals.file.LoadFrame(None, "myframe")
# Vytvoření wx objektů(kvůli přístupu k vlastnostem, nebo kvůli navázání událostí)) 
globals.policko = xrc.XRCCTRL(globals.frame, "policko")
globals.stav = xrc.XRCCTRL(globals.frame, "stav")
globals.stav.StatusText  =u"Řádek 1 sloupec 1"
# vytvoření menu
globals.searchitem = globals.frame.MenuBar.FindItemById(xrc.XRCID("search"))
