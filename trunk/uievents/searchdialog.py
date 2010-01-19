# -- coding: UTF-8 --
import wx
import utils
import appenv
def search_ok(evt):
	text = appenv.search_dialog.FindWindowByName("what").Value
	if text == "":
		wx.MessageBox(u"Nelze vyhledávat, nebylo specifikováno hledané.", u"Nelze pokračovat", wx.ICON_ERROR, appenv.search_dialog)
	else:
		if appenv.search_dialog.FindWindowByName("re").Value:
			pos = utils.find_by_regex(text, appenv.policko.Value, appenv.search_dialog.FindWindowByName("case").Value)
		else:
			pos = utils.find(text, appenv.policko.Value, appenv.search_dialog.FindWindowByName("case").Value)
		if pos >= 0:
			appenv.policko.InsertionPoint = pos
			appenv.search_dialog.Hide()
		elif pos == -1:
			wx.MessageBox(u"Hledaný text nebyl nalezen.", u"Nenalezeno", wx.ICON_ERROR, appenv.search_dialog)
		elif pos == -2:
			wx.MessageDialog(u"Vložený regulární výraz není syntakticky správný.", u"Neplatný regulární výraz", wx.ICON_ERROR, appenv.search_dialog)
