# -- coding: UTF-8 --
import re
import wx
import utils
import versioninfo
import uievents.searchdialog
import  os
info = versioninfo.info()
import appenv
aboutInfo=u"koukavé označení {0.name}, skutečné jméno {0.longName}, verze {0.version}. Jako popis je uvedeno {0.description}, k čemuž dodáváme, že url {0.url}. Licenční a copirightové texty vemte prosím následující: {0.copyrightInfo}".format(info)
wildcard = u"Python soubory (*.py)|*.py|python soubory bez konzolových oken (*.pyw)|*.pyw|Textové soubory (*.txt)|*.txt|všechny druhy souborů (*.*)|*.*"
def speak_read_all(EVT):
	utils.speak(appenv.policko.Value)
def speak_read_to_end(evt):
	utils.speak(appenv.policko.GetRange(appenv.policko.InsertionPoint, appenv.policko.LastPosition))
def exit(evt):
	utils.promptsave()
	utils.speak(u"Nashledanou uživateli se jménem {0}. Doufám, že se ještě shledáme.".format(wx.GetUserName()))	
	appenv.app.ExitMainLoop()

def file_open(evt):
	utils.promptsave()
	path = wx.FileSelector(u"Zvolte si soubor k otevření", wildcard=wildcard, flags=wx.OPEN + wx.FD_FILE_MUST_EXIST, parent=appenv.frame)
	if  path != "":
		appenv.policko.Clear()
		appenv.filename = path
		fd = open(path, "r")
		appenv.policko.Value = fd.read()
		fd.close()
		utils.update_window_title()
def file_save_as(evt):
	path = wx.FileSelector(u"Zvolte jméno, pod kterým bude soubor uložen", wildcard=wildcard, flags=wx.SAVE, parent=appenv.frame).encode("windows-1250")
	appenv.policko.SaveFile(path)
	appenv.filename = path

def file_save(evt):
	if appenv.filename == "":
		file_save_as(evt)
	elif appenv.policko.IsModified() and appenv.filename != "":
		appenv.policko.SaveFile(appenv.filename)            
def help_about(EVT):
	wx.MessageBox(aboutInfo, u"O programu", wx.ICON_INFORMATION)
def help_help(EVT):
	wx.MessageBox(u"Pokud teď čekáte hromadu pokynů, jste na špatném místě. Ale kdyby jste přeci jen něco chtěli skusit najít, tak na http://mpyw.googlecode.com možná něco najdete.", "pokyny", wx.ICON_INFORMATION)                                
def edit_copy(EVT):
	appenv.policko.Copy()
def edit_cut(evt):
	appenv.policko.Cut()
def edit_paste(evt):
	appenv.policko.Paste()
def file_new(evt):
	utils.promptsave()
	appenv.filename = ""
	appenv.policko.Clear()
	utils.update_window_title()

def edit_go_to_line(evt):
	radek = wx.GetNumberFromUser(u"Vložte číslo řádku, na který chcete přejít.", u"číslo řádku", u"přejít na řádek", 1, parent=appenv.frame, min=1, max=appenv.policko.NumberOfLines)
	pos = appenv.policko.XYToPosition(0, radek - 1)
	appenv.policko.InsertionPoint = pos

def edit_search(evt):
	appenv.search_dialog = appenv.file.LoadDialog(appenv.frame, "searchdialog")
	appenv.search_dialog.FindWindowByName("find").Bind(wx.EVT_BUTTON, uievents.searchdialog.search_ok)
	appenv.search_dialog.FindWindowByName("cancel").Bind(wx.EVT_BUTTON, lambda evt: appenv.search_dialog.Hide())
	appenv.search_dialog.ShowModal()

def speak_indent(evt):
	line = appenv.policko.PositionToXY(appenv.policko.InsertionPoint)[1]
	text = appenv.policko.GetLineText(line)
	utils.speak(u"Úroveň {0}".format(utils.get_indent_level(text)))

def edit_increase_indent(evt):
	expr = re.compile("^", re.U + re.M)
	start = appenv.policko.Selection[0]
	end = appenv.policko.Selection[1]
	if start == end:
		#Some selection, indent in it
		lineno = appenv.policko.PositionToXY(appenv.policko.InsertionPoint)[1]
		start = appenv.policko.XYToPosition(0, lineno)
		len = appenv.policko.GetLineLength(lineno)
		end = start + len
	text = appenv.policko.GetRange(start, end)
	text = expr.sub(appenv.conf["indent"]["unit"], text)
	appenv.policko.Replace(start, end, text)
	utils.speak(u"Úroveň {0}".format(utils.get_indent_level(text)))

def edit_decrease_indent(evt):
	expr = re.compile("^%s"%appenv.conf["indent"]["unit"], re.U + re.M)
	start = appenv.policko.Selection[0]
	end = appenv.policko.Selection[1]
	if start == end:
		lineno = appenv.policko.PositionToXY(appenv.policko.InsertionPoint)[1]
		start = appenv.policko.XYToPosition(0, lineno)
		len = appenv.policko.GetLineLength(lineno)
		end = start + len
	text = appenv.policko.GetRange(start, end)
	text = expr.sub("", text)
	appenv.policko.Replace(start, end, text)
	utils.speak(u"Úroveň {0}".format(utils.get_indent_level(text)))

def edit_select_all(evt):
	appenv.policko.SelectAll()

def edit_undo(evt):
	appenv.policko.Undo()

def edit_redo(evt):
	appenv.policko.Redo()