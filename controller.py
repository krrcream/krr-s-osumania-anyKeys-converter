"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""
import os
import shutil
from pathlib import Path
import threading
from tkinter import BooleanVar, ttk, IntVar, DoubleVar
from about_ui import WinGUI as AboutGUI
from functions import *
from Every_series_and_jack_world import *
from NtoNC_HitObjects import NtoNC_HitObjects
from preset_HitObjects import Preset_HitObjects
from matadata import MataData
from ui import Win

github_URL = "https://github.com/krrcream/krr-s-osumania-anyKeys-converter"
bilibili_URL = "https://space.bilibili.com/276844"
osu_URL = "https://osu.ppy.sh/users/14769563"
program_version = "v1.0.1"

#替换成你的图标文件路径
ico_file = r"D:\mypythpon_project\krr_any_keys_converter V1.0.0\pythonProject\f.ico"

class Controller:
    ui: Win

    def __init__(self):
        pass

    def init(self, ui):
        # 实例化
        self.ui = ui
        self.ui.resizable(False, False)

        self.language = 'zh'

        self.ui.iconbitmap(ico_file)
        self.ui.title("krrcream的任意keys转换器 " + program_version)
        self.ui.protocol("WM_DELETE_WINDOW", self.on_closing)

        #选项卡值
        self.selected_tab_index = IntVar(value=0)
        style = ttk.Style()
        style.configure("TNotebook.Tab", background="white", foreground="black")
        style.configure("TNotebook.Tab.selected", background="purple", foreground="white")

        self.ui.tk_tabs_select.bind("<<NotebookTabChanged>>", self.tab_change)

        # 狂风插入变量
        self.s4mk_value = BooleanVar(value=False)
        self.s4k_value = BooleanVar(value=False)
        self.s5k_value = BooleanVar(value=False)
        self.s6k_value = BooleanVar(value=False)
        self.s7k_value = BooleanVar(value=False)
        self.s8k_value = BooleanVar(value=False)
        self.s9k_value = BooleanVar(value=False)
        self.s10k_value = BooleanVar(value=False)
        self.s10pk_value = BooleanVar(value=False)

        self.if_sifting_value = BooleanVar(value=False)

        self.if_del_jack_value = BooleanVar(value=True)

        self.if_use_seed_value = BooleanVar(value=False)

        self.if_save_to_org_value = BooleanVar(value=True)

        self.to_key_value = IntVar(value=10)  # 目标键数

        self.blank_value = IntVar(value=0)  # 空白键数

        self.step_value = IntVar(value=15)  # 步距

        self.stap_time = DoubleVar(value=29998.8584 * math.exp(-0.3176 * self.to_key_value.get()) + 347.7248)

        self.density_value = IntVar(value=10)  # 密度

        self.if_del_jack_value.set(True)

        # 是否保存到原目录关联输入框
        self.ui.tk_input_path.configure(state='disable', foreground='gray')
        self.ui.tk_input_title.configure(state='disable', foreground='gray')
        self.ui.tk_input_artist.configure(state='disable', foreground='gray')
        #OD和HP输入框
        self.ui.tk_input_OD.configure(state='normal')
        self.ui.tk_input_HP.configure(state='normal')
        #seed输入框
        self.ui.tk_input_seed_line.configure(state='disable')

        #简单矩阵控件
        self.ui.tk_input_NToNS_num_line.configure(state='normal')

        # 万物系列
        self.EV_jack_or_stream = IntVar(value=1)
        self.to_key_value_EV = IntVar(value=10)
        self.density_value_EV = IntVar(value=2)
        self.noise_value_EV = DoubleVar(value=0.0)

        #杰克世界
        self.JW_w_density = DoubleVar(value=0.0)
        self.JW_h_density = DoubleVar(value=0.2)
        self.JW_add = IntVar(value=2)

        # 读取配置文件
        self.load_config()

        #狂风插入控件
        #元谱筛选框
        self.ui.tk_check_button_s4mk.configure(variable=self.s4mk_value, onvalue=True, offvalue=False, state='disable')
        self.ui.tk_check_button_s4k.configure(variable=self.s4k_value, onvalue=True, offvalue=False, state='disable')
        self.ui.tk_check_button_s5k.configure(variable=self.s5k_value, onvalue=True, offvalue=False, state='disable')
        self.ui.tk_check_button_s6k.configure(variable=self.s6k_value, onvalue=True, offvalue=False, state='disable')
        self.ui.tk_check_button_s7k.configure(variable=self.s7k_value, onvalue=True, offvalue=False, state='disable')
        self.ui.tk_check_button_s8k.configure(variable=self.s8k_value, onvalue=True, offvalue=False, state='disable')
        self.ui.tk_check_button_s9k.configure(variable=self.s9k_value, onvalue=True, offvalue=False, state='disable')
        self.ui.tk_check_button_s10k.configure(variable=self.s10k_value, onvalue=True, offvalue=False, state='disable')
        self.ui.tk_check_button_s10pk.configure(variable=self.s10pk_value, onvalue=True, offvalue=False,
                                                state='disable')
        #元谱筛选框
        self.ui.tk_check_button_if_sifting.configure(variable=self.if_sifting_value, cursor='hand2', onvalue=True,
                                                     offvalue=False, command=self.if_sifting)
        # 点击元谱筛选框时，根据元谱筛选框的状态，设置元谱筛选框的状态

        #是否处理子弹
        self.ui.tk_check_button_if_del_jack.configure(variable=self.if_del_jack_value, cursor='hand2', onvalue=True,
                                                      offvalue=False)
        #是否使用种子

        self.ui.tk_check_button_if_use_seed.configure(variable=self.if_use_seed_value, cursor='hand2', onvalue=True,
                                                      offvalue=False, command=self.if_use_seed)
        self.ui.tk_button_gen_seed_button.configure(cursor='hand2')
        self.ui.tk_button_gen_seed_button.bind("<Button-1>", self.gen_seed)

        self.ui.tk_check_button_if_save_to_org.configure(variable=self.if_save_to_org_value, cursor='hand2',
                                                         onvalue=True, offvalue=False, command=self.if_save_to_org)

        #初始化tokey滑条条
        #滑条范围为1到24，初始值为10，步长为1，和to_key_value绑定
        self.ui.tk_scale_to_key_slider.configure(from_=1, to=24, variable=self.to_key_value,
                                                 command=self.to_key_change)

        #初始化blank滑条
        self.ui.tk_scale_insert_blank_slider.configure(from_=0, to=self.to_key_value.get(),
                                                       variable=self.blank_value, command=self.blank_change)

        #初始化密度滑条
        #滑条范围为1到10，初始值为10，步长为1，和density_value绑定
        self.ui.tk_scale_density_slider.configure(from_=0, to=10, variable=self.density_value,
                                                  command=self.density_change)

        #初始化步距滑条
        #滑条范围为1到20，初始值为15，步长为1，和step_value绑定
        self.ui.tk_scale_convert_interval.configure(from_=1, to=24, variable=self.step_value,
                                                    command=self.step_change)

        #删除新生成的子弹
        self.ui.tk_check_button_if_del_jack.configure(variable=self.if_del_jack_value, cursor='hand2', onvalue=True,
                                                      offvalue=False)

        #万物系列单选框
        self.ui.tk_radio_button_EtoJACK_sel.configure(variable=self.EV_jack_or_stream, value=0,
                                                      command=self.EV_jack_or_stream_change)
        self.ui.tk_radio_button_EtoStream_sel.configure(variable=self.EV_jack_or_stream, value=1,
                                                        command=self.EV_jack_or_stream_change)

        #万物系列滑条
        self.ui.tk_scale_EV_to_key.configure(from_=1, to=24, variable=self.to_key_value_EV,
                                             command=self.to_key_value_EV_change)
        self.ui.tk_scale_EV_density.configure(from_=0,
                                              to=self.to_key_value_EV.get() if self.EV_jack_or_stream.get() == 0
                                              else int(self.to_key_value_EV.get() / 2), variable=self.density_value_EV,
                                              command=self.density_EV_change)
        self.ui.tk_scale_EV_noise.configure(from_=0, to=1, variable=self.noise_value_EV, command=self.noise_EV_change)

        #杰克世界
        self.ui.tk_scale_JW_h_density_slider.configure(from_=0, to=1, variable=self.JW_h_density,
                                                       command=self.JW_h_density_change)
        self.ui.tk_scale_JW_w_density_slider.configure(from_=0, to=1, variable=self.JW_w_density,
                                                       command=self.JW_w_density_change)
        self.ui.tk_scale_JW_add_slider.configure(from_=1, to=10, variable=self.JW_add, command=self.JW_add_change)

        #预设单选框
        self.preset_value = IntVar(value=0)
        self.ui.tk_radio_button_preset_NKDP.configure(variable=self.preset_value, value=0)
        self.ui.tk_radio_button_preset_NKDPM.configure(variable=self.preset_value, value=1)
        self.ui.tk_radio_button_preset_7kto6k.configure(variable=self.preset_value, value=2)
        self.ui.tk_radio_button_preset_4kdpto10k.configure(variable=self.preset_value, value=3)
        self.ui.tk_radio_button_preset_4kdpmto10k.configure(variable=self.preset_value, value=4)
        self.ui.tk_radio_button_preset_6kto10k.configure(variable=self.preset_value, value=5)
        self.ui.tk_radio_button_preset_7kto10k.configure(variable=self.preset_value, value=6)
        self.ui.tk_radio_button_preset_4kt6t10.configure(variable=self.preset_value, value=7)
        self.ui.tk_radio_button_preset_4kt7t10.configure(variable=self.preset_value, value=8)
        self.ui.tk_radio_button_preset_4kto7k.configure(variable=self.preset_value, value=9)

        #给标签Github添加链接
        self.ui.tk_label_change.configure(cursor='hand2', foreground='blue', font=('', 10, 'underline'))
        self.ui.tk_label_change.bind("<Button-1>", lambda event: self.change_language())  # 绑定鼠标左键单击事件
        # self.ui.tk_label_Github.bind("<Button-1>", lambda e: webbrowser.open_new(github_URL))  # 绑定鼠标左键单击事件
        #About标签
        self.ui.tk_label_About.configure(cursor='hand2', foreground='blue', font=('', 10, 'underline'))
        self.ui.tk_label_About.bind("<Button-1>", self.open_about_window)

    def open_about_window(self, event):
        about_window = AboutGUI(self.language,ico_file)
        about_window.grab_set()


    # def preset_change(self):
    #     print(self.preset_value.get())

    def on_closing(self):
        self.save_config()
        self.ui.destroy()

    def save_config(self):
        config_data = {
            's4mk_value': self.s4mk_value.get(),
            's4k_value': self.s4k_value.get(),
            's5k_value': self.s5k_value.get(),
            's6k_value': self.s6k_value.get(),
            's7k_value': self.s7k_value.get(),
            's8k_value': self.s8k_value.get(),
            's9k_value': self.s9k_value.get(),
            's10k_value': self.s10k_value.get(),
            's10pk_value': self.s10pk_value.get(),
            'if_sifting_value': self.if_sifting_value.get(),
            'if_del_jack_value': self.if_del_jack_value.get(),
            'if_save_to_org_value': self.if_save_to_org_value.get(),
            'if_use_seed_value': self.if_use_seed_value.get(),
            'to_key_value': self.to_key_value.get(),
            'blank_value': self.blank_value.get(),
            'step_value': self.step_value.get(),
            'input_path': self.ui.tk_input_path.get(),
            'input_title': self.ui.tk_input_title.get(),
            'input_artist': self.ui.tk_input_artist.get(),
            'input_OD': self.ui.tk_input_OD.get(),
            'input_HP': self.ui.tk_input_HP.get(),
            'input_seed': self.ui.tk_input_seed_line.get()
        }

        with open('config.fq', 'w') as f:
            for key, value in config_data.items():
                if isinstance(value, bool):
                    value = str(value).lower()  # 将布尔值转换为小写的字符串
                f.write(f"{key}={value}\n")

    def load_config(self):
        try:
            with open('config.fq', 'r') as f:
                lines = f.readlines()

            config_data = {}
            for line in lines:
                try:
                    key, value = line.strip().split('=')
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    else:
                        try:
                            value = int(value)  # 尝试将值转换为整数
                        except ValueError:
                            pass  # 如果转换失败，保留原字符串
                    config_data[key] = value
                except ValueError:
                    print(f"读取时line.strip()出错:")
            # 设置变量的值
            self.s4mk_value.set(config_data.get('s4mk_value', False))
            self.s4k_value.set(config_data.get('s4k_value', False))
            self.s5k_value.set(config_data.get('s5k_value', False))
            self.s6k_value.set(config_data.get('s6k_value', False))
            self.s7k_value.set(config_data.get('s7k_value', False))
            self.s8k_value.set(config_data.get('s8k_value', False))
            self.s9k_value.set(config_data.get('s9k_value', False))
            self.s10k_value.set(config_data.get('s10k_value', False))
            self.s10pk_value.set(config_data.get('s10pk_value', False))
            self.if_sifting_value.set(config_data.get('if_sifting_value', False))
            self.if_del_jack_value.set(config_data.get('if_del_jack_value', False))
            self.if_save_to_org_value.set(config_data.get('if_save_to_org_value', True))
            self.if_use_seed_value.set(config_data.get('if_use_seed_value', False))
            self.to_key_value.set(config_data.get('to_key_value', 10))
            self.blank_value.set(config_data.get('blank_value', 0))
            self.step_value.set(config_data.get('step_value', 15))

            #设置筛选
            if self.if_sifting_value.get():
                self.ui.tk_check_button_s4mk.configure(state='enable')
                self.ui.tk_check_button_s4k.configure(state='enable')
                self.ui.tk_check_button_s5k.configure(state='enable')
                self.ui.tk_check_button_s6k.configure(state='enable')
                self.ui.tk_check_button_s7k.configure(state='enable')
                self.ui.tk_check_button_s8k.configure(state='enable')
                self.ui.tk_check_button_s9k.configure(state='enable')
                self.ui.tk_check_button_s10k.configure(state='enable')
                self.ui.tk_check_button_s10pk.configure(state='enable')

            else:
                self.ui.tk_check_button_s4mk.configure(state='disable')
                self.ui.tk_check_button_s4k.configure(state='disable')
                self.ui.tk_check_button_s5k.configure(state='disable')
                self.ui.tk_check_button_s6k.configure(state='disable')
                self.ui.tk_check_button_s7k.configure(state='disable')
                self.ui.tk_check_button_s8k.configure(state='disable')
                self.ui.tk_check_button_s9k.configure(state='disable')
                self.ui.tk_check_button_s10k.configure(state='disable')

            #更新输入框状态
            if self.if_save_to_org_value.get():
                self.ui.tk_input_path.configure(state='disable', foreground='gray')
                self.ui.tk_input_title.configure(state='disable', foreground='gray')
                self.ui.tk_input_artist.configure(state='disable', foreground='gray')
                # 如果不选中，则只读输入框
            else:
                self.ui.tk_input_path.configure(state='normal', foreground='black')
                self.ui.tk_input_title.configure(state='normal', foreground='black')
                self.ui.tk_input_artist.configure(state='normal', foreground='black')

            if self.if_use_seed_value.get():
                self.ui.tk_input_seed_line.configure(state='normal')
            else:
                self.ui.tk_input_seed_line.configure(state='disable')

            # 设置输入框的值
            self.ui.tk_input_seed_line.delete(0, 'end')
            self.ui.tk_input_seed_line.insert(0, config_data.get('input_seed', ''))
            self.ui.tk_input_path.delete(0, 'end')
            self.ui.tk_input_path.insert(0, config_data.get('input_path', ''))
            self.ui.tk_input_title.delete(0, 'end')
            self.ui.tk_input_title.insert(0, config_data.get('input_title', ''))
            self.ui.tk_input_artist.delete(0, 'end')
            self.ui.tk_input_artist.insert(0, config_data.get('input_artist', ''))
            self.ui.tk_input_OD.delete(0, 'end')
            self.ui.tk_input_OD.insert(0, config_data.get('input_OD', ''))
            self.ui.tk_input_HP.delete(0, 'end')
            self.ui.tk_input_HP.insert(0, config_data.get('input_HP', ''))

            # 设置标签显示
            self.ui.tk_label_to_key_num.configure(text=str(self.to_key_value.get()))
            self.ui.tk_label_insert_blank_num.configure(text=str(self.blank_value.get()))
            self.ui.tk_label_step_num.configure(text=str(self.step_value.get()))


        except FileNotFoundError:
            pass  # 如果文件不存在，则不进行任何操作

        # 种子生成按钮事件

    def gen_seed(self, evt):  # 生成种子按钮事件
        num = generate_seed()
        self.ui.tk_input_seed_line.delete(0, 'end')
        self.ui.tk_input_seed_line.insert(0, num)

    def if_use_seed(self):  # 是否使用种子按钮事件
        if self.if_use_seed_value.get():
            self.ui.tk_input_seed_line.configure(state='normal')
        #如果不选中，则隐藏输入框
        else:
            self.ui.tk_input_seed_line.configure(state='disable')

    # 元谱筛选框事件
    def if_sifting(self):
        if self.if_sifting_value.get():
            self.ui.tk_check_button_s4mk.configure(state='enable')
            self.ui.tk_check_button_s4k.configure(state='enable')
            self.ui.tk_check_button_s5k.configure(state='enable')
            self.ui.tk_check_button_s6k.configure(state='enable')
            self.ui.tk_check_button_s7k.configure(state='enable')
            self.ui.tk_check_button_s8k.configure(state='enable')
            self.ui.tk_check_button_s9k.configure(state='enable')
            self.ui.tk_check_button_s10k.configure(state='enable')
            self.ui.tk_check_button_s10pk.configure(state='enable')
            self.s4mk_value.set(True)
            self.s4k_value.set(True)
            self.s5k_value.set(True)
            self.s6k_value.set(True)
            self.s7k_value.set(True)
            self.s8k_value.set(True)
            self.s9k_value.set(True)
            self.s10k_value.set(True)
            self.s10pk_value.set(True)
        else:
            self.ui.tk_check_button_s4mk.configure(state='disable')
            self.ui.tk_check_button_s4k.configure(state='disable')
            self.ui.tk_check_button_s5k.configure(state='disable')
            self.ui.tk_check_button_s6k.configure(state='disable')
            self.ui.tk_check_button_s7k.configure(state='disable')
            self.ui.tk_check_button_s8k.configure(state='disable')
            self.ui.tk_check_button_s9k.configure(state='disable')
            self.ui.tk_check_button_s10k.configure(state='disable')
            self.ui.tk_check_button_s10pk.configure(state='disable')
            self.s4mk_value.set(False)
            self.s4k_value.set(False)
            self.s5k_value.set(False)
            self.s6k_value.set(False)
            self.s7k_value.set(False)
            self.s8k_value.set(False)
            self.s9k_value.set(False)
            self.s10k_value.set(False)
            self.s10pk_value.set(False)
        # print(self.s4k_value.get())

    def if_save_to_org(self):  # 是否保存到原目录按钮事件
        if self.if_save_to_org_value.get():
            self.ui.tk_input_path.configure(state='disable', foreground='gray', )
            self.ui.tk_input_title.configure(state='disable', foreground='gray')
            self.ui.tk_input_artist.configure(state='disable', foreground='gray')
            #如果不选中，则只读输入框
        else:
            self.ui.tk_input_path.configure(state='normal', foreground='black')
            self.ui.tk_input_title.configure(state='normal', foreground='black')
            self.ui.tk_input_artist.configure(state='normal', foreground='black')

    def to_key_change(self, value):  # 目标键数滑动条事件
        int_value = int(float(value))  # 将浮点数转为整数
        self.to_key_value.set(int_value)  # 更新IntVar的值
        self.ui.tk_label_to_key_num.configure(text=str(int_value))  # 更新标签显示
        self.ui.tk_scale_insert_blank_slider.configure(from_=0, to=self.to_key_value.get(),
                                                       value=self.blank_value.get(),
                                                       variable=self.blank_value, command=self.blank_change)

    def blank_change(self, value):  # 空白键数滑动条事件
        int_value = int(float(value))  # 将浮点数转为整数
        self.blank_value.set(int_value)  # 更新IntVar的值
        self.ui.tk_label_insert_blank_num.configure(text=str(int_value))  # 更新标签显示

    def step_change(self, value):  # 步距滑动条事件
        temp = 0
        int_value = int(float(value))  # 将浮点数转为整数
        self.step_value.set(int_value)  # 更新IntVar的值
        self.ui.tk_label_step_num.configure(text=str(int_value))  # 更新标签显示
        int_value -= 1
        if int_value == 0:
            temp = 99999999.9999
        elif 0 < int_value <= 19:
            temp = 29998.8584 * math.exp(-0.3176 * int_value) + 347.7248
        elif 19 < int_value <= 23:
            temp = 420.0000 - (int_value - 19) * 50.0000
        self.stap_time.set(temp)  # 更新DoubleVar的值
        # print(self.stap_time.get())

    def density_change(self, value):  # 密度滑动条事件
        int_value = int(float(value))  # 将浮点数转为整数
        self.density_value.set(int_value)  # 更新IntVar的值
        self.ui.tk_label_density_value.configure(text=str(int_value))  # 更新标签显示

    def tab_change(self, event):  # 选项卡事件
        # 获取当前选中的选项卡
        selected_tab = event.widget.select()
        self.selected_tab_index.set(event.widget.index(selected_tab))

    def EV_jack_or_stream_change(self):
        self.ui.tk_scale_EV_density.configure(from_=0,
                                              to=self.to_key_value_EV.get() if self.EV_jack_or_stream.get() == 0
                                              else (1 if self.to_key_value_EV.get() == 1 else int(
                                                  self.to_key_value_EV.get() / 2)), variable=self.density_value_EV,
                                              command=self.density_EV_change)
        temp = self.to_key_value_EV.get() if self.EV_jack_or_stream.get() == 0 else (
            1 if self.to_key_value_EV.get() == 1 else int(self.to_key_value_EV.get() / 2))
        self.ui.tk_label_Lab_EV_density.configure(text=temp)  # 更新标签显示
        self.density_value_EV.set(temp)  # 设置密度为0

    #万物系列
    def to_key_value_EV_change(self, value):  # 目标键数滑动条事件
        int_value = int(float(value))  # 将浮点数转为整数
        self.to_key_value_EV.set(int_value)  # 更新IntVar的值
        self.ui.tk_scale_EV_density.configure(from_=0,
                                              to=self.to_key_value_EV.get() if self.EV_jack_or_stream.get() == 0
                                              else (1 if self.to_key_value_EV.get() == 1 else int(
                                                  self.to_key_value_EV.get() / 2)), variable=self.density_value_EV,
                                              command=self.density_EV_change)
        self.ui.tk_label_lab_EV_to_key.configure(text=str(int_value))  # 更新标签显示

    def density_EV_change(self, value):  # 密度滑动条事件
        int_value = int(float(value))  # 将浮点数转为整数
        self.density_value_EV.set(int_value)  # 更新IntVar的值
        self.ui.tk_label_Lab_EV_density.configure(text=str(int_value))  # 更新标签显示

    def noise_EV_change(self, value):  # 噪声滑动条事件
        value = float(value)
        self.noise_value_EV.set(value)  # 更新DoubleVar的值
        self.ui.tk_label_Lab_EV_noise.configure(text=str(value))  # 更新标签显示

    def JW_w_density_change(self, value):  # 密度滑动条事件
        value = float(value)  # 将浮点数转为整数
        self.ui.tk_label_JW_w_lab.configure(text=str(value))  # 更新IntVar的值

    def JW_h_density_change(self, value):  # 密度滑动条事件
        value = float(value)  # 将浮点数转为整数
        self.ui.tk_label_JW_h_lab.configure(text=str(value))  # 更新IntVar的值

    def JW_add_change(self, value):  # 密度滑动条事件
        int_value = int(float(value))  # 将浮点数转为整数
        self.ui.tk_label_JW_add_lab.configure(text=str(int_value))  # 更新IntVar的值

    def on_drop(self, event):
        paths = self.ui.tk.splitlist(event.data)

        def process_file(file):
            # try:
                if self.if_use_seed_value.get():
                    seed = int(self.ui.tk_input_seed_line.get() or 0)  # 使用 or 运算符处理空字符串
                    random.seed(seed)
                    np.random.seed(seed)
                if self.selected_tab_index.get() == 0:
                    self.NtoNC(file)
                elif self.selected_tab_index.get() == 1:
                    self.NtoNS(file)
                elif self.selected_tab_index.get() == 2:
                    self.Everything_To_N(file)
                elif self.selected_tab_index.get() == 3:
                    self.Jack_World(file)
                elif self.selected_tab_index.get() == 4:
                    self.preset_convert(file)
            # except Exception as e:
            #     print(f"处理文件 {file} 时发生错误: {e}")
        def handle_path(path):
            path = Path(path)
            if path.exists():
                if path.is_file():
                    if if_osu_file(str(path)):
                        process_file(str(path))  # 直接处理文件
                elif path.is_dir():
                    for root_dir, dirs, files in os.walk(path):
                        root_dir = Path(root_dir)
                        for name in files:
                            file_path = root_dir / name
                            if if_osu_file(str(file_path)):
                                process_file(str(file_path))  # 直接处理文件

        threading.BoundedSemaphore(value=min(len(paths), os.cpu_count() + 4, 10))
        threads = []  # 新建一个线程列表
        for path in paths:
            thread = threading.Thread(target=handle_path, args=(path,))  # 创建线程
            thread.start()  # 启动线程
            threads.append(thread)  # 添加到线程列表

    def on_radio_button_select_E(self, selected_value):
        if selected_value == 1:
            self.ui.tk_radio_button_EtoJACK_sel.configure(value=True)
        elif selected_value == 2:
            self.ui.tk_radio_button_EtoStream_sel.configure(value=True)

            #转谱

    def NtoNC(self, file):
        """
        将谱子转换为NC键
        """
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        META, HOBJ = osu_file_str_split1(content)
        METAs = MataData(META)
        org_keys = int(METAs.get_data("CircleSize")[0])
        should_process = True
        if self.if_sifting_value.get():
            should_process = False
            # 判断 org_key 是否满足条件
            if (self.s4mk_value.get() and org_keys < 4) or \
                    (self.s4k_value.get() and org_keys == 4) or \
                    (self.s5k_value.get() and org_keys == 5) or \
                    (self.s6k_value.get() and org_keys == 6) or \
                    (self.s7k_value.get() and org_keys == 7) or \
                    (self.s8k_value.get() and org_keys == 8) or \
                    (self.s9k_value.get() and org_keys == 9) or \
                    (self.s10k_value.get() and org_keys == 10) or \
                    (self.s10pk_value.get() and org_keys > 10):
                should_process = True

        if should_process:
            pass

            to_keys = self.to_key_value.get()
            blank = self.blank_value.get()
            interval = self.stap_time.get()
            OD = self.ui.tk_input_OD.get()
            HP = self.ui.tk_input_HP.get()
            #如果HP和OD不是0.0到10.0的浮点数（包含0和10),则修改，否则不修改
            if HP:
                try:
                    float_hp = round(float(HP), 1)  # 转换为浮点数
                    if 0.0 <= float_hp <= 10.0:  # 检查范围
                        METAs.set_data("HPDrainRate", HP)
                except ValueError:
                    pass  # 忽略无效输入
            if OD:
                try:
                    float_od = round(float(OD), 1)  # 转换为浮点数
                    if 0.0 <= float_od <= 10.0:  # 检查范围
                        METAs.set_data("OverallDifficulty", OD)
                except ValueError:
                    pass  # 忽略无效输入

            #处理META
            METAs.set_data("CircleSize", to_keys)
            version_tag = "[" + str(org_keys) + "To" + str(to_keys) + "C]"
            new_file_path_osu = self.save_files(version_tag, file, METAs)

            METAs_new_lines = METAs.get_new_lines()
            beat_time = float(METAs.get_data("beat_time")[0])
            #处理HitObject
            HOBJs = NtoNC_HitObjects.from_lines(HOBJ, org_keys)
            MTX = HOBJs.NtoNC_convert_MTX(to_keys, blank, interval, beat_time=beat_time,
                                          density=self.density_value.get(), del_jack_flag=self.if_del_jack_value.get())
            HOBJs_new_lines = HOBJs.get_to_keys_obj(MTX)

            #把METAs_new_lines和HOBJs_new_lines写入文件,如果文件存在则覆盖内容，如果不存在则创建文件并写入
            combined_content = '\n'.join(METAs_new_lines) + '\n' + '\n'.join(HOBJs_new_lines)

            if len(new_file_path_osu.name) > 255:
                new_file_path_osu = new_file_path_osu.parent / (
                        new_file_path_osu.stem[:255 - len(new_file_path_osu.suffix)] + new_file_path_osu.suffix)
            try:
                if os.path.exists(new_file_path_osu):
                    with open(new_file_path_osu, 'w', encoding='utf-8') as f:
                        f.write(combined_content)
                else:
                    with open(new_file_path_osu, 'x', encoding='utf-8') as f:
                        f.write(combined_content)
            except Exception as e:
                print(f"创建文件时发生错误: {e}")

    def NtoNS(self, file):
        """
        将谱子转换为NS键
        """
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

            META, HOBJ = osu_file_str_split1(content)
            METAs = MataData(META)
            org_keys = int(METAs.get_data("CircleSize")[0])
            NToNS_array = str_to_array(self.ui.tk_input_NToNS_num_line.get())
            to_keys = len(NToNS_array)
            OD = self.ui.tk_input_OD.get()
            HP = self.ui.tk_input_HP.get()
            #如果HP和OD不是0.0到10.0的浮点数（包含0和10),则修改，否则不修改
            if HP:
                try:
                    float_hp = round(float(HP), 1)  # 转换为浮点数
                    if 0.0 <= float_hp <= 10.0:  # 检查范围
                        METAs.set_data("HPDrainRate", HP)
                except ValueError:
                    pass  # 忽略无效输入
            if OD:
                try:
                    float_od = round(float(OD), 1)  # 转换为浮点数
                    if 0.0 <= float_od <= 10.0:  # 检查范围
                        METAs.set_data("OverallDifficulty", OD)
                except ValueError:
                    pass  # 忽略无效输入

            #处理META
            METAs.set_data("CircleSize", to_keys)
            version_tag = "[" + str(org_keys) + "To" + str(to_keys) + "S]"
            new_file_path_osu = self.save_files(version_tag, file, METAs)

            METAs_new_lines = METAs.get_new_lines()
            #处理HitObject
            HOBJs = NtoNC_HitObjects.from_lines(HOBJ, org_keys)
            HOBJs_new_lines = HOBJs.get_to_keys_obj_NtoNS(NToNS_array)
            #把METAs_new_lines和HOBJs_new_lines写入文件,如果文件存在则覆盖内容，如果不存在则创建文件并写入
            combined_content = '\n'.join(METAs_new_lines) + '\n' + '\n'.join(HOBJs_new_lines)
            if len(new_file_path_osu.name) > 255:
                new_file_path_osu = new_file_path_osu.parent / (
                        new_file_path_osu.stem[:255 - len(new_file_path_osu.suffix)] + new_file_path_osu.suffix)
            try:
                if os.path.exists(new_file_path_osu):
                    with open(new_file_path_osu, 'w', encoding='utf-8') as f:
                        f.write(combined_content)
                else:
                    with open(new_file_path_osu, 'x', encoding='utf-8') as f:
                        f.write(combined_content)
            except Exception as e:
                print(f"创建文件时发生错误: {e}")

    def Everything_To_N(self, file):
        """
        万物系列
        """
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

            META, HOBJ = osu_file_str_split1(content)
            METAs = MataData(META)
            org_keys = int(METAs.get_data("CircleSize")[0])
            to_keys = self.to_key_value_EV.get()
            OD = self.ui.tk_input_OD.get()
            HP = self.ui.tk_input_HP.get()
            #如果HP和OD不是0.0到10.0的浮点数（包含0和10),则修改，否则不修改
            if HP:
                try:
                    float_hp = round(float(HP), 1)  # 转换为浮点数
                    if 0.0 <= float_hp <= 10.0:  # 检查范围
                        METAs.set_data("HPDrainRate", HP)
                except ValueError:
                    pass  # 忽略无效输入
            if OD:
                try:
                    float_od = round(float(OD), 1)  # 转换为浮点数
                    if 0.0 <= float_od <= 10.0:  # 检查范围
                        METAs.set_data("OverallDifficulty", OD)
                except ValueError:
                    pass  # 忽略无效输入

            #处理META
            METAs.set_data("CircleSize", to_keys)
            if self.EV_jack_or_stream.get() == 1:
                version_tag = "[EtoStream" + str(to_keys) + "K]"
            else:
                version_tag = "[EtoJack" + str(to_keys) + "K]"

            new_file_path_osu = self.save_files(version_tag, file, METAs)
            METAs_new_lines = METAs.get_new_lines()
            #处理HitObject
            HOBJs = NtoNC_HitObjects.from_lines(HOBJ, org_keys)
            start_time = HOBJs.MTX_start_time
            if self.EV_jack_or_stream.get() == 1:
                MTX = generate_matrix_everything_to_stream(start_time.size, self.to_key_value_EV.get(),
                                                           self.density_value_EV.get(), self.noise_value_EV.get())
            else:
                MTX = generate_matrix_everything_to_jack(start_time.size, self.to_key_value_EV.get(),
                                                         self.density_value_EV.get(), self.noise_value_EV.get())
            HOBJs_new_lines = HOBJs.get_to_keys_obj_if_note(MTX)
            #把METAs_new_lines和HOBJs_new_lines写入文件,如果文件存在则覆盖内容，如果不存在则创建文件并写入
            combined_content = '\n'.join(METAs_new_lines) + '\n' + '\n'.join(HOBJs_new_lines)
            if len(new_file_path_osu.name) > 255:
                new_file_path_osu = new_file_path_osu.parent / (
                        new_file_path_osu.stem[:255 - len(new_file_path_osu.suffix)] + new_file_path_osu.suffix)
            try:
                if os.path.exists(new_file_path_osu):
                    with open(new_file_path_osu, 'w', encoding='utf-8') as f:
                        f.write(combined_content)
                else:
                    with open(new_file_path_osu, 'x', encoding='utf-8') as f:
                        f.write(combined_content)
            except Exception as e:
                print(f"创建文件时发生错误: {e}")

    def Jack_World(self, file):
        """
        将谱子转换为NS键
        """
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

            META, HOBJ = osu_file_str_split1(content)
            METAs = MataData(META)
            org_keys = int(METAs.get_data("CircleSize")[0])
            array = [i for i in range(org_keys)]
            OD = self.ui.tk_input_OD.get()
            HP = self.ui.tk_input_HP.get()
            #如果HP和OD不是0.0到10.0的浮点数（包含0和10),则修改，否则不修改
            if HP:
                try:
                    float_hp = round(float(HP), 1)  # 转换为浮点数
                    if 0.0 <= float_hp <= 10.0:  # 检查范围
                        METAs.set_data("HPDrainRate", HP)
                except ValueError:
                    pass  # 忽略无效输入
            if OD:
                try:
                    float_od = round(float(OD), 1)  # 转换为浮点数
                    if 0.0 <= float_od <= 10.0:  # 检查范围
                        METAs.set_data("OverallDifficulty", OD)
                except ValueError:
                    pass  # 忽略无效输入

            #处理META
            version_tag = "[JackWorld]"
            new_file_path_osu = self.save_files(version_tag, file, METAs)
            METAs_new_lines = METAs.get_new_lines()
            #处理HitObject
            HOBJs = NtoNC_HitObjects.from_lines(HOBJ, org_keys)
            if_note = HOBJs.MTX_if_note.copy()
            mask = update_matrix_mask(if_note, self.JW_w_density.get(), self.JW_h_density.get(), self.JW_add.get())
            if_not_in_LN = get_in_LN_position(HOBJs.MTX_hold_time, HOBJs.MTX_start_time, True)
            HOBJs.MTX_if_note = update_matrix(if_note, mask, if_not_in_LN)
            HOBJs_new_lines = HOBJs.get_to_keys_obj_NtoNS(array)
            #把METAs_new_lines和HOBJs_new_lines写入文件,如果文件存在则覆盖内容，如果不存在则创建文件并写入
            combined_content = '\n'.join(METAs_new_lines) + '\n' + '\n'.join(HOBJs_new_lines)
            if len(new_file_path_osu.name) > 255:
                new_file_path_osu = new_file_path_osu.parent / (
                        new_file_path_osu.stem[:255 - len(new_file_path_osu.suffix)] + new_file_path_osu.suffix)
            try:
                if os.path.exists(new_file_path_osu):
                    with open(new_file_path_osu, 'w', encoding='utf-8') as f:
                        f.write(combined_content)
                else:
                    with open(new_file_path_osu, 'x', encoding='utf-8') as f:
                        f.write(combined_content)
            except Exception as e:
                print(f"创建文件时发生错误: {e}")

    def preset_convert(self, file):
        """
        将谱子转换为NC键
        """
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        flag_preset = self.preset_value.get()
        META, HOBJ = osu_file_str_split1(content)
        METAs = MataData(META)
        org_keys = int(METAs.get_data("CircleSize")[0])
        should_process = False
        """ 0：NKDP 
            1：NKDPM
            2：7kto6k
            3：4kdpto10k
            4：4kdpmto10k
            5：6kto10k
            6：7kto10k
            7：4kt6t10
            8：4kt7t10
            9：4kto7k"""
        if flag_preset == 0 or flag_preset == 1:
            should_process = True
        elif flag_preset == 2 or flag_preset == 6:
            if org_keys == 7:
                should_process = True
        elif flag_preset == 3 or flag_preset == 4 or flag_preset == 7 or flag_preset == 8 or flag_preset == 9:
            if org_keys == 4:
                should_process = True
        elif flag_preset == 5:
            if org_keys == 6:
                should_process = True

        if should_process:
            pass

            to_keys = self.to_key_value.get()
            blank = self.blank_value.get()
            interval = self.stap_time.get()
            OD = self.ui.tk_input_OD.get()
            HP = self.ui.tk_input_HP.get()
            #如果HP和OD不是0.0到10.0的浮点数（包含0和10),则修改，否则不修改
            if HP:
                try:
                    float_hp = round(float(HP), 1)  # 转换为浮点数
                    if 0.0 <= float_hp <= 10.0:  # 检查范围
                        METAs.set_data("HPDrainRate", HP)
                except ValueError:
                    pass  # 忽略无效输入
            if OD:
                try:
                    float_od = round(float(OD), 1)  # 转换为浮点数
                    if 0.0 <= float_od <= 10.0:  # 检查范围
                        METAs.set_data("OverallDifficulty", OD)
                except ValueError:
                    pass  # 忽略无效输入

            #处理META
            labels = [f"[{org_keys}KDP]",
                      f"[{org_keys}KDPM]",
                      "[7Kt6KS]",
                      "[4KDPt10K]",
                      "[4KDPMt10K]",
                      "[6Kt10K]",
                      "[7Kt10K]",
                      "[4Kt6t10K]",
                      "[4Kt7t10K]",
                      "[4Kt7K]"
                      ]
            version_tag = labels[flag_preset]
            new_file_path_osu = self.save_files(version_tag, file, METAs)

            beat_time = float(METAs.get_data("beat_time")[0])
            HOBJs_new_lines = ""
            #处理HitObject
            HOBJs = Preset_HitObjects.from_lines(HOBJ, org_keys)
            if flag_preset == 2:  # 7kto6k
                METAs.set_data("CircleSize", 6)
                HOBJs_new_lines = HOBJs.get_to_keys_obj_NtoNS([0, 1, 2, 4, 5, 6])
            if flag_preset == 0:  # NKDP
                METAs.set_data("CircleSize", org_keys * 2)
                array = HOBJs.NKDPTOOL()
                HOBJs_new_lines = HOBJs.get_to_keys_obj_NtoNS(array)
            if flag_preset == 1:  # NKDPM
                METAs.set_data("CircleSize", org_keys * 2)
                array = HOBJs.NKDPMTOOL()
                HOBJs_new_lines = HOBJs.get_to_keys_obj_NtoNS(array)
            if flag_preset == 3:  # 4kdpto10k
                METAs.set_data("CircleSize", 10)
                MTX = HOBJs.preset_convert_MTX(func=HOBJs.fourK_dp_to_10K, beat_time=beat_time)
                HOBJs_new_lines = HOBJs.get_to_keys_obj(MTX)
            if flag_preset == 4:  # 4kdpmto10k
                METAs.set_data("CircleSize", 10)
                MTX = HOBJs.preset_convert_MTX(func=HOBJs.fourK_dpm_to_10K, beat_time=beat_time)
                HOBJs_new_lines = HOBJs.get_to_keys_obj(MTX)
            if flag_preset == 5:  # 6kto10k
                METAs.set_data("CircleSize", 10)
                MTX = HOBJs.preset_convert_MTX(func=HOBJs.sixK_to_10K, beat_time=beat_time)
                HOBJs_new_lines = HOBJs.get_to_keys_obj(MTX)
            if flag_preset == 6:  # 7kto10k
                METAs.set_data("CircleSize", 10)
                MTX = HOBJs.preset_convert_MTX(func=HOBJs.sevenK_to_10K, beat_time=beat_time)
                HOBJs_new_lines = HOBJs.get_to_keys_obj(MTX)
            if flag_preset == 7:  # 4kt6t10
                METAs.set_data("CircleSize", 10)
                MTX = HOBJs.preset_convert_MTX(func=HOBJs.fourK_to6to_10K, beat_time=beat_time)
                HOBJs_new_lines = HOBJs.get_to_keys_obj(MTX)
            if flag_preset == 8:  # 4kt7t10
                METAs.set_data("CircleSize", 10)
                MTX = HOBJs.preset_convert_MTX(func=HOBJs.fourK_to7to_10K, beat_time=beat_time)
                HOBJs_new_lines = HOBJs.get_to_keys_obj(MTX)
            if flag_preset == 9:  # 4kt7
                METAs.set_data("CircleSize", 7)
                MTX = HOBJs.preset_convert_MTX(func=HOBJs.fourK_to7, beat_time=beat_time)
                HOBJs_new_lines = HOBJs.get_to_keys_obj(MTX)


            METAs_new_lines = METAs.get_new_lines()
            #把METAs_new_lines和HOBJs_new_lines写入文件,如果文件存在则覆盖内容，如果不存在则创建文件并写入
            combined_content = '\n'.join(METAs_new_lines) + '\n' + '\n'.join(HOBJs_new_lines)

            if len(new_file_path_osu.name) > 255:
                new_file_path_osu = new_file_path_osu.parent / (
                        new_file_path_osu.stem[:255 - len(new_file_path_osu.suffix)] + new_file_path_osu.suffix)
            try:
                if os.path.exists(new_file_path_osu):
                    with open(new_file_path_osu, 'w', encoding='utf-8') as f:
                        f.write(combined_content)
                else:
                    with open(new_file_path_osu, 'x', encoding='utf-8') as f:
                        f.write(combined_content)
            except Exception as e:
                print(f"创建文件时发生错误: {e}")

    def save_files(self, version_tag, file , METAs):
        if self.if_save_to_org_value.get():
            version = version_tag + METAs.get_data("Version")[0]
            METAs.set_data("Version", version)
            file_name_osu, _, _ = METAs.get_save_file_name()
            return Path(file).parent / file_name_osu

        else:
            # 是否要修改title和artist
            old_title = METAs.get_data("Title")[0] if METAs.get_data("Title")[0] else "Unknown"
            if len(old_title) > 15:
                old_title = old_title[:8] + "..." + old_title[-7:]
            if self.ui.tk_input_title.get().strip():
                METAs.set_data("Title", self.ui.tk_input_title.get().strip())
            if self.ui.tk_input_artist.get().strip():
                METAs.set_data("Artist", self.ui.tk_input_artist.get().strip())
            version = version_tag + old_title + "[" + METAs.get_data("Version")[0] + "]"
            METAs.set_data("Version", version)
            new_file_path = self.ui.tk_input_path.get()
            new_file_path = Path(new_file_path).resolve()
            METAs.set_data("Artist", self.ui.tk_input_artist.get())
            METAs.set_data("Title", self.ui.tk_input_title.get())
            file_name_osu, file_name_audio, file_name_BG = METAs.get_save_file_name()
            old_file_path_audio = Path(file).parent / file_name_audio
            old_file_path_BG = Path(file).parent / file_name_BG

            # 避免文件名重复标签，不使用随机数，直接从title和version中截取
            available_file_names_tag = ''.join([
                old_title[1], str(len(old_title)), version[-1], str(len(version)),
                old_title[-1]
            ])

            file_name_audio = available_file_names_tag + file_name_audio
            file_name_BG = available_file_names_tag + file_name_BG
            METAs.set_data("AudioFilename", file_name_audio)
            METAs.set_data("Background", file_name_BG)

            new_file_path_audio = Path(new_file_path) / file_name_audio
            new_file_path_BG = Path(new_file_path) / file_name_BG

            # 验证new_file_path是否存在，不存在则创建
            if not os.path.exists(new_file_path):
                os.makedirs(new_file_path)

            # 复制音频文件
            try:
                shutil.copy(old_file_path_audio, new_file_path_audio)
            except Exception as e:
                error_message = f"复制音频文件时发生错误: - {e}"
                print(error_message)

            # 复制背景图文件
            try:
                shutil.copy(old_file_path_BG, new_file_path_BG)
            except Exception as e:
                error_message = f"复制背景图文件时发生错误: - {e}"
                print(error_message)

            return Path(new_file_path)/file_name_osu

    def change_language(self):
        if self.language == 'zh':
            self.language = 'en'
        else:
            self.language = 'zh'
        self.update_ui_text()



    def update_ui_text(self):
        # 更新窗口标题
        self.ui.title("krrcream的任意键转换器 " + program_version if self.language == 'zh'
                      else "krrcream's Any Keys Converter " + program_version)
        self.ui.tk_label_About.configure(text="使用说明" if self.language == 'zh' else "Guide")
        # 更新其他控件的文本
        self.ui.tk_label_leb_convert_interval.configure(text="转换速度：" if self.language == 'zh' else "Conv. Speed:")
        self.ui.tk_label_leb_to_key.configure(text="目标键数：" if self.language == 'zh' else "Target Key:")
        self.ui.tk_check_button_if_sifting.configure(text="谱面过滤：" if self.language == 'zh' else "filter:")
        self.ui.tk_check_button_if_del_jack.configure(
            text="处理生成的Jack" if self.language == 'zh' else "Del Gene Jacks")
        self.ui.tk_label_lab_density.configure(text="密  度：" if self.language == 'zh' else "Density:")
        self.ui.tk_label_leb_insert_blank.configure(
            text="插入空列：" if self.language == 'zh' else "Insert Blank:")
        self.ui.tk_label_JW_w_density.configure(text="横向密度：" if self.language == 'zh' else "Horizontal Density:")
        self.ui.tk_label_JW_h_density.configure(text="纵向密度：" if self.language == 'zh' else "Vertical Density:")
        self.ui.tk_label_JW_add.configure(text="Jack纵度：" if self.language == 'zh' else "Jack Verticality:")
        self.ui.tk_label_leb_path.configure(text="路  径：" if self.language == 'zh' else "Path:")
        self.ui.tk_label_leb_title.configure(text="标  题：" if self.language == 'zh' else "Title:")
        self.ui.tk_label_leb_artist.configure(text="艺术家：" if self.language == 'zh' else "Artist:")
        self.ui.tk_check_button_if_save_to_org.configure(
            text="保存到原路径" if self.language == 'zh' else "Save to Original Path")
        self.ui.tk_label_change.configure(text="Language" if self.language == 'zh' else "语言")

        self.ui.tk_label_to_key_E.configure(text="目标键数：" if self.language == 'zh' else "Target Key:")
        self.ui.tk_label_density_E.configure(text="密  度：" if self.language == 'zh' else "Density:")
        self.ui.tk_label_noise_E.configure(text="噪  音：" if self.language == 'zh' else "Noise:")

        # 设置Tab页的标题
        self.ui.tk_tabs_select.tab(0, text="狂风插入" if self.language == 'zh' else "Gale Insrt")
        self.ui.tk_tabs_select.tab(1, text="简单矩阵" if self.language == 'zh' else "Simple MTX")
        self.ui.tk_tabs_select.tab(2, text="万物系列" if self.language == 'zh' else "Evg Series")
        self.ui.tk_tabs_select.tab(3, text="杰克世界" if self.language == 'zh' else "Jack World")
        self.ui.tk_tabs_select.tab(4, text="预  设" if self.language == 'zh' else "Presets")

        self.ui.tk_button_gen_seed_button.configure(text="生成" if self.language == 'zh' else "Generate")
        # 设置复选框和单选按钮的文本
        self.ui.tk_radio_button_EtoStream_sel.configure(
            text="万物化切" if self.language == 'zh' else "To Stream")
        self.ui.tk_radio_button_EtoJACK_sel.configure(
            text="万物化叠" if self.language == 'zh' else "To Jack")
        # 设置描述标签的文本
        self.ui.tk_label_NtoNS_desc1.configure(
            text="NtoNC，简单矩阵转换" if self.language == 'zh' else "NtoNC, simple matrix conversion")
        self.ui.tk_label_NtoNS_desc2.configure(
            text="输入数字的长度为目标键数" if self.language == 'zh' else "The length of the input number is the target key number")
        self.ui.tk_label_NtoNS_desc3.configure(
            text="例如① 0,1,2,4,5,6 是7k删空" if self.language == 'zh' else "e.g.① 0,1,2,4,5,6 is 7k delete space")
        self.ui.tk_label_NtoNS_desc4.configure(
            text="例如② 6,0,1,2,3,4,5,6 将7k的第7轨复制并插入为第一轨变为8k" if self.language == 'zh' else "e.g.② 6,0,1,2,3,4,5,6 insert the 7# colunm to 1#to become 8k")
