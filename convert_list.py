# -*- coding: utf-8 -*-
import math
import random
from typing import List

import numpy as np

from row_of_notes import RowOfNotes

# --------简单预设list------------
to_4KDP1 = [0, 1, 2, 3, 0, 1, 2, 3]
to_4KDP2 = [3, 2, 1, 0, 3, 2, 1, 0]
to_4KDPM1 = [0, 1, 2, 3, 3, 2, 1, 0]
to_4KDPM2 = [3, 2, 1, 0, 0, 1, 2, 3]

to_BMSto7k = [1, 2, 3, 4, 5, 6, 7]
to_7kto6k_delete_middle_columm = [0, 1, 2, 4, 5, 6]

to_7kto8k_8KW = [0, 1, 2, 3, 3, 4, 5, 6]
to_7kto8k_8KT = [3, 0, 1, 2, 4, 5, 6, 3]


def count_differences(arr1, arr2):
    return sum(1 for x, y in zip(arr1, arr2) if x != y)


# --------正态分布随机数生成--------
def np_random_num(keys):
    mean = (keys - 1) / 2
    std_dev = keys / 2.5
    # 生成一个在0到keys之间符合正态分布的随机数
    random_num = int(round(np.random.normal(mean, std_dev)))
    while random_num < 0 or random_num > keys - 1:
        random_num = int(round(np.random.normal(mean, std_dev)))
    return random_num


# --------预设list---------------
def to_4KDPChaos_list(num=1):  #用来4K生成8K大裤衩练习的
    convert_permutations = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 0, 1, 0],
        [1, 1, 0, 1],
        # [0, 0, 1, 1],
        # [1, 1, 0, 0]
    ]
    random_permutation1 = random.choice(convert_permutations)
    random_permutation2 = random.choice(convert_permutations)
    random_permutation2 = [x + 2 for x in random_permutation2]
    index_list = random_permutation1 + random_permutation2
    if num == 1:
        random_num = random.randint(1, 8)
        index_list = index_list[random_num:] + index_list[:random_num]
    return index_list


def to_lowKeys_2_highKeys_addkeys_chaos(keys, add_columns, add_blank=0):  #任意低K转任意高K
    """

    :param key:原谱K数，请用获取文件时跟CS关联，测试时需要手填
    :param add_columns: 添加的随机轨道的个数
    :param add_blank: 添加的随机空行的个数
    :return: 变换列表
    比如7k转10k，我们又不想要note太多，可以add_columns=1,add_blank=2  key=10 ，这样复制原有的1个轨道后再加两个空轨道

    """
    #生成列表
    convert_permutations = list(range(0, keys))
    temp = convert_permutations
    if add_columns >= 0:
        #插入复制的轨道
        for i in range(add_columns):  #随机抽选轨道
            key = convert_permutations.index(np_random_num(keys))
            while key < 0 or key > keys - 1:
                key = convert_permutations.index(np_random_num(keys))
            position = random.randint(0, len(temp))
            temp.insert(position, key)

        # if add_blank > 0:  #插入轨道
        #     for j in range(add_blank):
        #         position = random.randint(0, len(temp))
        #         temp.insert(position, -1)
    elif add_columns < 0:
        random.shuffle(temp)
        temp = temp[:keys + add_columns]
        temp = sorted(temp)
    if add_blank > 0:
        add_flag = add_blank#插入空轨道实现左右
        random_index = random.randint(0, len(temp))
        while add_flag > 0:
            temp.insert(random_index, -1)
            if random_index > len(temp)/2:
                random_index = random.randint(0, math.floor(len(temp)/2))
                print(random_index)
            elif random_index < len(temp)/2:
                random_index = random.randint(math.ceil(len(temp)/2), len(temp))
                print(random_index)
            elif random_index == len(temp)/2:
                random_index = random.randint(0, len(temp))
                print(random_index)
            add_flag -= 1
    return temp


# def to_lowKeys_2_highKeys_wkeys(keys,add_columns,add_blank=0): #任意低K转任意高K的随机双键 废弃，但未来可能启用
#     """
#
#     :param key:原谱K数，请用获取文件时跟CS关联，测试时需要手填
#     :param add_columns: 添加的随机双键的个数
#     :param add_blank: 添加的随机空行的个数
#     :return: 比如to_lowKeys_2_highKeys_wkeys(7,2,1)  会生成 [0,1,2,2,3,-1,4,5,6,6] 这种两个双键，插入一个空行
#
#     """
#     #生成列表
#     convert_permutations = list(range(0, keys))
#     #插入复制的轨道
#     for i in range(add_blank):
#         blank_column = np_random_num(len(convert_permutations))
#         convert_permutations.insert(blank_column,-1)
#     for i in range(add_columns):
#         key = list(range(0, keys))[np_random_num(keys)]
#         try:
#             index = convert_permutations.index(key)
#         except ValueError:
#             print("列表中不存在数字", key)
#         convert_permutations.insert(index, key)
#     return convert_permutations

def everthing_to_jacks(keys, matrix_merged: List[RowOfNotes], to_keys):
    object_matrix = [[note[0] for note in obj.row] for obj in matrix_merged]
    nonzero_counts = [row.count(0) for row in object_matrix]
    probability_list = [count / keys for count in nonzero_counts]
    new_matrix = []
    for val in probability_list:
        row = [0] * to_keys  # 生成长度为8，所有元素为0的列表
        num_ones = int(val * to_keys)  # 根据概率计算1的个数
        for _ in range(num_ones):
            index = random.randint(0, to_keys - 1)  # 随机选择下标
            row[index] = index
        new_matrix.append(row)
    return new_matrix