# -*- coding: utf-8 -*-
import math

class RowOfNotes:
    def __init__(self, start_time, holding_time, row=[], keys=7):
        """
        :param keys: 当前谱的colunms默认7

        self.row: [[0,""],.....]的二维列表，[0,""]表示当前轨道无,[1,str]表示当前轨道有，str等于去掉column值的一行字符串
        比如"96,192,43790,128,0,43887:0:0:0:0:"则str = "192,43790,128,0,43887:0:0:0:0:"，默认先构建一个4K的row，不影响后续
        """
        self.start_time = start_time
        self.holding_time = holding_time
        self.row = row
        self.keys = keys

    @classmethod
    def new_row_from_original_str_line(cls, note_str, keys=7):
        """
        输入物件字符串来构建行
        :param note_str: 一行物件的字符串，如 "96,192,43790,128,0,43887:0:0:0:0:"
        :param keys: 当前谱面的keys，用来计算下标，默认值7，如果是其他模式的谱则要填写
        """
        parts = note_str.split(',')
        start_time = int(parts[2])
        holding_time = int(parts[5].split(':', 1)[0])
        temp = [[0, ""] for _ in range(keys)]
        index = int(math.floor(int(parts[0]) * keys / 512))
        temp[index][0] = 1
        temp[index][1] = note_str[note_str.find(',') + 1:]
        row = temp
        return cls(start_time, holding_time, row, keys)

    # ---------getter & setter-----------------------
    @property
    def keys(self):
        return self._keys

    @keys.setter
    def keys(self, value):
        self._keys = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def holding_time(self):
        return self._holding_time

    @holding_time.setter
    def holding_time(self, value):
        self._holding_time = value
    # ---------------------------------------------------