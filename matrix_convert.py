# -*- coding: utf-8 -*-
import copy
import math
import random

from typing import List, Union, Callable

import convert_list
from row_of_notes import RowOfNotes


def keyvalue(column, keys):
    if keys <= 3 or (keys > 3 and keys % 2 == 0):
        return math.floor((column + 0.5) * 512 / keys)
    if keys > 3 and keys % 2 == 1:
        if column < (keys - 1) / 2:
            return math.floor((column + 0.5) * 512 / (keys - 1))
        if column > (keys - 1) / 2:
            return math.floor((column - 0.5) * 512 / (keys - 1))
        if column == (keys - 1) / 2:
            return 256


def who_zero_more(row_0, row_2):
    count_row_0 = 0
    count_row_2 = 0
    for p in range(len(row_0)):
        if row_0[p][0] == 0:
            count_row_0 += 1
        if row_2[p][0] == 0:
            count_row_2 += 1
    if count_row_0 > count_row_2:
        return 0
    elif count_row_0 < count_row_2:
        return 1


def judge_time(row_0_start_time, start_time_list: List[int], limitation):
    differences = [abs(row_0_start_time - start_time) for start_time in start_time_list]
    return all(diff < limitation for diff in differences)


def are_rows_different(row1, row2):
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            return True
    return False


def gen_simple_note_string(start_time):
    str1 = f"192,{start_time},1,0,0:0:0:0:"
    return str1


def different_indices(row1, row2):
    indices = []
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            indices.append(i)
    return indices


def calrowinterval(row1, row2):
    return row1.start_time - row2.start_time


def jack_deletion_by_dif_indecis(row_0, row_1, dif_lst, time=0):
    def count_one(row):
        count = 0
        for i in range(len(row)):
            if row[0] == 1:
                count += 1
        return count

    for index in dif_lst:
        if row_0[index][0] == 1 and row_1[index][0] == 1:
            if count_one(row_0) > count_one(row_1):
                row_0[index][0] = 0
                row_0[index][1] = ""
            else:
                row_1[index][0] = 0
                row_1[index][1] = ""


def blank_column_check(row_0, row_1, row_2, row_1_start_time, start_time_list: List[int], limitation=150.0):
    # 将note多的移动到少的那里或者无法移动时则自己填
    indices_of_zeros = [i for i, x in enumerate(row_1) if x[0] == 0]
    if len(indices_of_zeros) >= len(row_1) - 2:
        common_zeros = [index for index, (value1, value2) in enumerate(zip(row_0, row_2)) if
                        value1[0] == 0 and value2[0] == 0]
        indices1 = random.sample(common_zeros, math.ceil(len(common_zeros) / 4 * 3))
        if  judge_time(row_1_start_time, start_time_list, limitation):
            pass
        else:
            for index in indices1:
                row_1[index][0] = 1
                # print(index)
                row_1[index][0] = 1
                row_1[index][1] = gen_simple_note_string(row_1_start_time)
                row_0[index][0] = 0
                row_0[index][1] = ""
                row_2[index][0] = 0
                row_2[index][1] = ""
            lst = [x for x in range(len(row_1))]
            set1 = set(lst)
            set2 = set(indices1)
            tozeroindices = set1 - set2
            for index1 in tozeroindices:
                row_1[index1][0] = 0
                row_1[index1][1] = ""

def blank_column_checkV2(row_0:RowOfNotes,row_rim:List[RowOfNotes],limitation=150.0,con_indices:List[int]=None):
    if not row_rim:
        pass
    else:
        indices_of_zeros = [i for i, x in enumerate(row_0.row) if x[0] == 0]
        if len(indices_of_zeros) >= len(row_0.row) - 2:
            sample_size = math.ceil(len(indices_of_zeros) / 3)
            sampled_list = random.sample(indices_of_zeros, sample_size)
            if all(abs((row_0.start_time - sT.start_time)) > limitation for sT in row_rim):
                for index in con_indices:
                    if all(sT.row[index][0] == 0 for sT in row_rim):
                        row_0.row[index][0] = 1
                        row_0.row[index][1] = gen_simple_note_string(row_0.start_time)

# def blank_column_check(row_0,row_1,row_1_starttime):
#     # 将note多的移动到少的那里或者无法移动时则自己填
#     zero_flag = 0
#     for each in row_1:
#         if each[0] == 0:
#             zero_flag += 1
#     if zero_flag == len(row_1):
#         indecis = random.sample(list(range(len(row_1))),math.ceil(len(row_1)/2))
#         for index in indecis:
#             row_1[index][0] = 1
#             row_1[index][1] = gen_simple_note_string(row_1_starttime)
#             row_0[index][0] = 0
#             row_0[index][1] = ""


def wblank_addnotes(row_0, row_1, row_2, row_1_starttime, jack_del_limitation=150):  # 双空校验，加键
    wzero_indices = [i for i, (note_0, note_2) in enumerate(zip(row_0, row_2)) if note_0[0] == 0 and note_2[0] == 0]
    if len(wzero_indices) > 0:
        wzero_indices = random.sample(wzero_indices, math.ceil(len(wzero_indices) * 1 / 3))
        for index in wzero_indices:
            row_1[index][0] = 1
            row_1[index][1] = gen_simple_note_string(row_1_starttime)


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
            input_list: Union[List[int], Callable[[], List[int]]], step=32, time_step=1600, jack_del_limitation=150,
            deljackLV=2):
    time_flag = 0
    step_flag = 0
    convert_list_matrix = []
    matrix_convert = []

    if callable(input_list):
        # 如果输入是一个方法，调用它来获取整数列表
        index_list = input_list()
    else:
        # 如果输入是一个整数列表，直接使用它,简单矩阵变换
        index_list = input_list

    # ---------写入-------------
    for i, row in enumerate(matrix_merged):
        if ((row.start_time > row.holding_time) and
                (step_flag > step or time_flag >= time_step)):  # 如果没有面条以及满足时间或者行的步距则更新变换
            time_flag = 0
            step_flag = 0
            if callable(input_list):
                # 重新获取变换列表
                last_convert_lst = index_list  # 旧变换列表
                index_list = input_list()  # 新列表
                while convert_list.count_differences(last_convert_lst, index_list) > len(index_list) / 2:
                    index_list = input_list()  # 新列表
            else:
                # 如果输入是一个整数列表，直接使用它,简单矩阵变换
                index_list = input_list
        convert_list_matrix.append(index_list)
        if i < len(matrix_merged) - 1:  # 完成一行，增加时间步距
            time_flag += (matrix_merged[i + 1].start_time - matrix_merged[i].start_time)
        step_flag += 1  # 完成一行，增加步距

    for k, row1 in enumerate(matrix_merged):
        temp = []
        for each_as_index in convert_list_matrix[k]:
            temp.append(matrix_merged[k].row[each_as_index])

        matrix_convert.append(matrix_merged[k])
        matrix_convert[k].row.clear()
        for each in temp:
            matrix_convert[k].row.append(each)

    delflag = 0
    for i in range(len(matrix_convert) - 2):
        if are_rows_different(convert_list_matrix[i], convert_list_matrix[i + 1]):
            flag = 4
            dif_lst = different_indices(convert_list_matrix[i], convert_list_matrix[i + 1])
            if matrix_convert[i + 1].start_time - matrix_convert[i].start_time > jack_del_limitation * 7 / 4:
                continue
            else:

                temp_row_num = i
                limitation = jack_del_limitation * 7 / 4
                k = 0
                if deljackLV == 3:
                    flag = 4
                    limitation = jack_del_limitation * 7 / 4
                elif deljackLV == 2:
                    flag = 2
                    limitation = jack_del_limitation * 5 / 4
                elif deljackLV == 1:
                    flag = 1
                    limitation = jack_del_limitation * 3 / 4
                elif deljackLV == 0:
                    flag = 0
                    limitation = jack_del_limitation * 1 / 2
                if limitation < 77:
                    limitation = 77
                if limitation > 200:
                    limitation = 200
                while flag > 0 and (matrix_convert[temp_row_num + 1 + k].start_time - matrix_convert[
                    temp_row_num].start_time < limitation) and temp_row_num + 1 + k < len(matrix_convert):
                    jack_deletion_by_dif_indecis(matrix_convert[temp_row_num].row,
                                                 matrix_convert[temp_row_num + 1 + k].row,
                                                 dif_lst)

                    #组合start_time_list
                    start_time_list = []
                    for c in range(4, 0, -1):
                        try:
                            start_time_list.append(matrix_convert[temp_row_num + k + 1 - c])
                        except IndexError:
                            pass

                    # 处理 i+1 到 i+4 的索引
                    for c in range(1, 5):
                        try:
                            start_time_list.append(matrix_convert[temp_row_num + k + 1 + c])
                        except IndexError:
                            pass

                    blank_column_checkV2(matrix_convert[temp_row_num + k], start_time_list, limitation, dif_lst)

                    k += 1
                    flag -= 1

    # for l in range(len(matrix_convert) - 2):
    #     if are_rows_different(convert_list_matrix[l],convert_list_matrix[l+1]):
    #         flag = 4
    #         k=0
    #         if deljackLV == 3:
    #             flag = 1
    #         elif deljackLV == 2:
    #             flag = 1
    #         elif deljackLV == 1:
    #             flag = 1
    #         elif deljackLV == 0:
    #             flag = 0
    #
    #
    #         while flag > 0 and l+2+k<len(matrix_convert):
    #             print(f"{l+k+1}行，时间是{matrix_convert[l+k+1].start_time}")
    #             blank_column_check(matrix_convert[l+k].row, matrix_convert[l+k+1].row,matrix_convert[l+k+2].row, matrix_convert[l+k+1].start_time)
    #             flag -= 1
    #             k+=1

    return matrix_convert


def write_notes(matrix_convert: List[RowOfNotes]):
    note_str = ""
    to_keys = len(matrix_convert[0].row)
    for row_notes in matrix_convert:
        for i, note in enumerate(row_notes.row):
            if note[0] == 1:
                # column_value = key_dict[to_keys - 1][i]
                column_value = keyvalue(i, to_keys)
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
