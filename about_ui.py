"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""
import webbrowser
from tkinter import *
from tkinter.ttk import *
github_URL = "https://github.com/krrcream/krr-s-osumania-anyKeys-converter"
bilibili_URL = "https://space.bilibili.com/276844"
osu_URL = "https://osu.ppy.sh/users/14769563"

class WinGUI(Toplevel):
    def __init__(self,language):
        super().__init__()
        self.language = language
        self.__win()
        self.iconbitmap('f.ico')
        self.tk_frame_buttom = self.__tk_frame_buttom(self)
        self.tk_label_conme = self.__tk_label_conme(self.tk_frame_buttom)
        self.tk_label_OSU_URL = self.__tk_label_OSU_URL(self.tk_frame_buttom)
        self.tk_label_conline = self.__tk_label_conline(self.tk_frame_buttom)
        self.tk_label_Bilibili_URL = self.__tk_label_Bilibili_URL(self.tk_frame_buttom)
        self.tk_canvas_hxbu = self.__tk_canvas_hxbu(self)
        self.tk_label_Acknowledge = self.__tk_label_Acknowledge(self)
        self.tk_label_YuliangSSS = self.__tk_label_YuliangSSS(self)
        self.tk_label_Chiral_Cabbage = self.__tk_label_Chiral_Cabbage(self)
        self.tk_label_u_e = self.__tk_label_u_e(self)
        self.tk_label_RichMineral = self.__tk_label_RichMineral(self)
        self.tk_text_readme = self.__tk_text_readme(self)

    def __win(self):
        if self.language == 'zh':
            self.title("使用说明")
        else:
            self.title("Guide")
        # 设置窗口大小、居中
        width = 450
        height = 700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_frame_buttom(self, parent):
        frame = Frame(parent, )
        frame.place(x=3, y=667, width=447, height=33)
        return frame

    def __tk_label_conme(self, parent):
        temp ="联系方式:" if self.language == 'zh' else "Contact:"
        label = Label(parent, text=temp , anchor="center", )
        label.place(x=7, y=0, width=70, height=30)
        return label

    def __tk_label_OSU_URL(self, parent):
        label = Label(parent, text="OSU",foreground='blue', anchor="center",font=('', 10, 'underline'))
        label.place(x=394, y=0, width=50, height=30)
        label.config(cursor="hand2")
        label.bind("<Button-1>", lambda e: webbrowser.open(osu_URL))
        return label

    def __tk_label_conline(self, parent):
        label = Label(parent, text="QQ:510089504|Discord:krrcream", anchor="center", )
        label.place(x=84, y=0, width=211, height=30)
        return label

    def __tk_label_Bilibili_URL(self, parent):
        label = Label(parent, text="Bilibili", foreground='blue', anchor="center", font=('', 10, 'underline'))
        label.place(x=326, y=0, width=60, height=30)
        label.config(cursor="hand2")
        label.bind("<Button-1>", lambda e: webbrowser.open(bilibili_URL))
        return label

    def __tk_canvas_hxbu(self, parent):
        canvas = Canvas(parent)
        canvas.place(x=5, y=4, width=429, height=83)
        canvas.create_rectangle(7, 6, 426, 80, outline='black', width=2)
        return canvas

    def __tk_label_Acknowledge(self, parent):
        temp ="特别感谢" if self.language == 'zh' else "Acknowledgement"
        label = Label(parent, text=temp, anchor="center", font=('', 20, 'bold'))
        label.place(x=19, y=14, width=410, height=30)
        return label

    def __tk_label_YuliangSSS(self, parent):
        label = Label(parent, text="YuliangSSS", foreground='blue', anchor="center",font=('', 10, 'underline'))
        label.place(x=19, y=52, width=95, height=30)
        label.config(cursor="hand2")
        label.bind("<Button-1>", lambda e: webbrowser.open("https://osu.ppy.sh/users/15889644"))
        return label

    def __tk_label_Chiral_Cabbage(self, parent):
        label = Label(parent, text="Chiral_Cabbage", foreground='blue', anchor="center",font=('', 10, 'underline'))
        label.place(x=120, y=52, width=104, height=30)
        label.config(cursor="hand2")
        label.bind("<Button-1>", lambda e: webbrowser.open("https://osu.ppy.sh/users/32288791"))
        return label

    def __tk_label_u_e(self, parent):
        label = Label(parent, text="u_e", foreground='blue', anchor="center",font=('', 10, 'underline'))
        label.place(x=229, y=52, width=95, height=30)
        label.config(cursor="hand2")
        label.bind("<Button-1>", lambda e: webbrowser.open("https://osu.ppy.sh/users/2594421"))
        return label

    def __tk_label_RichMineral(self, parent):
        label = Label(parent, text="RichMineral", foreground='blue', anchor="center",font=('', 10, 'underline'))
        label.place(x=334, y=52, width=95, height=30)
        label.config(cursor="hand2")
        label.bind("<Button-1>", lambda e: webbrowser.open("https://osu.ppy.sh/users/35448136"))
        return label

    def __tk_text_readme(self, parent):
        text = Text(parent)
        # 设置文字字体
        text.configure(font=("Arial", 11))

        # 定义黑体字样式
        text.tag_configure("bold", font=("Arial", 11, "bold"))
        if self.language == 'zh':
            text.insert(END, "使用方法：", "bold")
            text.insert(END, "只需将.osu文件或包含.osu文件的文件夹拖入本程序窗口，即可完成批量转谱操作\n")
            text.insert(END,
                        "1. 预设功能：", "bold")
            text.insert(END,
                        "提供了多种预设选项，方便您快速上手。如果您不熟悉详细设置，可以直接选择预设进行操作\n")
            text.insert(END, "2. 程序界面上半部分：\n","bold")

            # 使用黑体字标签插入文本
            text.insert(END, "    2.1. OD和HP设置：", "bold")
            text.insert(END,
                        "如果您希望保留原谱的OD（Overall Difficulty）和HP（Hurt Points）值，请留空；如需修改，请输入新的数值并保存\n")

            text.insert(END, "    2.2. 保存路径：", "bold")
            text.insert(END,
                        "勾选“保存到原路径”将在原谱文件所在位置生成新谱；若您希望将所有转谱文件集中存储，请取消勾选并指定新的文件夹路径\n")

            text.insert(END, "    2.3. Seed功能：", "bold")
            text.insert(END, "使用相同的数字作为seed，将得到相同的转谱结果（大部分情况下）\n")

            text.insert(END, "3. 狂风插入：\n", "bold")

            text.insert(END, "    3.1. 转换速度：", "bold")
            text.insert(END, "该数值越大，排列变换速度越快，排列越随机；数值越小，随机性越小\n")

            text.insert(END, "    3.2. 目标键数：", "bold")
            text.insert(END, "指定您希望生成的键数\n")

            text.insert(END, "    3.3. 插入空列：", "bold")
            text.insert(END, "如果您觉得谱面密度过高，可以使用此功能在谱中插入空白列\n")

            text.insert(END, "    3.4. 密度调整：", "bold")
            text.insert(END, "这是一个试验性功能，降低密度可能会移除原谱的一些细节\n")

            text.insert(END, "    3.5. Jack处理：", "bold")
            text.insert(END, "在不同排列变换过程中可能会生成MiniJack，如果您希望保留这些Jack，请取消勾选\n")

            text.insert(END, "    3.6. 筛选器：", "bold")
            text.insert(END, "在批量处理文件时，此功能可以自动识别并筛选出您指定的键数\n")

            text.insert(END, "4. 简单矩阵：", "bold")
            text.insert(END, "请查看选项卡中的详细说明\n", )

            text.insert(END,
                        "5. 万物化叠和万物化切：", "bold")
            text.insert(END,
                        "这是两个试验性功能，它们会取原谱的start_time，并随机生成切或叠（大便）\n", )

            text.insert(END,
                        "6. 杰克世界：", "bold")
            text.insert(END,
                        "这也是一个试验性功能，它在原谱的基础上，通过横向和纵向增加note，进一步加入jack元素（大便）\n", )
        else:
            text.configure(wrap=WORD)
            text.insert(END, "Usage: ", "bold")
            text.insert(END, "Drag and drop your.osu file or folder containing.osu files into this program window to convert them all.\n")
            text.insert(END,
                        "1. Presets: ", "bold")
            text.insert(END,
                        "Multiple preset options are provided for quick setup. If you are not familiar with detailed settings, you can directly choose a preset to operate.\n")
            text.insert(END, "2. Upper Half of theProgram interface: \n", "bold")
            text.insert(END, "    2.1. OD and HP settings: ", "bold")
            text.insert(END,  "If you want to keep the original OD and HP values, leave them empty. If you need to modify them, enter the new values.\n")
            text.insert(END, "    2.2. Save Path: ", "bold")
            text.insert(END, "Check 'Save to Original Path' to generate new maps in the original location. If you want to store all converted maps in a folder, uncheck it and specify a new folder path.\n")
            text.insert(END, "    2.3. Seed Function: ", "bold")
            text.insert(END, "Use the same number as the seed to get the same converted result (most of the time).\n")
            text.insert(END, "3. Gale Insertion (NtoNC): \n", "bold")
            text.insert(END, "    3.1. Conversion Speed: ", "bold")
            text.insert(END, "The larger the value, the faster the arrangement changes, and the arrangement becomes more random. The smaller the value, the less randomness.\n")
            text.insert(END, "    3.2. Target Keys: ", "bold")
            text.insert(END, "Specify the number of keys you want to generate.\n")
            text.insert(END, "    3.3. Insert blank Columns: ", "bold")
            text.insert(END, "If you feel that the density of the map is too high, you can use this to insert empty columns in the map.\n")
            text.insert(END, "    3.4. Density Adjustment: ", "bold")
            text.insert(END, "This is an experimental function that reduces the density of the map may remove some details of the original map.\n")
            text.insert(END, "    3.5. Delete generated jacks: ", "bold")
            text.insert(END, "In different arrangement changes, MiniJacks may be generated. If you want to keep these Jacks, please uncheck this option.\n")
            text.insert(END, "    3.6. Filter: ", "bold")
            text.insert(END, "This function can automatically identify and filter out the specified keys in batch processing.\n")
            text.insert(END, "4. Simple Matrix (NtoNS): ", "bold")
            text.insert(END, "Please refer to the detailed explanation in the tab.\n", )
            text.insert(END, "5. Everything to Jack or Stream: ", "bold")
            text.insert(END, "These are two experimental functions, which extract the start_time of the original map and randomly generate a slice or unravel (poop).\n", )
            text.insert(END, "6. Jack World: ", "bold")
            text.insert(END, "This is also an experimental function, which adds notes horizontally and vertically based on the original map, further adding jack elements (poop).\n", )
        text.config(state=DISABLED)
        text.place(x=10, y=102, width=429, height=557)
        return text

class MyGUI:
    def __init__(self, master):
        pass
    def open_about_window(self):
        about_window = WinGUI(language='zh')
        about_window.grab_set()

if __name__ == "__main__":
    root = Tk()
    my_gui = MyGUI(root)
    root.mainloop()