import os

import tkinter
import tkinter.filedialog


# ファイルダイアログを開くためのやつ
def fileDialog():
    global filePath
    filePath = tkinter.filedialog.askopenfilename(
        filetypes=[("", "*")], initialdir=os.path.abspath(os.path.dirname(__file__)))


# 「ハッシュを計算する」ボタンが押されたときにする処理
def calculate(window,progressPage,resultPage):
    input()
    progressPage.tkraise()
    resultPage.tkraise()


"""
# デバッグ用のページチェンジャー
def debpagechan(resultPage,errResultPage,calculatedText,userHashText,errCalculatedText,errUserHashText):
    if input() == "0":
        calculatedText.set("SUC")
        userHashText.set("SUCUSR")
        resultPage.tkraise()
    else:
        errCalculatedText.set("ERR")
        errUserHashText.set("ERRUSR")
        errResultPage.tkraise()
"""