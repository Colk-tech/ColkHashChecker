# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.filedialog
import os
import tkinter.messagebox
from hashcalc import mainCalc
from tkinter import ttk

filePath = ""
algorithmNames = ["md5", "sha256", "sha512"]
intAlgorithm = 0


def changePage(page):
    page.tkraise()


def fileDialog(FP):
    global filePath
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filePath = tkinter.filedialog.askopenfilename(
        filetypes=fTyp, initialdir=iDir)
    labelChanger(FP, str(filePath))


def labelChanger(strObj, changeText):
    strObj.set(str(changeText))


def callCalc(page, EditBox, selectedAlgorithm):
    global filePath, usrHash, intAlgorithm, progressDiscriberText, calcuatedHashText, usrInputHashText, usrInputHashText
    global resultLabel, C_errorCode, C_hash, C_checker, C_errormsg, contentsPage, calcMsgText, resultText
    changePage(page)
    intAlgorithm = int(selectedAlgorithm.get())
    usrHash = str(EditBox.get())
    C_errorCode, C_hash, C_checker, C_errormsg = mainCalc(
        str(filePath), str(usrHash), int(intAlgorithm))
    calcMsgText.set('Calcuated!')
    descriptionLabelChanger(progressDiscriberText,
                            algorithmNames[intAlgorithm])
    calcuatedHashText.set('''Calculated file hash:
    ''' + C_hash)
    usrInputHashText.set('''Entered file hash:
    ''' + usrHash)
    if C_checker:
        resultText.set("Hash is correct.")
    else:
        resultText.set("ERROR!!! Hash is not correct!!!!!")


def descriptionLabelChanger(progressDiscriberText, algName):
    labelChanger(progressDiscriberText,
                 "Calcuating the file hash with " + algName + "...")


def main():
    global filePath
    global resultLabel
    global contentsPage
    window = tk.Tk()
    window.title("ColkHashChecker")
    window.geometry("460x335")

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # -----------------------------------StartPage---------------------------------

    # StartPage用のFrameを生成
    startPage = tk.Frame(window)

    # タイトル表示
    #--- ラベル生成
    # 空白
    spaceLabel1 = [tk.Label(startPage, text="") for column in range(1)]
    spaceLabel2 = [tk.Label(startPage, text="") for column in range(1)]
    spaceLabel3 = [tk.Label(startPage, text="") for column in range(1)]
    spaceLabel4 = [tk.Label(startPage, text="") for column in range(1)]
    # タイトル
    titleLabelFont = ("Meiryo UI", 32, "bold")
    titleLabel = ttk.Label(
        startPage, text="ColkHashChecker", font=titleLabelFont)
    # 説明文
    description = ttk.Label(
        startPage, text="Please select your desire algorithm to calculate.")
    # アルゴリズム
    selectedAlgorithm = tkinter.IntVar()
    selectedAlgorithm.set(0)
    algorithms =\
        [tk.Radiobutton(startPage, value=0, variable=selectedAlgorithm, text="MD5"), tk.Radiobutton(
            startPage, value=1, variable=selectedAlgorithm, text="sha256"), tk.Radiobutton(startPage, value=2, variable=selectedAlgorithm, text="sha512")]

    #--- ラベル配置
    # 空白
    for index in range(1):
        spaceLabel1[index].pack()
    # タイトル
    titleLabel.pack()
    for index in range(1):
        spaceLabel4[index].pack()

    description.pack()

    for index in range(1):
        spaceLabel2[index].pack()

    for index in range(3):
        algorithms[index].pack()

    for index in range(1):
        spaceLabel3[index].pack()

    # ボタン表示
    #---  ボタン生成
    nextButton = ttk.Button(startPage, text="Next",
                            command=lambda: changePage(contentsPage))

    #---  ボタン配置
    # ボタン
    nextButton.pack()

    # StartPageを配置
    startPage.grid(row=0, column=0, sticky="nsew")

    # -----------------------------------ContentsPage---------------------------------
    # ContentsPage用のFrameを生成
    contentsPage = tk.Frame(window)

    # filePathLabelを定義
    FP = tkinter.StringVar()
    FP.set("None is selected.")
    filePathLabel = ttk.Label(contentsPage, textvariable=FP)

    # 空白
    for n in range(3):
        ttk.Label(contentsPage, text="").pack()

    # 選択文
    plzChoose = ttk.Label(
        contentsPage, text="Please select the folder you want us to calculate.")
    plzChoose.pack()

    # 空白
    for n in range(3):
        ttk.Label(contentsPage, text="").pack()

    # ボタン
    fileButton = ttk.Button(contentsPage, text="Select",
                            command=lambda: fileDialog(FP))
    fileButton.pack()

    # 空白
    for n in range(3):
        ttk.Label(contentsPage, text="").pack()

    filePathLabel.pack()

    # 空白
    for n in range(3):
        ttk.Label(contentsPage, text="").pack()

    EditBox = tkinter.Entry(contentsPage, width=50)
    EditBox.insert(tkinter.END, "Please enter your hash")
    EditBox.pack()

    #---  ボタン生成
    global progressDiscriberText
    global calcuatedHashText
    global usrInputHashText
    global resultText
    global calcMsgText
    resultText = tkinter.StringVar()
    progressDiscriberText = tkinter.StringVar()
    progressDiscriberText.set(
        "Calculating the hash with " + algorithmNames[intAlgorithm] + "...")
    calcuatedHashText = tkinter.StringVar()
    usrInputHashText = tkinter.StringVar()
    calcMsgText = tkinter.StringVar()
    calcMsgText.set("Calcuating with " +
                    str(algorithmNames[intAlgorithm]) + "...")

    progressButton = ttk.Button(contentsPage, text="Next", command=lambda: callCalc(
        progressPage, EditBox, selectedAlgorithm))

    #---  ボタン配置
    # ボタン
    progressButton.pack()

    contentsPage.grid(row=0, column=0, sticky="nsew")

    # -----------------------------------ProgressPage---------------------------------
    # progressPage用のFrameを生成
    progressPage = tk.Frame(window)
    filePath = str(FP.get())

    progressLabelFont = ("Meiryo UI", 16, "bold")
    calcuatedHashLabel = ttk.Label(
        progressPage, textvariable=calcuatedHashText)
    usrInputHashLabel = ttk.Label(progressPage, textvariable=usrInputHashText)
    calcMsgLabel = ttk.Label(
        progressPage, textvariable=calcMsgText, font=("Meiryo UI", 16, "bold"))
    resultLabel = ttk.Label(
        progressPage, textvariable=resultText, font=("Meiryo UI", 12, "bold"))

    # 空白
    # ---  ラベル生成
    spaceLabel1 = [tk.Label(progressPage, text="") for column in range(5)]
    # タイトル

    # ---  ラベル配置
    # 空白
    for index in range(5):
        spaceLabel1[index].pack()
    # タイトル
    calcMsgLabel.pack()
    calcuatedHashLabel.pack()
    usrInputHashLabel.pack()
    resultLabel.pack()

    # MainPageを配置
    progressPage.grid(row=0, column=0, sticky="nsew")

    ###DO NOT CHANGE HERE###
    startPage.tkraise()
    window.mainloop()
    ######


if __name__ == "__main__":
    main()
