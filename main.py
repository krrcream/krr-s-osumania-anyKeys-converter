import os
import random
import shutil
import string
import sys
from functools import partial
from typing import List

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget
import convert_list
import matrix_convert
import windows
from row_of_notes import RowOfNotes
from matadata import MataData


def random_num_add(file_name_str):
    extension = os.path.splitext(file_name_str)[1]
    base_filename = os.path.splitext(file_name_str)[0]
    random_number = str(random.randint(1, 99999)).zfill(5)
    new_filename = f"{base_filename}_{random_number}{extension}"
    return new_filename

def calculatebeat(text_line:List[str]):
    index = 0
    for i, line in enumerate(text_line):
        if line.startswith("[TimingPoints]"):
            index = i + 1
            break
    return text_line[index].split(",")[1]

class my_window(QtWidgets.QMainWindow, windows.Ui_krr_anyKeys_convertor):
    def __init__(self):
        super(my_window, self).__init__()
        # self.resizeMode = Qt.AA_EnableHighDpiScaling
        self.setupUi(self)
        # 允许窗体接受拖拽
        self.setAcceptDrops(True)
        # ————————————————————————————————
        self.loadSettings()  # 加载之前保存的设置
        # ————————————————————————————————
        self.del_jack_lv = 2
        self.del_jack_lv_slider.valueChanged.connect(self.updateDelJackLv)
        self.version_flag = True
        self.versionmod.toggled.connect(self.versionFlagChange)
        self.simple_convert_flag = False
        self.simplecomvertmod.toggled.connect(self.simpleFlagChange)
        self.to4kdpcflag = False
        self.to4kdpc.toggled.connect(self.to4kDPCChange)
        self.toNkNkflag = True
        self.NtoNC.toggled.connect(self.toNkNkCChange)

    # ——————保存内容和下次载入————————
    def loadSettings(self):
        settings = QtCore.QSettings("String.fq", QtCore.QSettings.IniFormat)
        self.lineEdit_savepath.setText(settings.value("savepath", "请输入你的songs目录的一个文件夹(如需更多8K资源，请联系我加QQ群)"))
        self.lineEdit_title.setText(settings.value("title", ""))
        self.lineEdit_artist.setText(settings.value("artist", "V.A"))
        self.stap.setText(settings.value("stap", "16"))
        self.timestap.setText(settings.value("timestap", "1000"))

    def saveSettings(self):
        settings = QtCore.QSettings("String.fq", QtCore.QSettings.IniFormat)
        settings.setValue("savepath", self.lineEdit_savepath.text())
        settings.setValue("title", self.lineEdit_title.text())
        settings.setValue("artist", self.lineEdit_artist.text())
        settings.setValue("stap", self.stap.text())
        settings.setValue("timestap", self.timestap.text())

    def closeEvent(self, event):
        self.saveSettings()  # 在窗口关闭时保存设置
        super(my_window, self).closeEvent(event)  # 调用QMainWindow的closeEvent

    # ——————————————————————

    # 滑块和单选框关联
    def updateDelJackLv(self, value):
        self.del_jack_lv = value

    def versionFlagChange(self, checked):
        self.version_flag = checked

    def simpleFlagChange(self, checked):
        self.simple_convert_flag = checked
        # print(self.simple_convert_flag)
    def to4kDPCChange(self, checked):
        self.to4kdpcflag = checked
        # print(self.to4kdpcflag)
    def toNkNkCChange(self, checked):
        self.toNkNkflag = checked
        # print(self.toNkNkflag)

    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None:
        # 判断有没有接受到内容
        if a0.mimeData().hasUrls():
            # 如果接收到内容了，就把它存在事件中
            a0.accept()
        else:
            # 没接收到内容就忽略
            a0.ignore()

    def dropEvent(self, a0: QtGui.QDropEvent) -> None:
        if a0:
            for i in a0.mimeData().urls():
                # print(i.path())
                file_path = i.path()[1:]
                self.lineEdit.setText(file_path)
        file_path = file_path.replace('\\', '/')
        directory = os.path.dirname(file_path)
        save_path = ""
        title = ""
        artist = ""
        tokeys = 8
        stap = 16
        timestap = 1000
        simple_convert_list = []
        save_path = self.lineEdit_savepath.text()
        title = self.lineEdit_title.text()
        artist = self.lineEdit_artist.text()
        tokeys = int(self.tokeys.text())
        stap = int(self.stap.text())
        timestap = int(self.timestap.text())


        if self.convert_list.text() != "":
            simple_convert_list = [int(num) for num in self.convert_list.text().split(',')]

        # ------------------主程序
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # 查找[TimingPoints]的位置
            hit_objects_position = content.split('[HitObjects]', 1)

            # 提取开始到[HitObjects]之前的内容
            file_metadata = hit_objects_position[0] if hit_objects_position else content

            # 提取[HitObjects]之后的内容

            note_objs = '[HitObjects]' + hit_objects_position[1] if len(hit_objects_position) > 1 else ''

        lines_file_metadata = file_metadata.splitlines()
        lines_note_objs = note_objs.strip().splitlines()

        a_quarter_beat = int((float(calculatebeat(lines_file_metadata))/4))+3
        if a_quarter_beat < 90:
            a_quarter_beat = 90



        lines_file_metadata.append(lines_note_objs.pop(0))

        # 生成matadata以备用
        matadata = MataData(lines_file_metadata)
        # 生成原始列表以备用
        matrix = []
        for line in lines_note_objs:
            matrix.append(RowOfNotes.new_row_from_original_str_line(line, int(matadata.data["CircleSize"][0])))

        # -----------断点测试处-----
        #       matrix = matrix_convert.matrix_merge(matrix)
        #       matrix_convert.print_matrix(matrix)
        #       modified_method = partial(convert_list.to_lowKeys_2_highKeys_addkeys_chaos,
        #                                 keys=int(matadata.data["CircleSize"][0]),
        #                                 add_columns=8 - int(matadata.data["CircleSize"][0]))
        #
        #       matrix = matrix_convert.convert(matrix, modified_method, 16, 1000)
        #       matrix_convert.print_matrix(matrix)
        # ---------------------------

        # _______________判断是几K____________________#
        version_tag = ""
        if self.toNkNkflag == True:
            matadata.meta_alter("CircleSize", tokeys)
            # 操作矩阵，修改convert_list里的的默认参数
            modified_method = partial(convert_list.to_lowKeys_2_highKeys_addkeys_chaos,
                                      keys=int(matadata.data["CircleSize"][0]),
                                      add_columns=tokeys - int(matadata.data["CircleSize"][0]))
            matrix = matrix_convert.matrix_merge(matrix)
            matrix = matrix_convert.convert(matrix, modified_method, stap, timestap, a_quarter_beat, self.del_jack_lv)
            matrix_str = matrix_convert.write_notes(matrix)
            version_tag = f"[{int(matadata.data["CircleSize"][0])}To{tokeys}C]"
        elif self.to4kdpcflag == True and int(matadata.data["CircleSize"][0]) == 4:  # 4kdpchaos
            matadata.meta_alter("CircleSize", tokeys)
            # 操作矩阵
            matrix = matrix_convert.matrix_merge(matrix)
            matrix = matrix_convert.convert(matrix, convert_list.to_4KDPChaos_list, stap, timestap, a_quarter_beat, self.del_jack_lv)
            matrix_str = matrix_convert.write_notes(matrix)
            version_tag = f"[{int(matadata.data["CircleSize"][0])}To8DPC]"
        elif self.simple_convert_flag == True :
            matadata.meta_alter("CircleSize", len(simple_convert_list))
            matrix = matrix_convert.matrix_merge(matrix)
            matrix = matrix_convert.convert(matrix, simple_convert_list, stap, timestap, a_quarter_beat, self.del_jack_lv)
            matrix_str = matrix_convert.write_notes(matrix)
            version_tag = f"[{int(matadata.data["CircleSize"][0])}To{len(simple_convert_list)}S]"

        # ------------------需要复制和创建的的文件------------------------------
        new_audio_file_name = ""
        new_BG_file_name = ""

        def remove_invalid_filename_chars(s):
            valid_chars = "-_.() " + string.ascii_letters + string.digits  # 保留的有效字符
            return "".join([c for c in s if c in valid_chars])

        if not os.path.exists(save_path):
            os.makedirs(save_path)
        old_title = matadata.data["ArtistUnicode"][0]
        new_version = ""
        old_creator = remove_invalid_filename_chars(matadata.data["Creator"][0])
        old_version = remove_invalid_filename_chars(matadata.data["Version"][0])
        audio_file = str(matadata.data["AudioFilename"][0]).lstrip()
        BG_file = str(matadata.data["Background"][0]).lstrip()
        if self.version_flag == False:
            new_version = f"[{old_version}]"
            temp_str1 = random_num_add(title)
            new_audio_file_name = remove_invalid_filename_chars(
                temp_str1 + os.path.splitext(audio_file)[1])
            new_BG_file_name = remove_invalid_filename_chars(
                temp_str1 + os.path.splitext(BG_file)[1])
        elif self.version_flag == True:
            new_version = remove_invalid_filename_chars(matadata.data["TitleUnicode"][0])
            new_version += f"({old_creator})[{old_version}]"
            temp_str2 = random_num_add(matadata.data["TitleUnicode"][0][:10])
            new_audio_file_name = remove_invalid_filename_chars(temp_str2 + os.path.splitext(audio_file)[1])
            new_BG_file_name = remove_invalid_filename_chars(temp_str2 + os.path.splitext(BG_file)[1])
        # --------------------------------
        new_audio_file_name=new_audio_file_name.lstrip()
        new_BG_file_name=new_BG_file_name.lstrip()
        # ____________________________改matadata________________________________________
        matadata.meta_alter("AudioFilename", new_audio_file_name)

        if matadata.data["Background"] != "null":
            matadata.mata_new[matadata.data["Background"][1]] = f"0,0,\"{new_BG_file_name}\",0,0"

        if title != "":
            matadata.meta_alter("TitleUnicode", title)
            matadata.mata_new[matadata.data["TitleUnicode"][1] - 1] = f"Title:{title}"
        if artist != "":
            matadata.meta_alter("ArtistUnicode", artist)
            matadata.mata_new[matadata.data["ArtistUnicode"][1] - 1] = f"Title:{artist}"
        matadata.meta_alter("BeatmapID", 0)
        matadata.meta_alter("BeatmapSetID", -1)

        matadata.meta_alter("Creator", "krrcream")
        matadata.meta_alter("Version", version_tag + new_version)
        # ____________________________写入字符串________________________________________

        lines = matadata.get_new_lines()

        matadata_str = "\n".join(lines)

        # ____________________________生成文件________________________________________
        # print(new_audio_file_name)
        # print(new_BG_file_name)

        old_audio_file_path = os.path.join(directory, audio_file).replace('\\', '/')
        new_audio_file_path = os.path.join(save_path, new_audio_file_name).replace('\\', '/')
        # print(old_audio_file_path)
        # print(new_audio_file_path)
        shutil.copy(old_audio_file_path, new_audio_file_path)

        old_BG_file_path = os.path.join(directory, BG_file).replace('\\', '/')
        new_BG_file_path = os.path.join(save_path, new_BG_file_name).replace('\\', '/')
        # print(old_BG_file_path)
        # print(new_BG_file_path)
        shutil.copy(old_BG_file_path, new_BG_file_path)

        new_osu_file_path = os.path.join(save_path, new_version + ".osu").replace('\\', '/')

        # --------------转谱--------------------
        # 修BUG
        matadata_str = matadata.artist_bug_repair(matadata_str)
        # 生成osu


        name, extension = os.path.splitext(os.path.basename(new_osu_file_path))
        osu_new_name = f"{artist} - {title} (krrcream) [{version_tag + new_version}]"
        new_file_path = os.path.join(os.path.dirname(new_osu_file_path), osu_new_name + extension)

        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(matadata_str + "\n" + matrix_str)

        self.lineEdit.setText(f"成功！ → {new_file_path}")
# ----------------------------------------------------


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
# ----------------
    app = QtWidgets.QApplication(sys.argv)
    window = my_window()
    window.setFixedSize(window.size())
    window.show()
    sys.exit(app.exec_())
# ---------------
