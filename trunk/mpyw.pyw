# -- coding: UTF-8 --
# asi milion importů všeho možného...
import configobj
import wx
app = wx.PySimpleApp()
locale = wx.Locale(wx.LANGUAGE_DEFAULT)

from window import xrc

import globals
globals.conf = configobj.ConfigObj("mpyw.ini")
import uievents.mainmenu
import uievents.mainwindow
globals.app = app
globals.filename = ""
globals.frame.Maximize()
globals.frame.Bind(wx.EVT_ACTIVATE, uievents.mainwindow.main_focused)
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.file_new, id=xrc.XRCID("newfile"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.file_open, id=xrc.XRCID("openfile"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.file_save, id=xrc.XRCID("savefile"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.file_save_as, id=xrc.XRCID("saveasfile"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.exit, id=xrc.XRCID("exit"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_select_all, id=xrc.XRCID("selectall") )
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_undo, id=xrc.XRCID("undo"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_redo, id=xrc.XRCID("redo"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_cut, id=xrc.XRCID("cut"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_paste, id=xrc.XRCID("paste"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_copy, id=xrc.XRCID("copy"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_go_to_line, id=xrc.XRCID("gotoline"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_search, id=xrc.XRCID("search"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_increase_indent, id=xrc.XRCID("increaseindent"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_decrease_indent, id=xrc.XRCID("decreaseindent"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.speak_read_all, id=xrc.XRCID("readall"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.speak_read_to_end, id=xrc.XRCID("read"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.speak_indent, id=xrc.XRCID("sayindentlevel"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.help_about, id=xrc.XRCID("about"))
globals.frame.Bind(wx.EVT_MENU, uievents.mainmenu.help_help, id=xrc.XRCID("help"))
globals.frame.Bind(wx.EVT_CLOSE, uievents.mainmenu.exit)
globals.policko.Bind(wx.EVT_KEY_UP, uievents.mainwindow.updatestatusbar)
# zobrazíme hlavní okno
globals.frame.Show()
globals.app.MainLoop()