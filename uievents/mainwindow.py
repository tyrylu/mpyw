# -- coding: UTF-8 --
import globals
def main_focused(EVT):
 globals.policko.SetFocus()
def updatestatusbar(evt):
	#Kvůli otravnému chování událostí klávesnice, musí se ošetřovat stisk alt a f10 jinak...
	sloupec, radek = globals.policko.PositionToXY(globals.policko.InsertionPoint)
	globals.stav.StatusText = u"Řádek {0}, sloupec {1}".format(radek + 1, sloupec + 1)
	globals.searchitem.Enable(len(globals.policko.Value) != 0)
	evt.Skip()
