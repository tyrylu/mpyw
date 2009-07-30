# -- coding: UTF-8 --
import re
import wx
import utils
import versioninfo
import uievents.searchdialog
import  os
info = versioninfo.info()
import globals
aboutInfo=u"koukavé označení {0.name}, skutečné jméno {0.longName}, verze {0.version}. Jako popis je uvedeno {0.description}, k čemuž dodáváme, že url {0.url}. Licenční a copirightové texty vemte prosím následující: {0.copyrightInfo}".format(info)
wildcard = u"Python soubory (*.py)|*.py|python soubory bez konzolových oken (*.pyw)|*.pyw|Textové soubory (*.txt)|*.txt|všechny druhy souborů (*.*)|*.*"
def speak_read_all(EVT):
	utils.speak(globals.policko.Value)
def speak_read_to_end(evt):
	utils.speak(globals.policko.GetRange(globals.policko.InsertionPoint, globals.policko.LastPosition))
def exit(evt):
	utils.promptsave()
	utils.speak(u"Nashledanou uživateli se jménem {0}. Doufám, že se ještě shledáme.".format(wx.GetUserName()))	
	globals.app.ExitMainLoop()

def file_open(evt):
	utils.promptsave()
	path = wx.FileSelector(u"Zvolte si soubor k otevření", wildcard=wildcard, flags=wx.OPEN + wx.FD_FILE_MUST_EXIST, parent=globals.frame)
	if  path != "":
		globals.policko.Clear()
		globals.filename = path
		fd = open(path, "r")
		globals.policko.Value = fd.read()
		fd.close()
		utils.update_window_title()
def file_save_as(evt):
	path = wx.FileSelector(u"Zvolte jméno, pod kterým bude soubor uložen", wildcard=wildcard, flags=wx.SAVE, parent=globals.frame).encode("windows-1250")
	globals.policko.SaveFile(path)
	globals.filename = path

def file_save(evt):
	if globals.filename == "":
		file_save_as(evt)
	elif globals.policko.IsModified() and globals.filename != "":
		globals.policko.SaveFile(globals.filename)            
def help_about(EVT):
	wx.MessageBox(aboutInfo, u"O programu", wx.ICON_INFORMATION)
def help_help(EVT):
	wx.MessageBox(u"Pokud teď čekáte hromadu pokynů, jste na špatném místě. Ale kdyby jste přeci jen něco chtěli skusit najít, tak na http://mpyw.googlecode.com možná něco najdete.", "pokyny", wx.ICON_INFORMATION)                                
def edit_copy(EVT):
	globals.policko.Copy()
def edit_cut(evt):
	globals.policko.Cut()
def edit_paste(evt):
	globals.policko.Paste()
def file_new(evt):
	utils.promptsave()
	globals.filename = ""
	globals.policko.Clear()
	utils.update_window_title()

def edit_go_to_line(evt):
	radek = wx.GetNumberFromUser(u"Vložte číslo řádku, na který chcete přejít.", u"číslo řádku", u"přejít na řádek", 1, parent=globals.frame, min=1, max=globals.policko.NumberOfLines)
	pos = globals.policko.XYToPosition(0, radek - 1)
	globals.policko.InsertionPoint = pos

def edit_search(evt):
	globals.search_dialog = globals.file.LoadDialog(globals.frame, "searchdialog")
	globals.search_dialog.FindWindowByName("find").Bind(wx.EVT_BUTTON, uievents.searchdialog.search_ok)
	globals.search_dialog.FindWindowByName("cancel").Bind(wx.EVT_BUTTON, lambda evt: globals.search_dialog.Hide())
	globals.search_dialog.ShowModal()

def speak_indent(evt):
	line = globals.policko.PositionToXY(globals.policko.InsertionPoint)[1]
	text = globals.policko.GetLineText(line)
	utils.speak(u"Úroveň {0}".format(utils.get_indent_level(text)))

def edit_increase_indent(evt):
	start = globals.policko.Selection[0]
	end = globals.policko.Selection[1]
	if start == end:
		lineno = globals.policko.PositionToXY(globals.policko.InsertionPoint)[1]
		
		start = globals.policko.XYToPosition(0, lineno)
		len = globals.policko.GetLineLength(lineno)
		end = start + len
	text = globals.policko.GetRange(start, end)
	text = re.sub("^", globals.conf["indent"]["unit"], text, re.M + re.U)
	globals.policko.Replace(start, end, text)
	utils.speak(u"Úroveň {0}".format(utils.get_indent_level(text)))

def edit_decrease_indent(evt):
	start = globals.policko.Selection[0]
	end = globals.policko.Selection[1]
	if start == end:
		lineno = globals.policko.PositionToXY(globals.policko.InsertionPoint)[1]
		
		start = globals.policko.XYToPosition(0, lineno)
		len = globals.policko.GetLineLength(lineno)
		end = start + len
	text = globals.policko.GetRange(start, end)
	text = re.sub("^%s"%globals.conf["indent"]["unit"], "", text, re.M + re.U)
	globals.policko.Replace(start, end, text)
	utils.speak(u"Úroveň {0}".format(utils.get_indent_level(text)))

def edit_select_all(evt):
	globals.policko.SelectAll()

def edit_undo(evt):
	globals.policko.Undo()

def edit_redo(evt):
	globals.policko.Redo()