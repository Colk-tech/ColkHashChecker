# (C) 2020 Colk All rights reserved.

import sys
import os
import time

# pipのライブラリ
import tkinter
from tkinter import ttk
import tkinter.filedialog

# 自作ライブラリ
from filhas import *

# globalで使う変数を定めておく
algorithms = ["MD5","sha256","sha512"]


def fileDialog():
    global filePath
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filePath = tkinter.filedialog.askopenfilename(
        filetypes=fTyp, initialdir=iDir)

# 計算するときに呼び出されるやつ
def calculate(progressPage,resultPage):
    input()
    progressPage.tkraise()
    resultPage.tkraise()

def main():

    # 変数定義
    global algorithms

    # -----------------------------------rootのwindow--------------------------------- #


    # rootの設定
    window = tkinter.Tk()
    window.title("ColkHashChecker")
    window.geometry("460x335")
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)


    # -----------------------------------startPage--------------------------------- #


    # startPageのFrameを生成
    startPage = tkinter.Frame(window)

    # タイトルのラベルを設定
    titleLabel = ttk.Label(startPage,
                           text = "ColkHashChecker", font=("Meiryo UI", 32, "bold"))

    # 説明文のラベルを設定
    description = ttk.Label(startPage,
                            text = "Please select your desire algorithm to calculate.")

    # アルゴリズム選択のラジオボタンの設定
    selectedAlgorithm = tkinter.IntVar()
    # 一番上のラジオボタンを選択しておく
    selectedAlgorithm.set(0)
    # 実際のオブジェクト
    algorithmButtons = [tkinter.Radiobutton(startPage, value=index, variable=selectedAlgorithm, text=algorithms[index])
                        for index in range(len(algorithms))]

    # 画面推移用のボタンの設定
    nextButton = ttk.Button(startPage, text="Next",
                            command=lambda: contentsPage.tkraise())

    ######################### startPageのコンポーネントを配置する #########################

    # 空白
    tkinter.Label(startPage, text="").pack()

    # タイトルラベルを配置する
    titleLabel.pack()

    # 空白
    tkinter.Label(startPage, text="").pack()

    # 説明文を配置する
    description.pack()

    # 空白
    tkinter.Label(startPage, text="").pack()

    # アルゴリズムのラジオボタンを配置する
    for index in range(len(algorithmButtons)):
        algorithmButtons[index].pack()

    # 空白
    tkinter.Label(startPage, text="").pack()

    # 次へボタンを配置する
    nextButton.pack()

    # StartPageを配置する
    startPage.grid(row=0, column=0, sticky="nsew")


    # -----------------------------------contentsPage--------------------------------- #


    # contentsPageのFrameを生成
    contentsPage = tkinter.Frame(window)

    # 選択の催促文を設定する
    chooseLabel = ttk.Label(contentsPage,
                            text = "Please select the folder you want us to calculate.")

    # クリックでファイルを選択ボタンを設定する
    fileSelect = ttk.Button(contentsPage, text="Select",
                            command=lambda: fileDialog())

    #ファイルパスを表示するラベルを設定
    # 表示する変数を定義、あとからこれを更新してやれば表示が変わる
    filePathStr = tkinter.StringVar()
    filePathStr.set("None is selected")
    filePathLabel = ttk.Label(contentsPage, textvariable=filePathStr)

    # ユーザーが持っているhashを入力するboxを設定
    hashBox = tkinter.Entry(contentsPage, width=50)
    hashBox.insert(tkinter.END, "Please enter your hash")

    # 「次へ」ボタンを設定
    progressButton = ttk.Button(contentsPage, text="Next",
                                command = lambda: calculate(progressPage,resultPage))


    ######################### contentsPageのコンポーネントを配置する #########################

    # 空白
    for n in range(3):
        tkinter.Label(contentsPage, text="").pack()

    # 催促の文を配置
    chooseLabel.pack()

    # 空白
    for n in range(3):
        tkinter.Label(contentsPage, text="").pack()

    # ファイルセレクトのボタンを設置
    fileSelect.pack()

    # 空白
    for n in range(3):
        tkinter.Label(contentsPage, text="").pack()

    # 選択したファイルのパスを表示するラベルを配置
    filePathLabel.pack()

    # 空白
    for n in range(3):
        tkinter.Label(contentsPage, text="").pack()

    # 「次へ」ボタンを配置
    progressButton.pack()

    # contentsPageを配置する
    contentsPage.grid(row=0, column=0, sticky="nsew")


    # -----------------------------------progressPage--------------------------------- #

    # progressPageのFrameを生成
    progressPage = tkinter.Frame(window)

    # 計算中ラベルの設定
    nowProcessingLabel = ttk.Label(progressPage,
                                   text = "Now calculating...", font=("Meiryo UI", 16, "bold"))

    # しばらくお待ち下さいラベルの設定
    plzWaitLabel = ttk.Label(progressPage,
                             text = "Please wait...", font=("Meiryo UI", 16, "bold"))

    ######################### progressPageのコンポーネントを配置する #########################
    # 空白
    for n in range(3):
        tkinter.Label(progressPage, text="").pack()

    # 計算中ラベルの配置
    nowProcessingLabel.pack()

    # しばらくお待ち下さいラベルの配置
    plzWaitLabel.pack()

    # progressPageを配置する
    progressPage.grid(row=0, column=0, sticky="nsew")


    # -----------------------------------resultPage--------------------------------- #


    # contentsPageのFrameを生成
    resultPage = tkinter.Frame(window)

    # 計算完了ラベルの設定
    finishMessageLabel = ttk.Label(resultPage,
                                   text = "Calculated!", font = ("Meiryo UI", 16, "bold"))

    # 計算されたファイルハッシュを表示するラベルの設定
    calculatedText = tkinter.StringVar()
    calculatedText.set("Calculated file hash:")
    calculatedHashLabel = ttk.Label(resultPage,
                                    textvariable = calculatedText)

    #ユーザーから入力されたハッシュを表示するラベルの設定
    userHashText = tkinter.StringVar()
    userHashText.set("Entered file hash:")
    userHashLabel = ttk.Label(resultPage,
                              textvariable = userHashText)

    # 照合結果を表示してくれるラベルの設定
    resultText = tkinter.StringVar()
    resultText.set("")
    resultLabel = ttk.Label(resultPage,
                            textvariable = resultText)

    ######################### contentsPageのコンポーネントを配置する #########################

    # 空白
    for n in range(3):
        tkinter.Label(resultPage, text="").pack()

    # 計算完了ラベルを配置
    calculatedHashLabel.pack()

    # 入力されたハッシュを表示するラベルを配置
    userHashLabel.pack()

    # 照合結果を表示してくれるラベルを配置
    resultLabel.pack()

    # resultPageを配置する
    resultPage.grid(row=0, column=0, sticky="nsew")


    ###DO NOT CHANGE HERE###
    startPage.tkraise()
    window.mainloop()
    ########################


if __name__ == "__main__":
    main()