# -*- coding: utf-8 -*-
import math
import random

from typing import List, Union, Callable
from row_of_notes import RowOfNotes


def keyvalue(column,keys):
    if keys <= 3 or (keys>3 and keys % 2 ==0):
        return math.floor((column+0.5) *512/keys)
    if keys >3 and keys % 2 == 1:
        if column < (keys-1) / 2:
            return math.floor((column+0.5) *512/(keys-1))
        if column > (keys-1) / 2:
            return math.floor((column-0.5) *512/(keys-1))
        if column == (keys - 1)/2:
            return 256

#空行校验
def line_blank_check(rowup, rowmid, rowdown,str):
    if all(note[0] == 0 for note in rowmid):

        zero_indicesdown = [index for index, value in enumerate(rowdown) if value[0] == 0]
        zero_indicesup = [index for index, value in enumerate(rowup) if value[0] == 0]
        if len(zero_indicesup) < len(zero_indicesdown):
            zero_indicesdown = random.sample(zero_indicesdown, math.floor(len(zero_indicesdown) / 2))
            for each_index1 in zero_indicesdown:
                rowmid[each_index1][0] = 1
                rowmid[each_index1][1] = f"192,{str},1,0,0:0:0:0:"
                rowup[each_index1][0] = 0
        elif len(zero_indicesup) >= len(zero_indicesdown):
            zero_indicesup = random.sample(zero_indicesup, math.floor(len(zero_indicesup) / 2))
            for each_index2 in zero_indicesup:
                rowmid[each_index2][0] = 1
                rowmid[each_index2][1] = f"192,{str},1,0,0:0:0:0:"
                rowdown[each_index2][0] = 0

def matrix_merge(pending_matrix: List[RowOfNotes]):
    temp_matrix = []
    temp_row_of_notes = pending_matrix[0]
    if not all(isinstance(item, RowOfNotes) for item in pending_matrix):
        raise TypeError("所有元素必须是RowOfNotes的实例。")
    for i, row_m in enumerate(pending_matrix):  # 合并同时间的note
        if temp_row_of_notes.start_time == row_m.start_time:
            for j, note in enumerate(pending_matrix[i].row):
                if note[0] == 1:
                    temp_row_of_notes.row[j] = note
            temp_row_of_notes.holding_time = max(temp_row_of_notes.holding_time, row_m.holding_time)
        if temp_row_of_notes.start_time < row_m.start_time:
            temp_matrix.append(temp_row_of_notes)
            temp_row_of_notes = row_m
        if i == len(pending_matrix) - 1:
            temp_matrix.append(temp_row_of_notes)

    for i, row_m in enumerate(temp_matrix):  # 更新面条最大时间
        if i > 0:
            row_m.holding_time = max(row_m.holding_time, temp_matrix[i - 1].holding_time)
    return temp_matrix


def print_matrix(matrix_print: List[RowOfNotes]):  # 打印0,1,0格式的方便检查，该方法和算法无关
    for item in matrix_print:
        print(f"开始时间:{item.start_time},面条或面条最大时间:{item.holding_time}  ", end="")
        print("[", end=" ")
        for note in item.row:
            print(note[0], end=" ")
        print("]")




def convert(matrix_merged: List[RowOfNotes],
            input_list: Union[List[int], Callable[[], List[int]]], step=32, time_step=1600,jack_del_limitation=150 ,deljackLV=2):
    matrix_convert = []
    time_flag = 0
    step_flag = 0
    # 变换

    if callable(input_list):
        # 如果输入是一个方法，调用它来获取整数列表
        index_list = input_list()
    else:
        # 如果输入是一个整数列表，直接使用它,简单矩阵变换
        index_list = input_list
    for i, row_of_notes1 in enumerate(matrix_merged):
        temp_row = []
        convert_flag = 0
        if ((row_of_notes1.start_time > row_of_notes1.holding_time) and
                (step_flag > step or time_flag >= time_step)):  # 如果没有面条以及满足时间或者行的步距则更新变换
            time_flag = 0
            step_flag = 0
            if callable(input_list):
                # 重新获取变换列表
                index_list = input_list()
                convert_flag = 3  # 是否发生变换，当con_flag = 1时需要执行删子弹方法
            else:
                # 如果输入是一个整数列表，直接使用它,简单矩阵变换
                index_list = input_list

        for j, index in enumerate(index_list):  # 从左往右铺设note,把原始行里对应下标轨道的note，填入临时轨道，如果是-1则填空
            temp_row.append(matrix_merged[i].row[index])
            if j == len(index_list) - 1:
                matrix_convert.append(RowOfNotes(row_of_notes1.start_time, row_of_notes1.holding_time, temp_row,
                                                 len(temp_row)))  # 往矩阵里插入新的RowOfNotes对象
        if i < len(matrix_merged) - 1:  # 完成一行，增加时间步距
            time_flag += (matrix_merged[i + 1].start_time - matrix_convert[i].start_time)

        step_flag += 1  # 完成一行步距+1

        # 删除子弹 del_jack有BUG，暂时不用
        if deljackLV==3:
            if i >= 6 and convert_flag == 3:
                for k in range(len(matrix_convert[i].row)):
                    if (matrix_convert[i].row[k][0]) == 1 and matrix_convert[i].start_time - matrix_convert[i-1].start_time < jack_del_limitation * 1.33:
                        if matrix_convert[i - 1].row[k][0] == 1:
                            matrix_convert[i - 1].row[k] =[0,""]
                        if matrix_convert[i].start_time - matrix_convert[i - 2].start_time < jack_del_limitation + 2:
                            matrix_convert[i - 2].row[k] = [0, ""]
                        if matrix_convert[i].start_time - matrix_convert[i - 3].start_time < jack_del_limitation + 2:
                            matrix_convert[i - 3].row[k] = [0, ""]
                        if matrix_convert[i].start_time - matrix_convert[i - 4].start_time < jack_del_limitation + 2:
                            matrix_convert[i - 4].row[k] = [0, ""]
                        if matrix_convert[i].start_time - matrix_convert[i - 5].start_time < jack_del_limitation + 2:
                            matrix_convert[i - 5].row[k] = [0, ""]
                convert_flag = 2
                line_blank_check(matrix_convert[i].row, matrix_convert[i - 1].row, matrix_convert[i - 2].row, matrix_convert[i - 1].start_time)
            if i >= 6 and convert_flag == 2:
                for n in range(len(matrix_convert[i].row)):
                    if matrix_convert[i].row[n][0] == 1:
                        if matrix_convert[i].start_time - matrix_convert[i - 2].start_time < jack_del_limitation + 2:
                            matrix_convert[i - 2].row[n] = [0, ""]
                        if matrix_convert[i].start_time - matrix_convert[i - 3].start_time < jack_del_limitation + 2:
                            matrix_convert[i - 3].row[n] = [0, ""]
                convert_flag = 1
                line_blank_check(matrix_convert[i - 1].row, matrix_convert[i - 2].row, matrix_convert[i - 3].row, matrix_convert[i - 2].start_time)
            if i >= 6 and convert_flag == 1:
                for n in range(len(matrix_convert[i].row)):
                    if matrix_convert[i].row[n][0] == 1:
                        if matrix_convert[i].start_time - matrix_convert[i - 3].start_time < jack_del_limitation + 2:
                            matrix_convert[i - 3].row[n] = [0, ""]
                convert_flag = 0
                line_blank_check(matrix_convert[i - 2].row, matrix_convert[i - 3].row, matrix_convert[i - 4].row, matrix_convert[i - 3].start_time)
        elif deljackLV == 2:
            if i >= 6 and convert_flag == 3:
                for k in range(len(matrix_convert[i].row)):
                    if (matrix_convert[i].row[k][0]) == 1 and matrix_convert[i].start_time - matrix_convert[i-1].start_time < jack_del_limitation * 1.33:
                        if matrix_convert[i - 1].row[k][0] == 1:
                            matrix_convert[i - 1].row[k] =[0,""]
                        if matrix_convert[i].start_time - matrix_convert[i - 2].start_time < jack_del_limitation + 2:
                            matrix_convert[i - 2].row[k] = [0, ""]
                convert_flag = 2
                line_blank_check(matrix_convert[i].row, matrix_convert[i - 1].row, matrix_convert[i - 2].row, matrix_convert[i - 1].start_time)
            if i >= 6 and convert_flag == 2:
                for n in range(len(matrix_convert[i].row)):
                    if matrix_convert[i].row[n][0] == 1:
                        if matrix_convert[i].start_time - matrix_convert[i - 2].start_time < jack_del_limitation + 2:
                            matrix_convert[i - 2].row[n] = [0, ""]
                convert_flag = 0
                line_blank_check(matrix_convert[i - 1].row, matrix_convert[i - 2].row, matrix_convert[i - 3].row, matrix_convert[i - 2].start_time)
        elif deljackLV == 1:
            if i >= 6 and convert_flag == 3:
                for k in range(len(matrix_convert[i].row)):
                    if (matrix_convert[i].row[k][0]) == 1 and matrix_convert[i].start_time - matrix_convert[
                        i - 1].start_time < jack_del_limitation /5 * 4:
                        if matrix_convert[i - 1].row[k][0] == 1:
                            matrix_convert[i - 1].row[k] = [0, ""]
                convert_flag = 0
                line_blank_check(matrix_convert[i].row, matrix_convert[i - 1].row, matrix_convert[i - 2].row, matrix_convert[i - 1].start_time)
        elif deljackLV == 0:
            convert_flag = 0

    return matrix_convert



def write_notes(matrix_convert: List[RowOfNotes]):
    note_str = ""
    to_keys = len(matrix_convert[0].row)
    for row_notes in matrix_convert:
        for i, note in enumerate(row_notes.row):
            if note[0] == 1:
                # column_value = key_dict[to_keys - 1][i]
                column_value = keyvalue(i,to_keys)
                note_str += str(column_value) + "," + note[1] + "\n"
    return note_str

# 示例
# notes = """36,192,330,1,0,0:0:0:0:
# 182,192,330,1,0,0:0:0:0:
# 36,192,545,1,0,0:0:0:0:
# 109,192,545,1,0,0:0:0:0:
# 36,192,760,1,0,0:0:0:0:"""
#
# note_list = notes.splitlines() #给文本按行分成列表
# matrix = []
# # 每个note为一个RowOfNotes，矩阵未合并
# for line in note_list:
#     matrix.append(RowOfNotes.new_row_from_original_str_line(line))
#
# matrix = matrix_merge(matrix)
# print_matrix(matrix)
#
# matrix = convert(matrix, convert_list.to_lowKeys_2_highKeys_chaos(7,1,0))
# print(write_notes(matrix))
