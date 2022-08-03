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
## Class Menu
###########################################################################

class Menu(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Hangman", pos=wx.DefaultPosition, size=wx.Size(415, 236),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.target = wx.StaticText(self, wx.ID_ANY, u"这是一个猜句子的游戏，游戏规则与经典游戏“吊死鬼”相似。", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.target.SetLabelMarkup(u"这是一个猜句子的游戏，游戏规则与经典游戏“吊死鬼”相似。")
        self.target.Wrap(-1)

        self.target.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer2.Add(self.target, 0, wx.ALL, 5)

        self.text2 = wx.StaticText(self, wx.ID_ANY, u"谜底是个有意义的英语句子，全部字母小写，没有句点。", wx.DefaultPosition, wx.DefaultSize, 0)
        self.text2.Wrap(-1)

        bSizer2.Add(self.text2, 0, wx.ALL, 5)

        self.text3 = wx.StaticText(self, wx.ID_ANY,
                                   u"规则：\n1.你可以输入一个字母或你的最终答案。\n2.如果字母存在于句子中，将会在相应位置填写，否则会扣除一条命。\n3.若输入的最终答案与谜底不符，则扣去一条命。\n4.猜出正确句子胜利。生命用完则游戏失败。",
                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.text3.Wrap(-1)

        bSizer2.Add(self.text3, 0, wx.ALL | wx.EXPAND, 5)

        self.startGame = wx.Button(self, wx.ID_ANY, u"开始游戏", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.startGame, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.startGame.Bind(wx.EVT_BUTTON, self.gameStart)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def gameStart(self, event):
        event.Skip()
