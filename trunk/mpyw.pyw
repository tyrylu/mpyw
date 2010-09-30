# -- coding: UTF-8 --
# asi milion importů všeho možného...
import configobj
import wx
import window
xrc = window.xrc
import appenv
import uievents.mainmenu
import uievents.mainwindow
import utils


class mpywapp(wx.App):
  def OnInit(self):
    appenv.lc = locale = wx.Locale(wx.LANGUAGE_DEFAULT)
    appenv.conf = configobj.ConfigObj("mpyw.ini")
    appenv.filename = ""
    window.prepare_controls()
    utils.init()
    appenv.frame.Maximize()
    appenv.frame.Bind(wx.EVT_ACTIVATE, uievents.mainwindow.main_focused)
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.file_new, id=xrc.XRCID("newfile"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.file_open, id=xrc.XRCID("openfile"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.file_save, id=xrc.XRCID("savefile"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.file_save_as, id=xrc.XRCID("saveasfile"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.exit, id=xrc.XRCID("exit"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_select_all, id=xrc.XRCID("selectall") )
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_undo, id=xrc.XRCID("undo"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_redo, id=xrc.XRCID("redo"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_cut, id=xrc.XRCID("cut"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_paste, id=xrc.XRCID("paste"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_copy, id=xrc.XRCID("copy"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_go_to_line, id=xrc.XRCID("gotoline"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_search, id=xrc.XRCID("search"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_increase_indent, id=xrc.XRCID("increaseindent"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.edit_decrease_indent, id=xrc.XRCID("decreaseindent"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.speak_read_all, id=xrc.XRCID("readall"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.speak_read_to_end, id=xrc.XRCID("read"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.speak_indent, id=xrc.XRCID("sayindentlevel"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.help_about, id=xrc.XRCID("about"))
    appenv.frame.Bind(wx.EVT_MENU, uievents.mainmenu.help_help, id=xrc.XRCID("help"))
    appenv.frame.Bind(wx.EVT_CLOSE, uievents.mainmenu.exit)
    appenv.policko.Bind(wx.EVT_KEY_UP, uievents.mainwindow.updatestatusbar)
    appenv.frame.Show()
    return True

app = mpywapp()
appenv.app = app
if __name__ == "__main__":
  appenv.app.MainLoop()