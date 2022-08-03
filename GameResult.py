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
## Class gameResult
###########################################################################

class gameResult(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(358, 133), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        bSizer8.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.gameResult = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.gameResult, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer8)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
