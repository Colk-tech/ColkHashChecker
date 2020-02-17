# (C) 2020 Colk All rights reserved.

# いつものライブラリ
import sys
import os

# tkinter関連のライブラリ
import tkinter
from tkinter import ttk
import tkinter.filedialog

# 自作ライブラリ
from filhas import *
from mainlib import *

# globalで使う変数を定めておく
algorithms = ["MD5","sha256","sha512"]
global filePath

def main():

    # 変数定義
    global algorithms
    global filePath

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
                                command = lambda: debpagechan(resultPage,errResultPage,calculatedText,userHashText,errCalculatedText,errUserHashText))
                                #command = lambda: calculate(window,progressPage,resultPage))


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

    # ハッシュが合致した場合のresultPageのFrameを生成
    resultPage = tkinter.Frame(window)

    # 結果表示ラベルの設定
    finishMessageLabel = ttk.Label(resultPage,
                                      text="Calculated!", font=("Meiryo UI", 16, "bold"))

    # 計算されたファイルハッシュを表示するラベルの設定
    calculatedText = tkinter.StringVar()
    calculatedText.set("Calculated file hash:")
    calculatedHashLabel = ttk.Label(resultPage,
                                    textvariable=calculatedText)

    # ユーザーから入力されたハッシュを表示するラベルの設定
    userHashText = tkinter.StringVar()
    userHashText.set("Entered file hash:")
    userHashLabel = ttk.Label(resultPage,
                              textvariable=userHashText)

    ######################### resultPageのコンポーネントを配置する #########################

    # 空白
    for n in range(3):
        tkinter.Label(resultPage, text="").pack()

    # 結果表示ラベルを配置
    finishMessageLabel.pack()

    # 計算されたハッシュを表示するラベルを配置
    calculatedHashLabel.pack()

    # 入力されたハッシュを表示するラベルを配置
    userHashLabel.pack()

    # resultPageを配置する
    resultPage.grid(row=0, column=0, sticky="nsew")



    # -----------------------------------errResultPage--------------------------------- #


    # ハッシュが合致しなかった場合のerrResultPageのFrameを生成
    errResultPage = tkinter.Frame(window)

    # 結果表示ラベルの設定
    errFinishMessageLabel = ttk.Label(errResultPage,
                                   text = "Calculated!", font = ("Meiryo UI", 16, "bold"))

    # 計算されたファイルハッシュを表示するラベルの設定
    errCalculatedText = tkinter.StringVar()
    errCalculatedText.set("Calculated file hash:")
    errCalculatedHashLabel = ttk.Label(errResultPage,
                                    textvariable = calculatedText)

    #ユーザーから入力されたハッシュを表示するラベルの設定
    errUserHashText = tkinter.StringVar()
    errUserHashText.set("Entered file hash:")
    errUserHashLabel = ttk.Label(errResultPage,
                              textvariable = userHashText)

    ######################### errResultPageのコンポーネントを配置する #########################

    # 空白
    for n in range(3):
        tkinter.Label(errResultPage, text="").pack()

    # 結果表示ラベルを配置
    errFinishMessageLabel.pack()

    # 計算されたハッシュを表示するラベルを配置
    errCalculatedHashLabel.pack()

    # 入力されたハッシュを表示するラベルを配置
    errUserHashLabel.pack()

    # errResultPageを配置する
    errResultPage.grid(row=0, column=0, sticky="nsew")


    ###DO NOT CHANGE HERE###
    startPage.tkraise()
    window.mainloop()
    ########################


if __name__ == "__main__":
    main()