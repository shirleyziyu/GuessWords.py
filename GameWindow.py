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
## Class GameMain
###########################################################################

class GameMain(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Hangman", pos=wx.DefaultPosition, size=wx.Size(480, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.hint = wx.StaticText(self, wx.ID_ANY, u"\n请输入单个字母或答案", wx.DefaultPosition, wx.DefaultSize, 0)
        self.hint.Wrap(-1)

        self.hint.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer6.Add(self.hint, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"生命"), wx.VERTICAL)

        self.lifes = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_READONLY)
        self.lifes.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))
        self.lifes.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.lifes.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        sbSizer1.Add(self.lifes, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer6.Add(sbSizer1, 1, wx.EXPAND, 5)

        bSizer2.Add(bSizer6, 1, wx.EXPAND, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"提示"), wx.VERTICAL)

        self.outputHint = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.TE_READONLY)
        sbSizer3.Add(self.outputHint, 0, wx.ALL | wx.EXPAND, 5)

        bSizer2.Add(sbSizer3, 1, wx.EXPAND, 5)

        bSizer81 = wx.BoxSizer(wx.VERTICAL)

        self.usersInput = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer81.Add(self.usersInput, 0, wx.ALL | wx.EXPAND, 5)

        self.retry = wx.Button(self, wx.ID_ANY, u"重开", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer81.Add(self.retry, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.Add(bSizer81, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.usersInput.Bind(wx.EVT_TEXT_ENTER, self.confirmInput)
        self.retry.Bind(wx.EVT_BUTTON, self.Again)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def confirmInput(self, event):
        event.Skip()

    def Again(self, event):
        event.Skip()
