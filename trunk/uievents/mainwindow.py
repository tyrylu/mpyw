# -- coding: UTF-8 --
import appenv
def main_focused(EVT):
 appenv.policko.SetFocus()
def updatestatusbar(evt):
	#Kvůli otravnému chování událostí klávesnice, musí se ošetřovat stisk alt a f10 jinak...
	sloupec, radek = appenv.policko.PositionToXY(appenv.policko.InsertionPoint)
	appenv.stav.StatusText = u"Řádek {0}, sloupec {1}".format(radek + 1, sloupec + 1)
	appenv.searchitem.Enable(len(appenv.policko.Value) != 0)
	evt.Skip()
