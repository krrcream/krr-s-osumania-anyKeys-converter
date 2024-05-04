import random
import numpy as np
from typing import List
from row_of_notes import RowOfNotes
from matrix_convert import gen_simple_note_string,keyvalue,matrix_merge

def create_matrix_blocks(timestamps, objects_list, interval=100):
    # 构建一个空列表用于保存矩阵块
    matrix_blocks = []
    start_blocks = []
    P_blocks = []
    # 用于记录连续时间戳的起始和结束索引
    start_index = 0
    end_index = 0
    start_blocks.append(timestamps[start_index])
    # 遍历时间戳列表
    for i in range(1, len(timestamps)):
        if timestamps[i] - timestamps[start_index] <= interval-10:  # 当连续时间戳在间隔范围内时
            end_index = i  # 更新结束索引
        else:  # 当间隔范围超出时
            if end_index < start_index:
                end_index = start_index# 若结束索引为0，说明此时还在间隔内，不生成矩阵块
            interval_objects = objects_list[start_index:end_index+1]  # 提取对应的物件状态
            temp_block = np.array(interval_objects)
            matrix_blocks.append(temp_block)  # 创建矩阵块并添加到列表
            # 计算矩阵块中所有1出现的概率
            total_elements = temp_block.size  # 获取矩阵中的总元素数量
            count_ones = np.count_nonzero(temp_block == 1)  # 计算矩阵中1的出现次数
            P_blocks.append(count_ones / total_elements)  # 计算概率并插入
            start_index = i  # 更新起始索引
            start_blocks.append(timestamps[start_index])  # 更新起始时间戳
        if i == len(timestamps) - 1:  # 若遍历到最后一个时间戳，则生成最后一个矩阵块
            end_index = i
            interval_objects = objects_list[start_index:end_index+1]  # 提取对应的物件状态
            temp_block = np.array(interval_objects)
            matrix_blocks.append(temp_block)  # 创建矩阵块并添加到列表
            # 计算矩阵块中所有1出现的概率
            total_elements = temp_block.size  # 获取矩阵中的总元素数量
            count_ones = np.count_nonzero(temp_block == 1)  # 计算矩阵中1的出现次数
            P_blocks.append(count_ones / total_elements)  # 计算概率并插入

    return start_blocks, P_blocks, matrix_blocks

def make_disjoint(list1, list2):
    zero_indices = [i for i in range(len(list1)) if list1[i] == 0 and list2[i] == 0]
    for i in range(len(list1)):
        if list1[i] == 1 and list2[i] == 1:
            if zero_indices:
                random_index = random.choice(zero_indices)
                zero_indices.remove(random_index)
                list2[random_index] = 1
            list2[i] = 0

def everthing_to_jacks(keys, matrix_merged: List[RowOfNotes], to_keys, BPM_org_limitation=100.0,flag=1):
    object_matrix = [[note[0] for note in obj.row] for obj in matrix_merged]
    start_time_list = [obj.start_time for obj in matrix_merged]
    start_time_list1,probability_list1,matrix_blocks = create_matrix_blocks(start_time_list, object_matrix, BPM_org_limitation-10.0)
    new_matrix = []
    for val in probability_list1:
        row = [0] * to_keys  # 生成长度为8，所有元素为0的列表
        num_ones = int(val * to_keys)  # 根据概率计算1的个数
        adjustment = 0
        if flag == 1:
            adjustment = random.randint(0, 2)  # 随机增加或减少±to_keys/4
        elif flag == 0:
            adjustment = random.randint(-2, 0)  # 随机增加或减少±to_keys/4
        num_ones += adjustment
        num_ones = max(1, min(num_ones, to_keys))  # 限制最小为1，最大为8
        for _ in range(num_ones):
            index = random.randint(0, to_keys - 1)  # 随机选择下标
            row[index] = 1
        new_matrix.append(row)
    return start_time_list1, new_matrix



def adjust_rows(row1, row2):
    for i in range(len(row1)):
        if row1[i] == 1 and row2[i] == 1:  # 如果相同下标同时为1
            if i%2 == 0:
                row1[i] = 0
            else:#
                row2[i] = 0  # 则将其中一个改为0
    return row1, row2


def everthing_to_stream(keys, matrix_merged: List[RowOfNotes], to_keys, BPM_org_limitation=100.0):
    start_time_list2, matrix2 = everthing_to_jacks(keys, matrix_merged, to_keys, (BPM_org_limitation/2+15.0),flag=0)
    for i in range(len(matrix2) - 1):
        make_disjoint(matrix2[i-1], matrix2[i])
    return start_time_list2, matrix2


def row_of_notes_matrix_generation(start_time_list2: List[int], matrix3: List[List[int]]):
    for i in range(len(start_time_list2)):
        for j in range(len(matrix3[i])):
            if matrix3[i][j] == 1:
                matrix3[i][j] = [1, gen_simple_note_string(start_time_list2[i])]
            if matrix3[i][j] == 0:
                matrix3[i][j] = [0, ""]

def jacks_in_stream(matrix_merged: List[RowOfNotes], interval=8, add_num=1,BPM_org_limitation=100.0, flag=1):
    columns = []
    object_matrix = [[note[0] for note in obj.row] for obj in matrix_merged]#NOTE矩阵
    start_time_list = [obj.start_time for obj in matrix_merged]#时间戳列表
    holding_time_list = [obj.holding_time for obj in matrix_merged]#面条持续时间列表
    keys = len(object_matrix[0])
    for i in range(keys):
        columns.append([row[i] for row in object_matrix])
    for j in range(len(columns[0])):
        if j % interval == 0 and 0 < j < len(columns[0])-2:
            previous_row_ones = []
            previous_row_notes = object_matrix[j-1]
            for i, note in enumerate(previous_row_notes):
                if note == 1:
                    previous_row_ones.append(i)
            if start_time_list[j] > holding_time_list[j] and start_time_list[j] - start_time_list[j-1]>BPM_org_limitation:
                random_numbers = random.sample(previous_row_ones, min(add_num,len(previous_row_ones)))
                for num in random_numbers:
                    columns[num][j] = 1
                    if flag == 1:
                        columns[num][j + 1] = 0
                        all_zero_indices = []
                        for n in range(keys):
                            if columns[n][j]==0 or columns[n][j+2]==0:
                                all_zero_indices.append(n)
                        if all_zero_indices:
                            if num<= keys/2:
                                all_zero_indices = [x for x in all_zero_indices if x >= keys/2]
                            else:
                                all_zero_indices = [x for x in all_zero_indices if x <= keys/2]
                            if all_zero_indices:
                                random_index = random.choice(all_zero_indices)
                                all_zero_indices.remove(random_index)
                                columns[random_index][j + 1] = 1
    object_matrix = [list(row) for row in zip(*columns)]
    return start_time_list, object_matrix

def write_notes_to_str(matrix_ok):
    note_str = ""
    to_keys = len(matrix_ok[0])
    for row_notes in matrix_ok:
        for i, note in enumerate(row_notes):
            if note[0] == 1:
                # column_value = key_dict[to_keys - 1][i]
                column_value = keyvalue(i, to_keys)
                note_str += str(column_value) + "," + note[1] + "\n"
    return note_str




#e.p
# notes = """9,192,110,5,0,0:0:0:0:
# 448,192,110,1,0,0:0:0:0:
# 228,192,110,1,0,0:0:0:0:
# 155,192,110,1,0,0:0:0:0:
# 9,192,335,1,0,0:0:0:0:
# 301,192,335,1,0,0:0:0:0:
# 82,192,448,1,0,0:0:0:0:
# 374,192,448,1,0,0:0:0:0:
# 9,192,561,1,0,0:0:0:0:
# """
# lines_note_objs = notes.strip().splitlines()
# matrix = []
# for line in lines_note_objs:
#     matrix.append(RowOfNotes.new_row_from_original_str_line(line,7))
# matrix = matrix_merge(matrix)
#
# start_time_list, matrix = jacks_in_stream(matrix)
# row_of_notes_matrix_generation(start_time_list, matrix)
# str = write_notes_to_str(matrix)
# print(str)
# # —————————————万物化系列e.p———————————————
# # # start_time_list, jack_matrix = everthing_to_jacks(4,matrix,8)
# # # # row_of_notes_matrix_generation(start_time_list, jack_matrix)
# # # jack_str = write_notes_to_str(jack_matrix)
# # # print(jack_str)
# # start_time_list1, stream_matrix = everthing_to_stream(4,matrix,8)
# # row_of_notes_matrix_generation(start_time_list1, stream_matrix)
# # stream_str = write_notes_to_str(stream_matrix)
# # print(stream_str)
