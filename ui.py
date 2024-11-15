"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""
from tkinter import *
from tkinter.ttk import *
from tkinterdnd2 import TkinterDnD, DND_FILES
class WinGUI(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_frame_bottom = self.__tk_frame_bottom(self)
        self.tk_tabs_select = self.__tk_tabs_select( self.tk_frame_bottom)
        self.tk_label_leb_convert_interval = self.__tk_label_leb_convert_interval( self.tk_tabs_select_0)
        self.tk_scale_convert_interval = self.__tk_scale_convert_interval( self.tk_tabs_select_0)
        self.tk_label_leb_to_key = self.__tk_label_leb_to_key( self.tk_tabs_select_0)
        self.tk_scale_to_key_slider = self.__tk_scale_to_key_slider( self.tk_tabs_select_0)
        self.tk_label_step_num = self.__tk_label_step_num( self.tk_tabs_select_0)
        self.tk_label_to_key_num = self.__tk_label_to_key_num( self.tk_tabs_select_0)
        self.tk_frame_container_if_sift = self.__tk_frame_container_if_sift( self.tk_tabs_select_0)
        self.tk_frame_container_sift = self.__tk_frame_container_sift( self.tk_frame_container_if_sift)
        self.tk_check_button_s4k = self.__tk_check_button_s4k( self.tk_frame_container_sift)
        self.tk_check_button_s5k = self.__tk_check_button_s5k( self.tk_frame_container_sift)
        self.tk_check_button_s6k = self.__tk_check_button_s6k( self.tk_frame_container_sift)
        self.tk_check_button_s7k = self.__tk_check_button_s7k( self.tk_frame_container_sift)
        self.tk_check_button_s8k = self.__tk_check_button_s8k( self.tk_frame_container_sift)
        self.tk_check_button_s9k = self.__tk_check_button_s9k( self.tk_frame_container_sift)
        self.tk_check_button_s10k = self.__tk_check_button_s10k( self.tk_frame_container_sift)
        self.tk_check_button_s10pk = self.__tk_check_button_s10pk( self.tk_frame_container_sift)
        self.tk_check_button_s4mk = self.__tk_check_button_s4mk( self.tk_frame_container_sift)
        self.tk_check_button_if_sifting = self.__tk_check_button_if_sifting( self.tk_frame_container_if_sift)
        self.tk_frame_container_2 = self.__tk_frame_container_2( self.tk_tabs_select_0)
        self.tk_check_button_if_del_jack = self.__tk_check_button_if_del_jack( self.tk_frame_container_2)
        self.tk_label_lab_density = self.__tk_label_lab_density( self.tk_tabs_select_0)
        self.tk_label_density_value = self.__tk_label_density_value( self.tk_tabs_select_0)
        self.tk_scale_density_slider = self.__tk_scale_density_slider( self.tk_tabs_select_0)
        self.tk_frame_NtoNS_container = self.__tk_frame_NtoNS_container( self.tk_tabs_select_1)
        self.tk_input_NToNS_num_line = self.__tk_input_NToNS_num_line( self.tk_frame_NtoNS_container)
        self.tk_label_frame_NtoNS_desc = self.__tk_label_frame_NtoNS_desc( self.tk_frame_NtoNS_container)
        self.tk_label_NtoNS_desc1 = self.__tk_label_NtoNS_desc1( self.tk_label_frame_NtoNS_desc)
        self.tk_label_NtoNS_desc2 = self.__tk_label_NtoNS_desc2( self.tk_label_frame_NtoNS_desc)
        self.tk_label_NtoNS_desc3 = self.__tk_label_NtoNS_desc3( self.tk_label_frame_NtoNS_desc)
        self.tk_label_NtoNS_desc4 = self.__tk_label_NtoNS_desc4( self.tk_label_frame_NtoNS_desc)
        self.tk_frame_every_container = self.__tk_frame_every_container( self.tk_tabs_select_2)
        self.tk_frame_to_key_e_container = self.__tk_frame_to_key_e_container( self.tk_frame_every_container)
        self.tk_scale_EV_to_key = self.__tk_scale_EV_to_key( self.tk_frame_to_key_e_container)
        self.tk_label_to_key_E = self.__tk_label_to_key_E( self.tk_frame_to_key_e_container)
        self.tk_label_lab_EV_to_key = self.__tk_label_lab_EV_to_key( self.tk_frame_to_key_e_container)
        self.tk_frame_EtoE_container_1 = self.__tk_frame_EtoE_container_1( self.tk_frame_every_container)
        self.tk_radio_button_EtoStream_sel = self.__tk_radio_button_EtoStream_sel( self.tk_frame_EtoE_container_1)
        self.tk_radio_button_EtoJACK_sel = self.__tk_radio_button_EtoJACK_sel( self.tk_frame_EtoE_container_1)
        self.tk_frame_fixed_mod_container_out = self.__tk_frame_fixed_mod_container_out( self.tk_frame_every_container)
        self.tk_frame_m2rcsumz = self.__tk_frame_m2rcsumz( self.tk_frame_every_container)
        self.tk_scale_EV_density = self.__tk_scale_EV_density( self.tk_frame_m2rcsumz)
        self.tk_label_density_E = self.__tk_label_density_E( self.tk_frame_m2rcsumz)
        self.tk_label_Lab_EV_density = self.__tk_label_Lab_EV_density( self.tk_frame_m2rcsumz)
        self.tk_frame_m2rdgj1p = self.__tk_frame_m2rdgj1p( self.tk_frame_every_container)
        self.tk_scale_EV_noise = self.__tk_scale_EV_noise( self.tk_frame_m2rdgj1p)
        self.tk_label_noise_E = self.__tk_label_noise_E( self.tk_frame_m2rdgj1p)
        self.tk_label_Lab_EV_noise = self.__tk_label_Lab_EV_noise( self.tk_frame_m2rdgj1p)
        self.tk_label_JW_w_density = self.__tk_label_JW_w_density( self.tk_tabs_select_3)
        self.tk_label_JW_h_density = self.__tk_label_JW_h_density( self.tk_tabs_select_3)
        self.tk_scale_JW_w_density_slider = self.__tk_scale_JW_w_density_slider( self.tk_tabs_select_3)
        self.tk_scale_JW_h_density_slider = self.__tk_scale_JW_h_density_slider( self.tk_tabs_select_3)
        self.tk_label_JW_w_lab = self.__tk_label_JW_w_lab( self.tk_tabs_select_3)
        self.tk_label_JW_h_lab = self.__tk_label_JW_h_lab( self.tk_tabs_select_3)
        self.tk_label_leb_insert_blank = self.__tk_label_leb_insert_blank( self.tk_tabs_select_0)
        self.tk_label_insert_blank_num = self.__tk_label_insert_blank_num( self.tk_tabs_select_0)
        self.tk_scale_insert_blank_slider = self.__tk_scale_insert_blank_slider( self.tk_tabs_select_0)
        self.tk_label_JW_add = self.__tk_label_JW_add( self.tk_tabs_select_3)
        self.tk_label_JW_add_lab = self.__tk_label_JW_add_lab( self.tk_tabs_select_3)
        self.tk_scale_JW_add_slider = self.__tk_scale_JW_add_slider( self.tk_tabs_select_3)
        self.tk_frame_preset_container = self.__tk_frame_preset_container( self.tk_tabs_select_4)
        self.tk_radio_button_preset_NKDP = self.__tk_radio_button_preset_NKDP( self.tk_frame_preset_container)
        self.tk_radio_button_preset_NKDPM = self.__tk_radio_button_preset_NKDPM( self.tk_frame_preset_container)
        self.tk_radio_button_preset_4kdpto10k = self.__tk_radio_button_preset_4kdpto10k( self.tk_frame_preset_container)
        self.tk_radio_button_preset_6kto10k = self.__tk_radio_button_preset_6kto10k( self.tk_frame_preset_container)
        self.tk_radio_button_preset_7kto10k = self.__tk_radio_button_preset_7kto10k( self.tk_frame_preset_container)
        self.tk_radio_button_preset_7kto6k = self.__tk_radio_button_preset_7kto6k( self.tk_frame_preset_container)
        self.tk_radio_button_preset_4kdpmto10k = self.__tk_radio_button_preset_4kdpmto10k( self.tk_frame_preset_container)
        self.tk_radio_button_preset_4kt6t10 = self.__tk_radio_button_preset_4kt6t10( self.tk_frame_preset_container)
        self.tk_radio_button_preset_4kt7t10 = self.__tk_radio_button_preset_4kt7t10( self.tk_frame_preset_container)
        self.tk_radio_button_preset_4kto7k = self.__tk_radio_button_preset_4kto7k( self.tk_frame_preset_container)
        self.tk_frame_container_1 = self.__tk_frame_container_1( self.tk_frame_bottom)
        self.tk_input_path = self.__tk_input_path( self.tk_frame_container_1)
        self.tk_label_leb_path = self.__tk_label_leb_path( self.tk_frame_container_1)
        self.tk_label_leb_title = self.__tk_label_leb_title( self.tk_frame_container_1)
        self.tk_input_artist = self.__tk_input_artist( self.tk_frame_container_1)
        self.tk_label_leb_artist = self.__tk_label_leb_artist( self.tk_frame_container_1)
        self.tk_button_gen_seed_button = self.__tk_button_gen_seed_button( self.tk_frame_container_1)
        self.tk_input_seed_line = self.__tk_input_seed_line( self.tk_frame_container_1)
        self.tk_label_leb_HP = self.__tk_label_leb_HP( self.tk_frame_container_1)
        self.tk_label_leb_OD = self.__tk_label_leb_OD( self.tk_frame_container_1)
        self.tk_input_HP = self.__tk_input_HP( self.tk_frame_container_1)
        self.tk_input_OD = self.__tk_input_OD( self.tk_frame_container_1)
        self.tk_input_title = self.__tk_input_title( self.tk_frame_container_1)
        self.tk_check_button_if_use_seed = self.__tk_check_button_if_use_seed( self.tk_frame_container_1)
        self.tk_check_button_if_save_to_org = self.__tk_check_button_if_save_to_org( self.tk_frame_container_1)
        self.tk_frame_right_line = self.__tk_frame_right_line(self)
        self.tk_label_rights_line = self.__tk_label_rights_line( self.tk_frame_right_line)
        self.tk_label_About = self.__tk_label_About( self.tk_frame_right_line)
        self.tk_label_change = self.__tk_label_change( self.tk_frame_right_line)
    def __win(self):
        self.title("krrcream的任意keys转换器")
        # 设置窗口大小、居中
        width = 440
        height = 523
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.minsize(width=width, height=height)

    def scrollbar_autohide(self,vbar, hbar, widget):
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

    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_frame_bottom(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0045, rely=0.0038, relwidth=0.9841, relheight=0.9962)
        return frame
    def __tk_tabs_select(self,parent):
        frame = Notebook(parent)
        self.tk_tabs_select_0 = self.__tk_frame_select_0(frame)
        frame.add(self.tk_tabs_select_0, text="狂风插入")
        self.tk_tabs_select_1 = self.__tk_frame_select_1(frame)
        frame.add(self.tk_tabs_select_1, text="简单矩阵")
        self.tk_tabs_select_2 = self.__tk_frame_select_2(frame)
        frame.add(self.tk_tabs_select_2, text="万物系列")
        self.tk_tabs_select_3 = self.__tk_frame_select_3(frame)
        frame.add(self.tk_tabs_select_3, text="杰克世界")
        self.tk_tabs_select_4 = self.__tk_frame_select_4(frame)
        frame.add(self.tk_tabs_select_4, text="预设方法")
        frame.place(relx=0.0023, rely=0.4069, relwidth=0.9954, relheight=0.5259)
        return frame
    def __tk_frame_select_0(self,parent):
        frame = Frame(parent)
        frame.place(relx=0.0023, rely=0.4069, relwidth=0.9954, relheight=0.5259)
        return frame
    def __tk_frame_select_1(self,parent):
        frame = Frame(parent)
        frame.place(relx=0.0023, rely=0.4069, relwidth=0.9954, relheight=0.5259)
        return frame
    def __tk_frame_select_2(self,parent):
        frame = Frame(parent)
        frame.place(relx=0.0023, rely=0.4069, relwidth=0.9954, relheight=0.5259)
        return frame
    def __tk_frame_select_3(self,parent):
        frame = Frame(parent)
        frame.place(relx=0.0023, rely=0.4069, relwidth=0.9954, relheight=0.5259)
        return frame
    def __tk_frame_select_4(self,parent):
        frame = Frame(parent)
        frame.place(relx=0.0023, rely=0.4069, relwidth=0.9954, relheight=0.5259)
        return frame
    def __tk_label_leb_convert_interval(self,parent):
        label = Label(parent,text="转换速度：",anchor="center", )
        label.place(relx=0.0000, rely=0.0146, relwidth=0.2111, relheight=0.1095)
        return label
    def __tk_scale_convert_interval(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.3480, rely=0.0146, relwidth=0.5800, relheight=0.1095)
        return scale
    def __tk_label_leb_to_key(self,parent):
        label = Label(parent,text="目标键数：",anchor="center", )
        label.place(relx=0.0000, rely=0.1350, relwidth=0.2111, relheight=0.1095)
        return label
    def __tk_scale_to_key_slider(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.3480, rely=0.1350, relwidth=0.5800, relheight=0.1095)
        return scale
    def __tk_label_step_num(self,parent):
        label = Label(parent,text="15",anchor="center", )
        label.place(relx=0.2181, rely=0.0146, relwidth=0.1160, relheight=0.1095)
        return label
    def __tk_label_to_key_num(self,parent):
        label = Label(parent,text="10",anchor="center", )
        label.place(relx=0.2181, rely=0.1350, relwidth=0.1160, relheight=0.1095)
        return label
    def __tk_frame_container_if_sift(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.6387, relwidth=0.9977, relheight=0.2737)
        return frame
    def __tk_frame_container_sift(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.3512, rely=0.0000, relwidth=0.5837, relheight=0.8667)
        return frame
    def __tk_check_button_s4k(self,parent):
        cb = Checkbutton(parent,text="4K",)
        cb.place(relx=0.0000, rely=0.0000, relwidth=0.1753, relheight=0.4615)
        return cb
    def __tk_check_button_s5k(self,parent):
        cb = Checkbutton(parent,text="5K",)
        cb.place(relx=0.1992, rely=0.0000, relwidth=0.1753, relheight=0.4615)
        return cb
    def __tk_check_button_s6k(self,parent):
        cb = Checkbutton(parent,text="6K",)
        cb.place(relx=0.3984, rely=0.0000, relwidth=0.1753, relheight=0.4615)
        return cb
    def __tk_check_button_s7k(self,parent):
        cb = Checkbutton(parent,text="7K",)
        cb.place(relx=0.5976, rely=0.0000, relwidth=0.1753, relheight=0.4615)
        return cb
    def __tk_check_button_s8k(self,parent):
        cb = Checkbutton(parent,text="8K",)
        cb.place(relx=0.7968, rely=0.0000, relwidth=0.1753, relheight=0.4615)
        return cb
    def __tk_check_button_s9k(self,parent):
        cb = Checkbutton(parent,text="9K",)
        cb.place(relx=0.0000, rely=0.5077, relwidth=0.1753, relheight=0.4615)
        return cb
    def __tk_check_button_s10k(self,parent):
        cb = Checkbutton(parent,text="10K",)
        cb.place(relx=0.1992, rely=0.5077, relwidth=0.1753, relheight=0.4615)
        return cb
    def __tk_check_button_s10pk(self,parent):
        cb = Checkbutton(parent,text="10+K",)
        cb.place(relx=0.3984, rely=0.5077, relwidth=0.2590, relheight=0.4615)
        return cb
    def __tk_check_button_s4mk(self,parent):
        cb = Checkbutton(parent,text="4-k",)
        cb.place(relx=0.7012, rely=0.5077, relwidth=0.2590, relheight=0.4615)
        return cb
    def __tk_check_button_if_sifting(self,parent):
        cb = Checkbutton(parent,text="元 谱 筛 选：",)
        cb.place(relx=0.0070, rely=0.2000, relwidth=0.2465, relheight=0.4000)
        return cb
    def __tk_frame_container_2(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.5073, relwidth=0.9838, relheight=0.1095)
        return frame
    def __tk_check_button_if_del_jack(self,parent):
        cb = Checkbutton(parent,text="处理生成的子弹",)
        cb.place(relx=0.0047, rely=0.0000, relwidth=0.2972, relheight=1.0000)
        return cb
    def __tk_label_lab_density(self,parent):
        label = Label(parent,text="  密    度：",anchor="center", )
        label.place(relx=0.0000, rely=0.3759, relwidth=0.2111, relheight=0.1095)
        return label
    def __tk_label_density_value(self,parent):
        label = Label(parent,text="10",anchor="center", )
        label.place(relx=0.2181, rely=0.3759, relwidth=0.1160, relheight=0.1095)
        return label
    def __tk_scale_density_slider(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.3480, rely=0.3759, relwidth=0.5800, relheight=0.1095)
        return scale
    def __tk_frame_NtoNS_container(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.0000, relwidth=0.9907, relheight=0.7737)
        return frame
    def __tk_input_NToNS_num_line(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.0187, rely=0.0472, relwidth=0.9649, relheight=0.1415)
        return ipt
    def __tk_label_frame_NtoNS_desc(self,parent):
        frame = LabelFrame(parent,text="",)
        frame.place(relx=0.0000, rely=0.2217, relwidth=0.9859, relheight=0.7830)
        return frame
    def __tk_label_NtoNS_desc1(self,parent):
        label = Label(parent,text="NtoNC，简单矩阵转换",anchor="center", )
        label.place(relx=0.0000, rely=0.0000, relwidth=0.9667, relheight=0.1928)
        return label
    def __tk_label_NtoNS_desc2(self,parent):
        label = Label(parent,text="输入数字的长度为目标keys数",anchor="center", )
        label.place(relx=0.0000, rely=0.2048, relwidth=0.9667, relheight=0.1928)
        return label
    def __tk_label_NtoNS_desc3(self,parent):
        label = Label(parent,text="e.g.① 0,1,2,4,5,6 是7k删除空",anchor="center", )
        label.place(relx=0.0000, rely=0.4096, relwidth=0.9667, relheight=0.1928)
        return label
    def __tk_label_NtoNS_desc4(self,parent):
        label = Label(parent,text="e.g.② 6,0,1,2,3,4,5,6 把7k的第7个轨道复制并插入到第一轨道成为8k",anchor="center", )
        label.place(relx=0.0000, rely=0.6145, relwidth=0.9667, relheight=0.1928)
        return label
    def __tk_frame_every_container(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.0146, relwidth=0.9907, relheight=0.9015)
        return frame
    def __tk_frame_to_key_e_container(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.1457, relwidth=0.9930, relheight=0.1336)
        return frame
    def __tk_scale_EV_to_key(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.4175, rely=0.0000, relwidth=0.5660, relheight=0.9091)
        return scale
    def __tk_label_to_key_E(self,parent):
        label = Label(parent,text="目标键数：",anchor="center", )
        label.place(relx=0.0142, rely=0.0000, relwidth=0.2146, relheight=0.9091)
        return label
    def __tk_label_lab_EV_to_key(self,parent):
        label = Label(parent,text="10",anchor="center", )
        label.place(relx=0.2547, rely=0.0000, relwidth=0.0825, relheight=0.9091)
        return label
    def __tk_frame_EtoE_container_1(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.0000, relwidth=1.0000, relheight=0.1255)
        return frame
    def __tk_radio_button_EtoStream_sel(self,parent):
        rb = Radiobutton(parent,text="万物化切",)
        rb.place(relx=0.5199, rely=0.0000, relwidth=0.2693, relheight=0.9677)
        return rb
    def __tk_radio_button_EtoJACK_sel(self,parent):
        rb = Radiobutton(parent,text="万物化叠",)
        rb.place(relx=0.0609, rely=0.0000, relwidth=0.2693, relheight=0.9677)
        return rb
    def __tk_frame_fixed_mod_container_out(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0070, rely=0.6194, relwidth=0.9930, relheight=0.3806)
        return frame
    def __tk_frame_m2rcsumz(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.2955, relwidth=0.9930, relheight=0.1336)
        return frame
    def __tk_scale_EV_density(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.4175, rely=0.0000, relwidth=0.5660, relheight=0.9091)
        return scale
    def __tk_label_density_E(self,parent):
        label = Label(parent,text="密   度：",anchor="center", )
        label.place(relx=0.0142, rely=0.0000, relwidth=0.2146, relheight=0.9091)
        return label
    def __tk_label_Lab_EV_density(self,parent):
        label = Label(parent,text="2",anchor="center", )
        label.place(relx=0.2547, rely=0.0000, relwidth=0.0825, relheight=0.9091)
        return label
    def __tk_frame_m2rdgj1p(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.4413, relwidth=0.9930, relheight=0.1336)
        return frame
    def __tk_scale_EV_noise(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.4175, rely=0.0000, relwidth=0.5660, relheight=0.9091)
        return scale
    def __tk_label_noise_E(self,parent):
        label = Label(parent,text="噪  音：",anchor="center", )
        label.place(relx=0.0142, rely=0.0000, relwidth=0.2146, relheight=0.9091)
        return label
    def __tk_label_Lab_EV_noise(self,parent):
        label = Label(parent,text="0.0",anchor="center", )
        label.place(relx=0.2547, rely=0.0000, relwidth=0.0825, relheight=0.9091)
        return label
    def __tk_label_JW_w_density(self,parent):
        label = Label(parent,text="横向密度:",anchor="center", )
        label.place(relx=0.0139, rely=0.0109, relwidth=0.2111, relheight=0.1095)
        return label
    def __tk_label_JW_h_density(self,parent):
        label = Label(parent,text="竖向密度:",anchor="center", )
        label.place(relx=0.0139, rely=0.1460, relwidth=0.2111, relheight=0.1095)
        return label
    def __tk_scale_JW_w_density_slider(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.3480, rely=0.0109, relwidth=0.5940, relheight=0.1095)
        return scale
    def __tk_scale_JW_h_density_slider(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.3480, rely=0.1460, relwidth=0.5940, relheight=0.1095)
        return scale
    def __tk_label_JW_w_lab(self,parent):
        label = Label(parent,text="0",anchor="center", )
        label.place(relx=0.2436, rely=0.0109, relwidth=0.0812, relheight=0.1095)
        return label
    def __tk_label_JW_h_lab(self,parent):
        label = Label(parent,text="0.2",anchor="center", )
        label.place(relx=0.2436, rely=0.1460, relwidth=0.0812, relheight=0.1095)
        return label
    def __tk_label_leb_insert_blank(self,parent):
        label = Label(parent,text="插入空列：",anchor="center", )
        label.place(relx=0.0000, rely=0.2555, relwidth=0.2111, relheight=0.1095)
        return label
    def __tk_label_insert_blank_num(self,parent):
        label = Label(parent,text="0",anchor="center", )
        label.place(relx=0.2181, rely=0.2555, relwidth=0.1160, relheight=0.1095)
        return label
    def __tk_scale_insert_blank_slider(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.3480, rely=0.2555, relwidth=0.5800, relheight=0.1095)
        return scale
    def __tk_label_JW_add(self,parent):
        label = Label(parent,text="Jack纵度:",anchor="center", )
        label.place(relx=0.0139, rely=0.2737, relwidth=0.2111, relheight=0.1095)
        return label
    def __tk_label_JW_add_lab(self,parent):
        label = Label(parent,text="2",anchor="center", )
        label.place(relx=0.2436, rely=0.2737, relwidth=0.0812, relheight=0.1095)
        return label
    def __tk_scale_JW_add_slider(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(relx=0.3480, rely=0.2737, relwidth=0.5940, relheight=0.1095)
        return scale
    def __tk_frame_preset_container(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.0000, relwidth=0.9930, relheight=0.9051)
        return frame
    def __tk_radio_button_preset_NKDP(self,parent):
        rb = Radiobutton(parent,text="NKDP tool",)
        rb.place(relx=0.0280, rely=0.0484, relwidth=0.2921, relheight=0.1210)
        return rb
    def __tk_radio_button_preset_NKDPM(self,parent):
        rb = Radiobutton(parent,text="NKDP Mirror tool",)
        rb.place(relx=0.3388, rely=0.0484, relwidth=0.3178, relheight=0.1210)
        return rb
    def __tk_radio_button_preset_4kdpto10k(self,parent):
        rb = Radiobutton(parent,text="4KDP To 10K (2Blank)",)
        rb.place(relx=0.0280, rely=0.1935, relwidth=0.4346, relheight=0.1210)
        return rb
    def __tk_radio_button_preset_6kto10k(self,parent):
        rb = Radiobutton(parent,text="6K To 10K (4Blank)",)
        rb.place(relx=0.0280, rely=0.3347, relwidth=0.3972, relheight=0.1210)
        return rb
    def __tk_radio_button_preset_7kto10k(self,parent):
        rb = Radiobutton(parent,text="7K To 10K (2Blank reduce pinky)",)
        rb.place(relx=0.0280, rely=0.4758, relwidth=0.5748, relheight=0.1210)
        return rb
    def __tk_radio_button_preset_7kto6k(self,parent):
        rb = Radiobutton(parent,text="7K DelS To 6K",)
        rb.place(relx=0.6729, rely=0.0484, relwidth=0.2921, relheight=0.1210)
        return rb
    def __tk_radio_button_preset_4kdpmto10k(self,parent):
        rb = Radiobutton(parent,text="4KDPM To 10K (2Blank)",)
        rb.place(relx=0.4907, rely=0.1935, relwidth=0.4369, relheight=0.1210)
        return rb
    def __tk_radio_button_preset_4kt6t10(self,parent):
        rb = Radiobutton(parent,text="4K To6To 10K (4Blank)",)
        rb.place(relx=0.5304, rely=0.3347, relwidth=0.3972, relheight=0.1210)
        return rb
    def __tk_radio_button_preset_4kt7t10(self,parent):
        rb = Radiobutton(parent,text="4K To7To 10K (3Blank reduce pinky)",)
        rb.place(relx=0.0280, rely=0.6169, relwidth=0.6215, relheight=0.1210)
        return rb
    def __tk_radio_button_preset_4kto7k(self,parent):
        rb = Radiobutton(parent,text="4K To 7K ",)
        rb.place(relx=0.6355, rely=0.4758, relwidth=0.2874, relheight=0.1210)
        return rb
    def __tk_frame_container_1(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.0000, relwidth=0.9931, relheight=0.4012)
        return frame
    def __tk_input_path(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.2023, rely=0.0478, relwidth=0.7907, relheight=0.1435)
        return ipt
    def __tk_label_leb_path(self,parent):
        label = Label(parent,text="路    径：",anchor="center", )
        label.place(relx=0.0116, rely=0.0478, relwidth=0.1791, relheight=0.1435)
        return label
    def __tk_label_leb_title(self,parent):
        label = Label(parent,text="标  题：",anchor="center", )
        label.place(relx=0.0116, rely=0.4306, relwidth=0.1791, relheight=0.1435)
        return label
    def __tk_input_artist(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.2023, rely=0.2392, relwidth=0.7907, relheight=0.1435)
        return ipt
    def __tk_label_leb_artist(self,parent):
        label = Label(parent,text="艺术家：",anchor="center", )
        label.place(relx=0.0116, rely=0.2392, relwidth=0.1791, relheight=0.1435)
        return label
    def __tk_button_gen_seed_button(self,parent):
        btn = Button(parent, text="生成", takefocus=False,)
        btn.place(relx=0.1651, rely=0.8134, relwidth=0.1628, relheight=0.1435)
        return btn
    def __tk_input_seed_line(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.3558, rely=0.8134, relwidth=0.6279, relheight=0.1435)
        return ipt
    def __tk_label_leb_HP(self,parent):
        label = Label(parent,text="HP",anchor="center", )
        label.place(relx=0.7163, rely=0.6220, relwidth=0.1279, relheight=0.1435)
        return label
    def __tk_label_leb_OD(self,parent):
        label = Label(parent,text="OD",anchor="center", )
        label.place(relx=0.3674, rely=0.6220, relwidth=0.1279, relheight=0.1435)
        return label
    def __tk_input_HP(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.8558, rely=0.6220, relwidth=0.1279, relheight=0.1435)
        return ipt
    def __tk_input_OD(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.5070, rely=0.6220, relwidth=0.1279, relheight=0.1435)
        return ipt
    def __tk_input_title(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.2023, rely=0.4306, relwidth=0.7907, relheight=0.1435)
        return ipt
    def __tk_check_button_if_use_seed(self,parent):
        cb = Checkbutton(parent,text="Seed",)
        cb.place(relx=0.0047, rely=0.8134, relwidth=0.1535, relheight=0.1435)
        return cb
    def __tk_check_button_if_save_to_org(self,parent):
        cb = Checkbutton(parent,text="保存到原始路径",)
        cb.place(relx=0.0093, rely=0.6268, relwidth=0.3372, relheight=0.1435)
        return cb
    def __tk_frame_right_line(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.0000, rely=0.9426, relwidth=0.9841, relheight=0.0574)
        return frame
    def __tk_label_rights_line(self,parent):
        label = Label(parent,text="© Copyright 2024 krrcream All Rights Reserved",anchor="center", )
        label.place(relx=0.0069, rely=0.0000, relwidth=0.6582, relheight=0.7667)
        return label
    def __tk_label_About(self,parent):
        label = Label(parent,text="说明",anchor="center", )
        label.place(relx=0.6790, rely=0.0000, relwidth=0.1432, relheight=0.7333)
        return label
    def __tk_label_change(self,parent):
        label = Label(parent,text="Language",anchor="center", )
        label.place(relx=0.8360, rely=0.0000, relwidth=0.1478, relheight=0.7667)
        return label
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_gen_seed_button.bind('<Button-1>',self.ctl.gen_seed)
        self.drop_target_register(DND_FILES)  # 注册拖拽目标
        self.dnd_bind('<<Drop>>', self.ctl.on_drop)  # 绑定拖拽事件

    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()