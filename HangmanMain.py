# -*- coding: UTF-8 -*-

#import wx
import GameWindow
import GameEnd


class gameFrame(GameWindow.GameMain):
    def __init__(self, parent):
        GameWindow.GameMain.__init__(self, parent)
        self.inputText = None
        self.sentence = "welcome to wonderland"
        self.answer = "welcome to wonderland"
        self.right_answer = list(self.answer)
        self.clue = list("*" * len(self.answer))
        self.chances = 10
        self.resultHint = self.__changeHint(" ")
        self.usersInput.SetFocus()
        self.lifes.SetValue(str(self.chances))
        self.outputHint.SetValue(self.resultHint)

    def confirmInput(self, event):
        '''点击确认后发生的事件'''
        self.inputText = self.usersInput.GetValue()
        self.__gameJudge()
        self.lifes.SetValue(str(self.chances))
        self.outputHint.SetValue(self.resultHint)
        self.usersInput.SetFocus()

    def __changeHint(self, enter):
        '''改变提示文本'''
        while self.sentence.find(enter) != -1:
            x = self.sentence.find(enter)
            self.clue[x] = self.right_answer[x]  # 利用列表进行替换
            self.sentence = self.sentence.replace(enter, "*", 1)
        return " ".join(self.clue)

    def __gameJudge(self):
        '''游戏判断：正确和错误，失败和胜利'''
        if self.chances > 1:
            if self.inputText == self.answer:
                GameEnd.gameEnd.openFrame(self)
                GameEnd.gameEnd.gameResult.SetValue("正确答案！游戏胜利！")
            elif len(self.inputText) == 1:
                if self.inputText in self.answer:
                    self.resultHint = self.__changeHint(self.inputText)
                else:
                    self.chances -= 1
            else:
                self.chances -= 1
        else:
            GameEnd.gameEnd.openFrame(self)
            GameEnd.gameEnd.gameResult.SetValue("机会耗尽，游戏失败。")

'''app = wx.App(False)

frame = gameFrame(None)

frame.Show(True)

# start the applications
app.MainLoop()'''
