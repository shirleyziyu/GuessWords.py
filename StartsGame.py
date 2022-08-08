# -*- coding: UTF-8 -*-
import wx
import GameMenu
import HangmanMain


class StartsGame(GameMenu.Menu):
    def __init__(self, parent):
        GameMenu.Menu.__init__(self, parent)

    def gameStart(self, event):
        app2 = wx.App(False)
        frame2 = HangmanMain.gameFrame(None)
        frame2.Show(True)
        app2.MainLoop()


class App1(wx.App):
    def OnInit(self):
        self.frame1 = StartsGame(None)
        self.frame1.Show(True)
        return True


app1 = App1()
app1.MainLoop()
