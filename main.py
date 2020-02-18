import os

# tkinter関連モジュール
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

# 抽象クラス使用
from abc import ABCMeta, abstractmethod

# 自作モジュール
from hashcalc import mainCalc

title = "ColkHashChecker"
algorithmNames = ["md5", "sha256", "sha512"]


class Root:
    def __init__(self):
        # windowの設定
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("460x335")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # 静的なページを先に初期化
        Data.pages = {
            "start" : StartPage(self.window),
            "contents" : ContentsPage(self.window)
        }

        # startページを先に呼び出す
        Data.pages["start"].frame.tkraise()
        self.window.mainloop()


class Page(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _next_page(self):
        pass


class StartPage(Page):
    """
    1版最初のページ
    hashのアルゴリズムを選ぶ場所
    """
    def __init__(self, r: Tk):
        """
        Args:
            r(tk.Tk): tk.Tk()で取得できるwindow
        """
        super().__init__()
        self.frame = Frame(r)

        # タイトルの設定
        title_label_font = ("Meiryo UI", 32, "bold")
        title_label = Label(self.frame, text=title, font=title_label_font)
        description = Label(self.frame, text="Please select your desire algorithm to calculate.")

        # アルゴリズム関連
        self.selected_algorithm = IntVar()
        self.selected_algorithm.set(0)
        select_algorithms_buttons = [
            Radiobutton(self.frame, value=0, variable=self.selected_algorithm, text=algorithmNames[0]),
            Radiobutton(self.frame, value=1, variable=self.selected_algorithm, text=algorithmNames[1]),
            Radiobutton(self.frame, value=2, variable=self.selected_algorithm, text=algorithmNames[2])
        ]

        # 開始ボタン
        start_button = Button(
            self.frame,
            text="Next",
            command=self.start
        )

        # -------- 配置 -------- #
        Utils.space(self.frame, 1)
        title_label.pack()
        Utils.space(self.frame, 1)
        description.pack()
        Utils.space(self.frame, 1)

        # ラジオボタン
        for button in select_algorithms_buttons:
            button.pack()

        Utils.space(self.frame, 1)

        # スタートボタン
        start_button.pack()

        self.frame.grid(row=0, column=0, sticky="nsew")

    def start(self):
        Data.algorithm_index = self.selected_algorithm.get()
        self._next_page()

    def _next_page(self):
        """
        次のページを呼び出す
        """
        Utils.change_page("contents")


class ContentsPage(Page):
    """
    2番目のページ
    ファイルをロードしてhashの入力を受けてDataクラスへ格納する
    """
    def __init__(self, r: Tk):
        """
        Args:
            r(Tk): tk.Tk()で取得できるwindow
        """
        super().__init__()
        self.root = r

        # --- パーツ定義 --- #
        self.frame = Frame(r)

        # ファイル選択
        self.filepath = StringVar()
        self.filepath.set("None is selected")
        self.filepath_label = Label(self.frame, textvariable=self.filepath)
        self.file_button = Button(self.frame, text="Select", command=self._file_dialog)

        plz_choose = Label(self.frame, text="Please select the folder you want us to calculate.")

        # 計算を行うボタン
        self.calc_button = Button(
            self.frame,
            text="Next",
            command=self._call_calc
        )

        # テキストボックス
        self.text_box = Entry(self.frame, width=100)
        self.text_box.insert(END, "Please enter your hash")

        # -------- 配置 -------- #
        Utils.space(self.frame, 3)
        plz_choose.pack()

        Utils.space(self.frame, 3)
        self.file_button.pack()

        Utils.space(self.frame, 3)
        self.filepath_label.pack()

        Utils.space(self.frame, 3)
        self.text_box.pack()
        self.calc_button.pack()
        self.frame.grid(row=0, column=0, sticky="nsew")

    def _file_dialog(self):
        file_type = [("", "*")]
        initial_dir = os.path.abspath(os.path.dirname(__file__))
        filepath = filedialog.askopenfilename(
            filetypes=file_type, initialdir=initial_dir
        )
        self.filepath.set(str(filepath))

    def _call_calc(self):
        """
        StringVarから値を受け取ってhashを計算する
        """
        input_hash = self.text_box.get()
        error_code, result_hash, checker, error_message = mainCalc(
            self.filepath.get(), input_hash, Data.algorithm_index
        )

        # hashが入力されなかった場合
        if input_hash == "":
            input_hash = "Please input your hash"

        # Dataクラスくんにぶち込む感じ
        Data.result = result_hash
        Data.user_input_hash = input_hash
        Data.checker = checker

        # 結果を表示する
        Data.pages["result"] = ResultPage(self.root)
        self._next_page()

    def _next_page(self):
        """
        次のページを呼び出す
        """
        Utils.change_page("result")


class ResultPage(Page):
    """
    3番目のページ
    Dataクラスから受け取ったデータを表示する
    """
    def __init__(self, r: Tk):
        """
        Args:
            r(tk.Tk): tk.Tk()で取得できるwindow
        """
        super().__init__()
        self.frame = Frame(r)

        # Label4人集
        calc_message_label = Label(
            self.frame,
            text="Calculated!!!",
            font=("Meiryo UI", 16, "bold")
        )
        calculated_hash_label = Label(
            self.frame,
            text="Calculated file hash:\n{}".format(Data.result)
        )
        user_input_hash_label = Label(
            self.frame,
            text="Entered file hash:\n{}".format(Data.user_input_hash)
        )
        result_label = Label(
            self.frame,
            text="Hash is correct." if Data.checker else "ERROR!!! Hash is incorrect!!!!!",
            font=("Meiryo UI", 12, "bold")
        )

        # -------- 配置 -------- #
        Utils.space(self.frame, 5)
        calc_message_label.pack()
        calculated_hash_label.pack()
        user_input_hash_label.pack()
        result_label.pack()
        self.frame.grid(row=0, column=0, sticky="nsew")

    def _next_page(self):
        pass


class Data:
    algorithm_index = 0
    filepath = ""
    pages = {}
    result = ""
    user_input_hash = ""
    checker = False


class Utils:
    @staticmethod
    def change_page(page_name: str):
        Data.pages[page_name].frame.tkraise()

    @staticmethod
    def space(frame: Frame, count: int):
        for _ in range(count):
            Label(frame, text="").pack()


if __name__ == "__main__":
    root = Root()
