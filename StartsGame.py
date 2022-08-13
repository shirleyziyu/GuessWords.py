# -*- coding: UTF-8 -*-
import wx
import GameMenu
import HangmanMain


class StartsGame(GameMenu.Menu):
    def __init__(self, parent):
        GameMenu.Menu.__init__(self, parent)

    def gameStart(self, event):
        app.frame2.Show(True)
        app.frame1.Destroy()



class App(wx.App):
    def OnInit(self):
        self.frame1 = StartsGame(None)
        self.frame1.Show(True)
        self.frame2 = HangmanMain.gameFrame(None)
        self.SetTopWindow(self.frame1)
        return True


app = App()
app.MainLoop()
