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
                           size=wx.Size(405, 148), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer6.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.gameResult = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.gameResult.SetMinSize(wx.Size(300, -1))

        bSizer6.Add(self.gameResult, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.retry = wx.Button(self, wx.ID_ANY, u"再来一次", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.retry, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
