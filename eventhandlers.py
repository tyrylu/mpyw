# -- coding: UTF-8 --
import wx
import utils
import versioninfo
import  os
info = versioninfo.info()
search_dialog = None
aboutInfo=u"koukavé označení {0.name}, skutečné jméno {0.longName}, verze {0.version}. Jako popis je uvedeno {0.description}, k čemuž dodáváme, že url {0.url}. Licenční a copirightové texty vemte prosím následující: {0.copyrightInfo}".format(info)
wildcard = u"Python soubory (*.py)|*.py|python soubory bez konzolových oken (*.pyw)|*.pyw|Textové soubory (*.txt)|*.txt|všechny druhy souborů (*.*)|*.*"

def promptsave():
	if policko.IsModified():
		savestate = wx.MessageBox(u"Text souboru {0} se změnil. Uložit změny?".format(filename), u"Změna souboru {0}".format(os.path.basename(filename)), wx.YES_NO + wx.ICON_QUESTION, frame)
		if savestate == wx.ID_YES:
			saverequest(evt)
	
def readalltext(EVT):
	utils.speak(policko.Value)
def readtoend(evt):
	utils.speak(policko.GetRange(policko.InsertionPoint, policko.LastPosition))
def exit(evt):
	promptsave()
	utils.speak(u"Nashledanou uživateli se jménem {0}. Doufám, že se ještě shledáme.".format(wx.GetUserName()))	
	app.ExitMainLoop()

def wintitle():
	frame.Title = "mpyw - {0}".format(filename)
def openrequest(evt):
	promptsave()
	path = wx.FileSelector(u"Zvolte si soubor k otevření", wildcard=wildcard, flags=wx.OPEN + wx.FD_FILE_MUST_EXIST, parent=frame)
	if  path != "":
		policko.Clear()



		filename = path
		policko.LoadFile(path)

def saveasrequest(evt):
	global filename
	path = wx.FileSelector(u"Zvolte jméno, pod kterým bude soubor uložen", wildcard=wildcard, flags=wx.SAVE, parent=frame).encode("windows-1250")
	policko.SaveFile(path)
	filename = path
	dlg.Destroy()
def saverequest(evt):
	if filename == "":
		saveasrequest(evt)
	elif policko.IsModified() and filename != "":
		policko.SaveFile(filename)      
def printrequest(EVT):
	wx.MessageBox(u"Funkce je zatím nedostupná, vyčkejte aktualizace.", u"alpha", wx.ICON_INFORMATION)
def aboutrequest(EVT):
	wx.MessageBox(aboutInfo, u"O programu", wx.ICON_INFORMATION)
def helprequest(EVT):
	wx.MessageBox(u"Pokud teď čekáte hromadu pokynů, jste na špatném místě. Ale kdyby jste přeci jen něco chtěli skusit najít, tak na http://mpyw.googlecode.com možná něco najdete.", "pokyny", wx.ICON_INFORMATION)                
def prinacteni(EVT):
 global policko    
 policko.SetFocus()
def kopirovat(EVT):
	policko.Copy()
def vyjmout(evt):
	policko.Cut()
def vlozit(evt):
	policko.Paste()
def newfilerequest(evt):
	global filename, policko
	promptsave()
	filename = ""
	policko.Clear()
	wintitle()
def updatestatusbar(evt):
	#Kvůli otravnému chování událostí klávesnice, musí se ošetřovat stisk alt a f10 jinak...
	sloupec, radek = policko.PositionToXY(policko.InsertionPoint)
	stav.StatusText = u"Řádek {0}, sloupec {1}".format(radek + 1, sloupec + 1)
	searchitem.Enable(len(policko.Value) != 0)
	evt.Skip()
def gotoline(evt):
	radek = wx.GetNumberFromUser(u"Vložte číslo řádku, na který chcete přejít.", u"číslo řádku", u"přejít na řádek", 1, parent=frame, min=1, max=policko.NumberOfLines)
	pos = policko.XYToPosition(0, radek - 1)
	policko.InsertionPoint = pos
def perform_search(evt):
	text = search_dialog.FindWindowByName("what").Value
	if text == "":
		wx.MessageBox(u"Nelze vyhledávat, nebylo specifikováno hledané.", u"Nelze pokračovat", wx.ICON_ERROR, search_dialog)
	else:
		if search_dialog.FindWindowByName("re").Value:
			pos = utils.find_by_regex(text, policko.Value, search_dialog.FindWindowByName("case").Value)
		else:
			pos = utils.find(text, policko.Value, search_dialog.FindWindowByName("case").Value)
		if pos >= 0:
			policko.InsertionPoint = pos
			search_dialog.Hide()
		elif pos == -1:
			wx.MessageBox(u"Hledaný text nebyl nalezen.", u"Nenalezeno", wx.ICON_ERROR, search_dialog)
		elif pos == -2:
			wx.MessageDialog(u"Vložený regulární výraz není syntakticky správný.", u"Neplatný regulární výraz", wx.ICON_ERROR, search_dialog)
def startsearch(evt):
	global search_dialog
	search_dialog = file.LoadDialog(frame, "searchdialog")
	search_dialog.FindWindowByName("find").Bind(wx.EVT_BUTTON, perform_search)
	search_dialog.FindWindowByName("cancel").Bind(wx.EVT_BUTTON, lambda evt: search_dialog.Hide())
	search_dialog.ShowModal()