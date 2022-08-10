# -*- coding: UTF-8 -*-
import wx
import GameMenu
import HangmanMain


class StartsGame(GameMenu.Menu):
    def __init__(self, parent):
        GameMenu.Menu.__init__(self, parent)

    def gameStart(self, event):
        class App2(wx.App):
            def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
                super().__init__(redirect, filename, useBestVisual, clearSigInt)
                self.frame2 = HangmanMain.gameFrame(None)
                self.frame2.Show()

        app2 = App2()
        app2.MainLoop()


class App1(wx.App):
    def OnInit(self):
        self.frame1 = StartsGame(None)
        self.frame1.Show(True)
        return True


app1 = App1()
app1.MainLoop()
