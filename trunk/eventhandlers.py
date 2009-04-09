# -- coding: UTF-8 --
import wx
import comtypes.client
import versioninfo
import  os
import win32gui
sapi = comtypes.client.CreateObject("SAPI.SPvoice")
info = versioninfo.info()
aboutInfo=u"kódové označení {0.name}, skutečné jméno {0.longName}, verze {0.version}. Jako popis je uvedeno {0.description}, k čemuž dodáváme, že url {0.url}. Licenční a copirightové texty vemte prosím následující: {0.copyrightInfo}".format(info)
wildcard = u"Python soubory (*.py)|*.py|"     \
           u"kompilované soubory (*.pyc)|*.pyc|" \
           u"všechny soubory (*.*)|*.*"

def readalltext(EVT):
	global sapi, policko
	sapi.speak(policko.GetValue())
def readtoend(evt):
	global sapi, policko
	sapi.speak(policko.GetRange(policko.GetInsertionPoint(), policko.GetLastPosition()))
def exit(evt):
	global app, sapi, filename, policko
	if policko.IsModified():
		savestate = win32gui.MessageBox(0, u"Text souboru %s se změnil. Uložit změny?"%filename, u"Změna souboru", 35)
		if savestate == 6:
			saverequest(evt)
			sapi.speak(u"Nashledanou uživateli se jménem %s. Doufám, že se ještě shledáme." % wx.GetUserName())	
			app.ExitMainLoop()
		elif savestate == 7:
			sapi.speak(u"Nashledanou uživateli se jménem %s. Doufám, že se ještě shledáme." % wx.GetUserName())	
			app.ExitMainLoop()
	else:          
		sapi.speak(u"Nashledanou uživateli se jménem %s. Doufám, že se ještě shledáme." % wx.GetUserName())	
		app.ExitMainLoop()
def wintitle():
	global frame, filename
	frame.SetTitle("mtext - %s" % filename)
def openrequest(evt):
	global frame, policko, filename
	if policko.IsModified():
		savestate = win32gui.MessageBox(0, u"Text souboru %s se změnil. Uložit změny?"%filename, u"Změna souboru", 35)
		if savestate == 6:
			saverequest(evt)
			filename = ""
			policko.Clear()
			wintitle()
		elif savestate == 7:
			filename = ""
	dlg = wx.FileDialog(frame,u"Zvolte si soubor k otevření", os.getcwd(), wildcard=wildcard, style=wx.OPEN | wx.CHANGE_DIR| wx.FD_FILE_MUST_EXIST)
	if dlg.ShowModal() == wx.ID_OK:
		path = dlg.GetPath()
		filename = path
		policko.LoadFile(path)
		wintitle()
	dlg.Destroy()
def saveasrequest(evt):
	global frame, policko, filename
	dlg = wx.FileDialog(frame,u"Zvolte jméno, pod kterým bude soubor uložen", os.getcwd(), wildcard=wildcard, style=wx.SAVE)
	if dlg.ShowModal() == wx.ID_OK:
		path = dlg.GetPath()
		policko.SaveFile(path)
		filename = path
		wintitle()
	dlg.Destroy()
def saverequest(evt):
	global policko, filename
	if filename == "":
		saveasrequest(evt)
	elif policko.IsModified() and filename != "":
		policko.SaveFile(filename)      
def printrequest(EVT):
	win32gui.MessageBox(0, u"Funkce je zatím nedostupná, vyčkejte aktualizace.", u"beta", 64)
def aboutrequest(EVT):
	win32gui.MessageBox(0, aboutInfo, u"O programu", 64)
def helprequest(EVT):
	win32gui.MessageBox(0, u"Pokud teď čekáte hromadu pokynů, jste na špatném místě. Pokyny jsou jednoduché: Napište něco do políčka  a stiskněte tlačítko. Určitě příjdete na to, které...", "pokyny", 64)                
def prinacteni(EVT):
 global policko    
 policko.SetFocus()
def kopirovat(EVT):
	global policko    
	policko.Copy()
def vyjmout(evt):
	global policko    
	policko.Cut()
def vlozit(evt):
	global policko
	policko.Paste()
def newfilerequest(evt):
	global filename, policko
	if policko.IsModified():
		savestate = win32gui.MessageBox(0, u"Text souboru %s se změnil. Uložit změny?"%filename, u"Změna souboru", 35)
		if savestate == 6:
			saverequest(evt)
			filename = ""
			policko.Clear()
			wintitle()
		elif savestate == 7:
			filename = ""
			policko.Clear()
			wintitle()
	else:
		filename = ""
		policko.Clear()
		wintitle()
def updatestatusbar(evt):
	#Kvůli otravnému chování událostí klávesnice, musí se ošetřovat stisk alt a f10 jinak...
	sloupec, radek = policko.PositionToXY(policko.GetInsertionPoint())
	stav.SetStatusText(u"Řádek {0}, sloupec {1}".format(radek + 1, sloupec + 1))
	evt.Skip()
def gotoline(evt):
	radek = wx.GetNumberFromUser(u"Vložte číslo řádku, na který chcete přejít.", u"číslo řádku", u"přejít na řádek", 1, parent=frame, min=1, max=policko.GetNumberOfLines())
	pos = policko.XYToPosition(0, radek - 1)
	policko.SetInsertionPoint(pos)