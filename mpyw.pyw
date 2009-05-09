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
eventhandlers.mymenubar = mymenubar

frame.Maximize()
frame.Bind(wx.EVT_ACTIVATE, eventhandlers.prinacteni)
frame.Bind(wx.EVT_MENU, eventhandlers.newfilerequest, id=149)
frame.Bind(wx.EVT_MENU, eventhandlers.printrequest, id=150)
frame.Bind(wx.EVT_MENU, eventhandlers.openrequest, id=151)
frame.Bind(wx.EVT_MENU, eventhandlers.saverequest, id=153)
frame.Bind(wx.EVT_MENU, eventhandlers.saveasrequest, id=152)
frame.Bind(wx.EVT_MENU, eventhandlers.exit, id=200)
frame.Bind(wx.EVT_MENU, eventhandlers.vyjmout, id=10)
frame.Bind(wx.EVT_MENU, eventhandlers.vlozit, id=12)
frame.Bind(wx.EVT_MENU, eventhandlers.kopirovat, id=11)
frame.Bind(wx.EVT_MENU, eventhandlers.vlozit, id=12)
frame.Bind(wx.EVT_MENU, eventhandlers.gotoline, id=13)
frame.Bind(wx.EVT_MENU, eventhandlers.readalltext, id=205)
frame.Bind(wx.EVT_MENU, eventhandlers.readtoend, id=206)
frame.Bind(wx.EVT_MENU, eventhandlers.aboutrequest, id=102)
frame.Bind(wx.EVT_MENU, eventhandlers.helprequest, id=112)
frame.Bind(wx.EVT_CLOSE, eventhandlers.exit)
policko.Bind(wx.EVT_KEY_UP, eventhandlers.updatestatusbar)
# zobrazíme hlavní okno
frame.Show()
app.MainLoop()