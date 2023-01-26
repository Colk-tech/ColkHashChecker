# Reference : https://sites.google.com/site/pythoncasestudy/home/tkinterdedrag-drop-ctypes-shi-yong

import sys
import tkinter
import ctypes
from ctypes.wintypes import HWND, UINT, WPARAM, LPARAM

prototype = ctypes.WINFUNCTYPE(ctypes.c_long, HWND, UINT, WPARAM, LPARAM)
WM_DROPFILES = 0x0233
GWL_WNDPROC = -4
WINPROC = None


def py_drop_func(hwnd, msg, wp, lp):
    """
    WinProcのプロトタイプ
    ファイルのドラッグアンドドロップイベント(WM_DROPFILES)を検出して、
    ドロップされたファイルを保存する。
    ここでウィンドウ(tk)を使用するとハングアップするのでデータ保存だけ行う。
    """
    if msg == WM_DROPFILES:
        ctypes.windll.shell32.DragQueryFile(wp, -1, None, None)
        szFile = ctypes.c_buffer(260)
        ctypes.windll.shell32.DragQueryFile(wp, 0, szFile, ctypes.sizeof(szFile))
        dropname = szFile.value.decode(sys.getfilesystemencoding())
        ctypes.windll.shell32.DragFinish(wp)
        print(dropname)

    return ctypes.windll.user32.CallWindowProcW(WINPROC, hwnd, msg, wp, lp)


def dropfile():
    if dropname is not None:
        print(dropname)
    app.after(1000, dropfile)


if __name__ == "__main__":
    dropname = None
    app = tkinter.Tk()

    # === ドラッグアンドドロップイベントを取得させるようにする。===
    # ハンドラの取得
    hwnd = app.winfo_id()
    # ウィンドウがドラッグアンドドロップを認識できるようにする。
    ctypes.windll.shell32.DragAcceptFiles(hwnd, True)
    # ウィンドウプロシージャを取得
    WINPROC = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_WNDPROC)
    # ドラッグアンドドロップを処理できるウィンドウプロシージャを作成
    drop_func = prototype(py_drop_func)
    # ウィンドウプロシージャを追加
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_WNDPROC, drop_func)

    app.after(1000, dropfile)

    app.mainloop()