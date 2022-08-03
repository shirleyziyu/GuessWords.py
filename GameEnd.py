# -*- coding:UTF-8 -*-
import wx
import GameResult


class gameEnd(GameResult.gameResult):
    def __init__(self, parent):
        GameResult.gameResult.__init__(self, parent)

    def openFrame(self):
        app = wx.App(False)
        frame = gameEnd(None)
        frame.Show(True)
        app.MainLoop()