# -- coding: UTF-8 --
import re
import os.path


import wx

import uievents.mainmenu
import globals
if globals.conf["speech"].as_bool("allowed"):
	import comtypes.client
	sapi = comtypes.client.CreateObject("SAPI.SPvoice")

def speak(text):
	try:
		sapi.speak(text)
	except NameError:
		pass
def find(what, where, case):
	if  not case:
		where = where.lower()
		what = what.lower()
	try:
		return where.index(what)
	except ValueError:
		return -1
def find_by_regex(regex, text, case):
	try:
		if case:
			reg = re.compile(regex, re.U)
		else:
			reg = re.compile(regex, re.I + re.U)
	except re.error:
			return -2
	res = reg.search(text)
	return res.start() or -1
def get_indent_level(text):
	char = globals.conf["indent"]["unit"]
	char = eval("\"%s\"\n"%char)
	charlen = len(char)
	levels = 0
	while text.startswith(char):
		levels += 1
		if len(text) == charlen:
			text = ""
		else:
			text = text[charlen:]
	return levels
def promptsave():
	if globals.policko.IsModified():
		savestate = wx.MessageBox(u"Text souboru {0} se zmÄ›nil. UloĹľit zmÄ›ny?".format(globals.filename), u"ZmÄ›na souboru {0}".format(os.path.basename(globals.filename)), wx.YES_NO + wx.ICON_QUESTION, globals.frame)
		if savestate == wx.ID_YES:
			uievents.mainmenu.on_file_save(evt)

def update_window_title():
	globals.frame.Title = "mpyw - {0}".format(globals.filename)
