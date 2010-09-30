# -- coding: UTF-8 --
import wx
from wx import xrc
import appenv

def prepare_controls():
  appenv.file = xrc.XmlResource("window.xrc")
  # Načtení hlavního okénečka
  appenv.frame = appenv.file.LoadFrame(None, "myframe")
  # Vytvoření wx objektů(kvůli přístupu k vlastnostem, nebo kvůli navázání událostí)) 
  appenv.policko = xrc.XRCCTRL(appenv.frame, "policko")
  appenv.stav = xrc.XRCCTRL(appenv.frame, "stav")
  appenv.stav.StatusText  =u"Řádek 1 sloupec 1"
  # vytvoření menu
  appenv.searchitem = appenv.frame.MenuBar.FindItemById(xrc.XRCID("search"))
  