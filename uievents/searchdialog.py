# -- coding: UTF-8 --
import wx
import utils
import globals
def search_ok(evt):
	text = globals.search_dialog.FindWindowByName("what").Value
	if text == "":
		wx.MessageBox(u"Nelze vyhledávat, nebylo specifikováno hledané.", u"Nelze pokračovat", wx.ICON_ERROR, globals.search_dialog)
	else:
		if globals.search_dialog.FindWindowByName("re").Value:
			pos = utils.find_by_regex(text, globals.policko.Value, globals.search_dialog.FindWindowByName("case").Value)
		else:
			pos = utils.find(text, globals.policko.Value, globals.search_dialog.FindWindowByName("case").Value)
		if pos >= 0:
			globals.policko.InsertionPoint = pos
			globals.search_dialog.Hide()
		elif pos == -1:
			wx.MessageBox(u"Hledaný text nebyl nalezen.", u"Nenalezeno", wx.ICON_ERROR, globals.search_dialog)
		elif pos == -2:
			wx.MessageDialog(u"Vložený regulární výraz není syntakticky správný.", u"Neplatný regulární výraz", wx.ICON_ERROR, globals.search_dialog)
