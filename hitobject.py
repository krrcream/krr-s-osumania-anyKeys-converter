"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""

from functions import *

class a_HitObject:
    def __init__(self, colunm, start_time, if_ln=1, hold_time=0, hs=":0:0:0:"):
        self.colunm = colunm
        self.start_time = start_time
        self.if_ln = if_ln
        self.hold_time = hold_time
        self.hs = hs

    @property
    def colunm(self):
        return self._colunm

    @colunm.setter
    def colunm(self, value):
        self._colunm = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def if_ln(self):
        return self._if_ln

    @if_ln.setter
    def if_ln(self, value):
        self._if_ln = value

    @property
    def hold_time(self):
        return self._hold_time

    @hold_time.setter
    def hold_time(self, value):
        self._hold_time = value

    @property
    def hs(self):
        return self._hs

    @hs.setter
    def hs(self, value):
        self._hs = value

    @classmethod
    def obj_from_line(cls, line):
        # 如果line是空行或者无法按逗号分割成6部分则不生成a_HitObject实例
        if not line:
            return None
        park = line.split(",")
        colunm = int(float(park[0]))
        start_time = round(float(park[2]))
        if_ln = int(park[3])

        # hs是park[5]第一个冒号及冒号之后的字符串
        # 若park[5]中没有冒号，则hs为":0:0:0:"

        if len(park) > 5 and ':' in park[5]:
            hs = ":" + park[5][park[5].find(":") + 1:]
            hold_time = int(float(park[5].split(":")[0]))
        else:
            hs = ":0:0:0:"
            hold_time = 0
        return cls(colunm, start_time, if_ln, hold_time, hs)

    def print_obj(self):
        temp = f"{self.colunm},192,{self.start_time},{self.if_ln},0,{self.hold_time}{self.hs}"
        # print(temp)
        return temp


class HitObjects:
    def __init__(self, MTX_if_note=None, MTX_start_time=None, MTX_if_ln=None, MTX_hold_time=None, MTX_hs=None, keys=7):
        self.keys = keys
        self.MTX_if_note = MTX_if_note if MTX_if_note is not None else np.zeros((0, keys), dtype=int)
        self.MTX_start_time = MTX_start_time if MTX_start_time is not None else np.zeros(0, dtype=int)
        self.MTX_if_ln = MTX_if_ln if MTX_if_ln is not None else np.ones((0, keys), dtype=int)
        self.MTX_hold_time = MTX_hold_time if MTX_hold_time is not None else np.zeros((0, keys), dtype=int)
        self.MTX_hs = MTX_hs if MTX_hs is not None else np.zeros((0, keys), dtype=object)

    # Getter and Setter for MTX_if_note
    @property
    def MTX_if_note(self):
        return self._MTX_if_note

    @MTX_if_note.setter
    def MTX_if_note(self, value):
        self._MTX_if_note = value

    # Getter and Setter for MTX_start_time
    @property
    def MTX_start_time(self):
        return self._MTX_start_time

    @MTX_start_time.setter
    def MTX_start_time(self, value):
        self._MTX_start_time = value

    # Getter and Setter for MTX_if_ln
    @property
    def MTX_if_ln(self):
        return self._MTX_if_ln

    @MTX_if_ln.setter
    def MTX_if_ln(self, value):
        self._MTX_if_ln = value

    # Getter and Setter for MTX_hold_time
    @property
    def MTX_hold_time(self):
        return self._MTX_hold_time

    @MTX_hold_time.setter
    def MTX_hold_time(self, value):
        self._MTX_hold_time = value

    # Getter and Setter for MTX_hs
    @property
    def MTX_hs(self):
        return self._MTX_hs

    @MTX_hs.setter
    def MTX_hs(self, value):
        self._MTX_hs = value


    @property
    def keys(self):
        return self._keys

    @keys.setter
    def keys(self, value):
        self._keys = value



    # 方法用于获取和设置二维矩阵中的特定元素
    def get_matrix_value(self, matrix_name, row, col):
        matrix = getattr(self, matrix_name)
        if 0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]:
            return matrix[row, col]
        else:
            raise IndexError("Index out of range")

    def set_matrix_value(self, matrix_name, row, col, value):
        matrix = getattr(self, matrix_name)
        if 0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]:
            matrix[row, col] = value
        else:
            raise IndexError("Index out of range")

    @classmethod
    def from_lines(cls, lines, keys=7):
        # print(lines)
        obj = []
        MTX_if_note = []
        MTX_start_time = []
        MTX_if_ln = []
        MTX_hold_time = []
        MTX_hs = []
        for line in lines:
            # 如果a_HitObject.obj_from_line(line)是hitobject.a_HitObject类，那么令temp = a_HitObject.obj_from_line(line)
            temp = a_HitObject.obj_from_line(line)
            if isinstance(temp, a_HitObject):
                obj.append(temp)

        # 初初始化长度为7的临时列表
        for note in obj:
            # 如果note为"",则跳过
            if note == "":
                continue
            MTX_start_time.append(int(float(note.start_time)))
            # 生成一个全部是0，长度为7的普通列表
            MTX_if_note.append([0] * int(keys))
            MTX_if_ln.append([1] * int(keys))
            MTX_hold_time.append([0] * int(keys))
            MTX_hs.append([0] * int(keys))  # 使用 None 替代对象数组
            index = int(key_value_to_colunm(int(float(note.colunm)), int(keys)))
            MTX_if_note[-1][index] = 1
            MTX_if_ln[-1][index] = int(float(note.if_ln))
            MTX_hold_time[-1][index] = int(float(note.hold_time))
            MTX_hs[-1][index] = note.hs

        # 转换为numpy数组
        MTX_if_note = np.array(MTX_if_note)
        MTX_start_time = np.array(MTX_start_time)
        MTX_if_ln = np.array(MTX_if_ln)
        MTX_hold_time = np.array(MTX_hold_time)
        MTX_hs = np.array(MTX_hs, dtype=object)

        MTX_if_note, MTX_if_ln, MTX_hold_time, MTX_hs, MTX_start_time = merge_rows(MTX_start_time, MTX_if_note, MTX_if_ln, MTX_hold_time, MTX_hs)
        keys = len(MTX_if_note[0])

        return cls(MTX_if_note, MTX_start_time, MTX_if_ln, MTX_hold_time, MTX_hs, keys)

    def get_obj(self):
        obj_str = []
        for i in range(len(self.MTX_start_time)):
            for j in range(self.keys):
                if self.MTX_if_note[i][j] == 1:
                    start_time = self.MTX_start_time[i]
                    if_ln = self.MTX_if_ln[i][j]
                    hold_time = self.MTX_hold_time[i][j]
                    hs = self.MTX_hs[i][j]
                    obj_str.append(f"{key_value(j, self.keys)},192,{start_time},{if_ln},0,{hold_time}{hs}")
        return obj_str

    def get_to_keys_obj(self, MTX):
        to_keys = len(MTX[0])
        obj_str = []
        for i in range(len(self.MTX_start_time)):
            for j in range(to_keys):
                # 检查 i 是否超过 MTX 的长度
                if i >= len(MTX):
                    break
                else:
                    index = i
                    if MTX[index][j] == -1:
                        continue
                    elif self.MTX_if_note[i][MTX[index][j]] == 1:
                        start_time = self.MTX_start_time[i]
                        if_ln = self.MTX_if_ln[i][MTX[index][j]]
                        hold_time = self.MTX_hold_time[i][MTX[index][j]]
                        hs = self.MTX_hs[i][MTX[index][j]]
                        obj_str.append(f"{key_value(j, to_keys)},192,{start_time},{if_ln},0,{hold_time}{hs}")
        return obj_str

    def get_to_keys_obj_NtoNS(self, array):
        to_keys = len(array)
        obj_str = []
        org_len = len(self.MTX_if_note[0])
        for i in range(len(self.MTX_start_time)):
            for j in range(to_keys):
                if array[j] < 0 or array[j] >= org_len:
                    continue
                elif self.MTX_if_note[i][array[j]] == 1:
                    start_time = self.MTX_start_time[i]
                    if_ln = self.MTX_if_ln[i][array[j]]
                    hold_time = self.MTX_hold_time[i][array[j]]
                    hs = self.MTX_hs[i][array[j]]
                    if hs =="":
                        hs = ":0:0:0:"
                    obj_str.append(f"{key_value(j, to_keys)},192,{start_time},{if_ln},0,{hold_time}{hs}")
        return obj_str

    def get_to_keys_obj_if_note(self, MTX):
        to_keys = len(MTX[0])
        obj_str = []
        for i in range(len(self.MTX_start_time)):
            for j in range(to_keys):
                if MTX[i][j] == 1:
                    start_time = self.MTX_start_time[i]
                    if_ln = 1
                    hold_time = 0
                    hs = ':0:0:0:'
                    obj_str.append(f"{key_value(j, to_keys)},192,{start_time},{if_ln},0,{hold_time}{hs}")

        return obj_str







