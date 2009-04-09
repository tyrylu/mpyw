# -- coding: UTF-8 --
import wx
from wx import xrc
file = xrc.XmlResource("window.xrc")
# Načtení hlavního okénečka
frame = file.LoadFrame(None, "myframe")

# Vytvoření wx objektů(kvůli přístupu k vlastnostem, nebo kvůli navázání událostí)) 
policko = xrc.XRCCTRL(frame, "policko")
stav = xrc.XRCCTRL(frame, "stav")
stav.SetStatusText(u"Řádek 1 sloupec 1")
# vytvoření menu
mymenubar = wx.MenuBar()
menu = wx.Menu()
soubormenu = wx.Menu()
newitem = soubormenu.Append(149, u"nový soubor...\tctrl+n")
openitem = soubormenu.Append(151, u"otevřít...\tctrl+o")
saveitem = soubormenu.Append(153, u"uložit\tctrl+s")
saveasitem = soubormenu.Append(152, u"uložit jako...\tctrl+shift+s")
printitem = soubormenu.Append(150, u"tisk\tctrl+p")
exititem = soubormenu.Append(200, u"konec\tctrl+q")
upravymenu = wx.Menu()
vyjmoutitem = upravymenu.Append(10, u"vyjmout\tctrl+x")
kopirovatitem = upravymenu.Append(11, u"kopírovat\tctrl+c")
vlozititem = upravymenu.Append(12, u"vložit\tctrl+v")
jdinaradekitem = upravymenu.Append(13, u"Přejít na řádek...\tctrl+g")
mluvitmenu = wx.Menu()
prectivseitem = mluvitmenu.Append(205, u"číst celý text\tctrl+shift+r")
prectiodkurzoruitem = mluvitmenu.Append(206, u"Číst od pozice kurzoru\tctrl+r")
helpitem = menu.Append(112, u"něco o používání programu")
aboutitem = menu.Append(102, u"o této skromné aplikaci\tctrl+f1")
mymenubar.Append(soubormenu, u"soubor")
mymenubar.Append(upravymenu, u"úpravy")
mymenubar.Append(mluvitmenu, u"mluvení")
mymenubar.Append(menu, u"Nápověda")
# definujeme, které menu se má ukázat
frame.SetMenuBar(mymenubar)