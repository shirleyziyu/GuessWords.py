# -*- coding: UTF-8 -*-

import wx
# import GameEnd
import GameWindow
import random

fo = open('sentencelib.txt')
library = fo.readlines()
randomAnswer = random.choice(library)
fo.close()


class gameFrame(GameWindow.GameMain):
    def __init__(self, parent):
        GameWindow.GameMain.__init__(self, parent)
        self.inputText = None
        self.sentence = randomAnswer[0:-1]
        self.answer = randomAnswer[0:-1]
        self.right_answer = list(self.answer)
        self.clue = list("*" * len(self.answer))
        self.chances = 10
        self.resultHint = self.__changeHint(" ")
        self.usersInput.SetFocus()
        self.lifes.SetValue(str(self.chances))
        self.outputHint.SetValue(self.resultHint)

    def confirmInput(self, event):
        '''回车后发生的事件'''
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
                '''game_e = GameEnd.gameEnd(None)
                game_e.openFrame("正确答案！游戏胜利！")
                game_e.gameResult.SetValue("正确答案！游戏胜利！")
                game_e.Show(True)'''
                self.resultHint = "正确答案！游戏胜利！"
                self.Destroy()
            elif len(self.inputText) == 1:
                if self.inputText in self.answer:
                    self.resultHint = self.__changeHint(self.inputText)
                else:
                    self.chances -= 1
            else:
                self.chances -= 1
        else:
            '''game_e = GameEnd.gameEnd(None)
            game_e.openFrame("机会耗尽，游戏失败。")
            game_e.gameResult.SetValue("机会耗尽，游戏失败。")
            game_e.Show(True)'''
            self.resultHint = "机会耗尽，游戏失败。"
            self.Destroy()
            wx.Exit()


if __name__ == "__main__":
    app = wx.App(False)
    frame = gameFrame(None)
    frame.Show(True)
    app.MainLoop()
