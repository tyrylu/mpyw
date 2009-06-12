# -- coding: UTF-8 --
# asi milion importů všeho možného...
import wx

app = wx.PySimpleApp()
locale = wx.Locale(wx.LANGUAGE_DEFAULT)
from window import *
import eventhandlers
eventhandlers.app = app
eventhandlers.frame = frame
eventhandlers.policko = policko
eventhandlers.filename = ""
eventhandlers.stav = stav
eventhandlers.searchitem = searchitem
eventhandlers.file = file
frame.Maximize()
frame.Bind(wx.EVT_ACTIVATE, eventhandlers.prinacteni)
frame.Bind(wx.EVT_MENU, eventhandlers.newfilerequest, id=xrc.XRCID("newfile"))
frame.Bind(wx.EVT_MENU, eventhandlers.openrequest, id=xrc.XRCID("openfile"))
frame.Bind(wx.EVT_MENU, eventhandlers.saverequest, id=xrc.XRCID("savefile"))
frame.Bind(wx.EVT_MENU, eventhandlers.saveasrequest, id=xrc.XRCID("saveasfile"))
frame.Bind(wx.EVT_MENU, eventhandlers.exit, id=xrc.XRCID("exit"))
frame.Bind(wx.EVT_MENU, eventhandlers.vyjmout, id=xrc.XRCID("cut"))
frame.Bind(wx.EVT_MENU, eventhandlers.vlozit, id=xrc.XRCID("paste"))
frame.Bind(wx.EVT_MENU, eventhandlers.kopirovat, id=xrc.XRCID("copy"))
frame.Bind(wx.EVT_MENU, eventhandlers.gotoline, id=xrc.XRCID("gotoline"))
frame.Bind(wx.EVT_MENU, eventhandlers.startsearch, id=xrc.XRCID("search"))
frame.Bind(wx.EVT_MENU, eventhandlers.readalltext, id=xrc.XRCID("readall"))
frame.Bind(wx.EVT_MENU, eventhandlers.readtoend, id=xrc.XRCID("read"))
frame.Bind(wx.EVT_MENU, eventhandlers.aboutrequest, id=xrc.XRCID("about"))
frame.Bind(wx.EVT_MENU, eventhandlers.helprequest, id=xrc.XRCID("help"))
frame.Bind(wx.EVT_CLOSE, eventhandlers.exit)
policko.Bind(wx.EVT_KEY_UP, eventhandlers.updatestatusbar)
# zobrazíme hlavní okno
frame.Show()
app.MainLoop()