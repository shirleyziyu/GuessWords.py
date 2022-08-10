# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class Result
###########################################################################

class Result(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Gameover", pos=wx.DefaultPosition,
                           size=wx.Size(315, 148), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer6.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.gameResult = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer6.Add(self.gameResult, 0, wx.ALL | wx.EXPAND, 5)

        self.retry = wx.Button(self, wx.ID_ANY, u"再来一次", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.retry, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.retry.Bind(wx.EVT_BUTTON, self.Again)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def Again(self, event):
        event.Skip()


if __name__ == "__main__":
    app = wx.App(False)
    frame = Result(None)
    frame.Show(True)
    app.MainLoop()
