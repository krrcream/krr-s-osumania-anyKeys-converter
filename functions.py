"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""
import math
import random
import re
from itertools import cycle, tee, chain

import numpy as np


#生成种子数字
def generate_seed():  # 生成随机种子
    # 生成随机长度
    seed_length = random.randint(6, 16)

    # 确保第一个字符不为0
    first_digit = str(random.randint(1, 9))  # 生成1到9之间随机数字
    remaining_digits = ''.join(random.choices('0123456789', k=seed_length - 1))  # 生成剩余的随机数字

    # 组合成最终的种子字符串
    seed = first_digit + remaining_digits
    return seed


def set_seed(seed):  #设置种子
    seed_int = int(seed)
    # 检查是否超出最大值
    if seed_int > 4294967294:
        # 如果超出范围，截取最后9个字符
        seed = seed[-9:]
    seed = int(seed)
    # np.random.seed(seed)  # 设置numpy的种子
    random.seed(seed)  # 设置random的种子


def random_num_add(num):  #随机生成num位数字，并返回num位字符串，左侧填充0
    num_str = str(random.randint(10 ** (num - 1), 10 ** num - 1))
    return num_str.zfill(num)


def add_random_to_file_name(file_name, num):
    # 去除后缀，加上_和用random_num_add(num)生成的随机数字后再重新加上后缀
    file_name_list = file_name.split('.')
    file_name_list[-2] += '_' + random_num_add(num)
    file_name = '.'.join(file_name_list)
    return file_name


#识别字符串是不是'.osu'后缀文件的路径，后缀名无视大小写
def if_osu_file(path):
    temp = path.lower()
    if temp.endswith('.osu'):
        return True
    else:
        return False


def key_value(column, keys):
    if keys <= 3 or (keys > 3 and keys % 2 == 0):
        return math.floor((column + 0.5) * 512 / keys)
    if keys > 3 and keys % 2 == 1:
        if column < (keys - 1) / 2:
            return math.floor((column + 0.5) * 512 / (keys - 1))
        if column > (keys - 1) / 2:
            return math.floor((column - 0.5) * 512 / (keys - 1))
        if column == (keys - 1) / 2:
            return 256


def key_value_to_colunm(key_value, keys):
    if keys <= 3 or (keys > 3 and keys % 2 == 0):
        return math.floor(key_value * keys / 512)
    if keys > 3 and keys % 2 == 1:
        if key_value < 256:
            return math.floor(key_value * (keys - 1) / 512)
        if key_value > 256:
            return math.floor(key_value * (keys - 1) / 512) + 1
        if key_value == 256:
            return (keys - 1) / 2


# def osu_file_str_split(str):
#     str_lines = str.split("\n")
#     mata = ""
#     hit_obj = ""
#     # 找到"[HitObjects]"行，把改行及前边所有行赋予mata，改行后所有行赋予hit_obj
#     for i in range(len(str_lines)):
#         if str_lines[i] == "[HitObjects]":
#             mata = str_lines[:i]
#             hit_obj = str_lines[i:]
#             break
#     return mata, hit_obj
def osu_file_str_split1(input_str):
    if not isinstance(input_str, str):
        raise ValueError("输入必须是字符串类型")

    str_lines = input_str.split("\n")

    try:
        index = str_lines.index("[HitObjects]")  # 使用index方法直接查找
    except ValueError:
        return str_lines, []  # 若未找到"[HitObjects]"，返回所有内容和空列表

    mata = str_lines[:index + 1]  # 前面的行
    hit_obj = str_lines[index + 1:]  # 从"[HitObjects]"开始的行
    return mata, hit_obj


#合并矩阵
# def merge_rows(start_time, *MTXs):
#     def is_monotonic_increasing(arr):
#         return np.all(arr[:-1] <= arr[1:])
#
#     def sort_start_time_and_MTXs(start_time, *MTXs):
#         if not is_monotonic_increasing(start_time):
#             sorted_indices = np.argsort(start_time)
#             start_time = start_time[sorted_indices]
#             MTXs = [MTX[sorted_indices] for MTX in MTXs]
#         return start_time, MTXs
#
#     def is_empty(value):
#         return value in [0, 0.0, "0", ""]
#
#     # 检查并排序
#     start_time, MTXs = sort_start_time_and_MTXs(start_time, *MTXs)
#
#     # 合并行
#     unique_times = np.unique(start_time)
#     merged_matrices = [[] for _ in MTXs]
#     merged_start_time = []
#     dtypes = [MTX.dtype for MTX in MTXs]
#
#     for time in unique_times:
#         indices = np.where(start_time == time)[0]
#         if len(indices) > 1:
#             for i, MTX in enumerate(MTXs):
#                 if MTX.dtype.kind in {'U', 'S'}:  # 处理字符串矩阵
#                     merged_row = np.full(MTX.shape[1], "", dtype=MTX.dtype)
#                     for idx in indices:
#                         for col in range(MTX.shape[1]):
#                             if not is_empty(MTX[idx, col]):
#                                 merged_row[col] = MTX[idx, col]
#                 else:  # 处理数值矩阵
#                     merged_row = np.zeros(MTX.shape[1], dtype=MTX.dtype)
#                     for idx in indices:
#                         for col in range(MTX.shape[1]):
#                             if not is_empty(MTX[idx, col]):
#                                 merged_row[col] = MTX[idx, col]
#                 merged_matrices[i].append(merged_row)
#             merged_start_time.append(time)
#         else:
#             for i, MTX in enumerate(MTXs):
#                 merged_matrices[i].append(MTX[indices[0]])
#             merged_start_time.append(time)
#
#     return [np.array(matrix, dtype=dtypes[i]) for i, matrix in enumerate(merged_matrices)], np.array(merged_start_time)

def merge_rows(start_time, *MTXs):
    unique_times = np.unique(start_time)

    # 初始化合并后的结果列表
    merged_MTXs = [[] for _ in range(len(MTXs))]

    for time in unique_times:
        indices = np.where(start_time == time)[0]

        for i, MTX in enumerate(MTXs):
            # 合并数字矩阵
            if np.issubdtype(MTX.dtype, np.number):
                merged_row = np.max(MTX[indices], axis=0)
            else:  # 合并字符串矩阵
                merged_row = []
                for col in range(MTX.shape[1]):
                    values = MTX[indices, col]
                    non_empty = [v for v in values if v not in ["0", "0.0", "", 0]]
                    merged_row.append(max(non_empty, key=lambda x: values.tolist().index(x), default=""))  # 取最新的非空值
            merged_MTXs[i].append(merged_row)

    # 返回合并的结果
    return *[np.array(mtx) for mtx in merged_MTXs], np.array(unique_times)


#比较两个相同长度数组中，相同下标下不同数字的个数
def different_num(list1, list2):
    return sum(1 for x, y in zip(list1, list2) if x != y)


#固定面条的index，抽选60%其他convert_array的index
def random_swap(list_convert, fixed_indices):
    # 从原列表中取出要固定的下标
    fixed_values = [list_convert[i] for i in fixed_indices]
    # 获取要交换的元素及其索引
    swap_indices = [index for index, value in enumerate(list_convert) if value not in fixed_values]
    # 从中抽选出60%的索引
    swap_indices = random.sample(swap_indices, int(len(swap_indices) * 0.6))
    swap_values = [list_convert[i] for i in swap_indices]
    # 随机打乱可交换的元素
    random.shuffle(swap_values)
    # 将固定的元素和打乱的元素合并
    for index, value in zip(swap_indices, swap_values):
        list_convert[index] = value
    return list_convert


#删除狂风插入中因插入而新生成的子弹
def MTX_del_jack(MTX_start_time, MTX, beat_time=400):
    result = MTX.copy()
    weight = result.shape[1]
    height = len(MTX_start_time)
    interval = beat_time / 4 * 1.5 + 2
    if interval < 77:
        interval = 77
    elif interval > 250:
        interval = 250
    # 创建一个标记矩阵用于记录需要修改的元素
    mask = np.zeros_like(result, dtype=bool)
    # 使用np.roll比较相邻行
    shifted_MTX = np.roll(result, shift=1, axis=0)
    different = (result != shifted_MTX)  # 找到不同的元素
    # 检查是否存在 -1
    no_minus_one = (result != -1) & (shifted_MTX != -1)
    # 标记需要修改的元素
    mask[1:, :] = different[1:, :] & no_minus_one[1:, :]
    # 根据 mask 更新 MTX
    for col in range(weight):
        true_indices =np.where(mask[:, col])[0]
        for index in true_indices:
            #初始化第一次
            if MTX_start_time[index] - MTX_start_time[index - 1] < interval:
                mask[index, col] = True
                #后续
                i = 1
                while index + i < height - 1 and MTX_start_time[index + i] - MTX_start_time[index - 1] < interval:
                    mask[index+i, col] = True
                    i += 1
            else:
                mask[index, col] = False
    result[mask] = -1
    return result


#闭包法插入-1和列表
def inserter_m1(lst, num):
    counter = random.randint(0, 1)
    if num == 0:
        return lst

    def insert_minus_one():
        nonlocal counter
        if len(lst) == 0 or len(lst) == 1:
            ml = 0
            mr = 1
        elif len(lst) % 2 == 0:
            ml = len(lst) / 2 - 1
            mr = len(lst) / 2 + 1
        else:
            ml = len(lst) / 2 - 0.5
            mr = len(lst) / 2 + 0.5
        if counter % 2 == 0:  # 插入左边
            index = random.randint(0, int(ml))
            lst.insert(index, -1)
        else:  # 插入右边
            index = random.randint(int(mr), len(lst))
            lst.insert(index, -1)
        counter += 1
        return lst

    for i in range((num - 1)):
        insert_minus_one()

    return insert_minus_one()


#左右左插入index
def inserter_lst(lst, lst_insert):
    counter = random.randint(0, 1)
    lst = lst
    num = len(lst_insert)
    i = 0
    temp = []

    def insert_minus_one():
        nonlocal counter
        nonlocal i
        if len(lst) == 0 or len(lst) == 1:
            ml = 0
            mr = 1
        elif len(lst) % 2 == 0:
            ml = len(lst) / 2 - 1
            mr = len(lst) / 2 + 1
        else:
            ml = len(lst) / 2 - 0.5
            mr = len(lst) / 2 + 0.5
        if counter % 2 == 0:  # 插入左边
            index = random.randint(0, int(ml))
            lst.insert(index, lst_insert[i])
        else:  # 插入右边
            index = random.randint(int(mr), len(lst))
            lst.insert(index, lst_insert[i])
        counter += 1
        return lst

    for i in range(num):
        temp = insert_minus_one()

    return temp


# 抽选位置变-1，用inserter统一命名

def inserter_b1(lst, num):
    counter = random.randint(0, 1)
    lst = lst
    temp = []
    if num == 0:
        return lst

    def insert_minus_one():
        nonlocal counter
        if len(lst) == 0:
            return lst
        elif len(lst) % 2 == 0:
            mr = int(len(lst) / 2)
            ml = mr - 1
        else:
            ml = int(len(lst) / 2 - 0.5)
            mr = ml + 1

        if counter % 2 == 0:
            index = random.randint(0, ml)
            lst[index] = -1
        else:
            index = random.randint(mr, len(lst) - 1)
            lst[index] = -1
        counter += 1
        return lst

    for i in range(num):
        temp = insert_minus_one()

    return temp


def deleter_b1(lst, num):
    counter = random.randint(0, 1)
    lst = lst
    temp = []
    if num == 0:
        return lst

    def delete_one():
        nonlocal counter
        if len(lst) == 0:
            return lst
        elif len(lst) % 2 == 0:
            mr = int(len(lst) / 2)
            ml = mr - 1
        else:
            ml = int(len(lst) / 2 - 0.5)
            mr = ml + 1

        if counter % 2 == 0:
            index = random.randint(0, ml)
            lst.pop(index)
        else:
            index = random.randint(mr, len(lst) - 1)
            lst.pop(index)
        counter += 1
        return lst

    for i in range(num):
        temp = delete_one()

    return temp


#有闭包法删除元素

#密度算法0到10
def MTX_density_b1(matrix, num):
    try:
        # 验证输入的矩阵
        if not isinstance(matrix, np.ndarray):
            raise ValueError("输入的矩阵必须是一个numpy数组。")
        if num >= 10:
            return  # 如果num不大于0，直接返回，不做任何操作
        # 计算列长度，避免重复调用
        elif num == 0:
            #吧所有元素设置为0
            matrix.fill(0)

        else:
            num_columns = matrix.shape[1]
            #生成行长度的随机数

            for i in range(0, matrix.size - matrix.shape[1] - 1, num):  # 以num为步长遍历元素
                step = np.random.randint(1, matrix.shape[1])
                row = (i + step) // num_columns  # 计算当前元素的行索引
                col = (i + step) % num_columns  # 计算当前元素的列索引
                matrix[row, col] = -1  # 将当前元素的值设置为-999
    except Exception as e:
        print(f"发生错误: {e}")


def sanitize_filename(filename):
    # 使用正则表达式替换非法字符
    return re.sub(r'[<>:"/\\|?*]', '_', filename)


#万物化系列
def generate_stream_matrix(height_MTX, to_keys, stream_num=1):
    matrix = np.zeros((height_MTX, to_keys))
    mask = np.zeros((height_MTX, to_keys), dtype=bool)
    for _ in range(stream_num):
        array = np.zeros(height_MTX, dtype=int)  #一行中第几列
        array[0] = np.random.randint(0, to_keys)
        # 初始化方向和计数器
        direction = np.random.choice([-1, 1])
        counter = 0

        # 生成数组的其他位置
        for i in range(1, height_MTX):
            counter_flag = np.random.randint(3, 11)
            # 当i变化大于等于3的时候可以重新选择方向
            if counter == counter_flag:
                direction = - direction
                counter = 0
            new_value = array[i - 1] + direction
            if new_value > to_keys - 1:
                new_value = new_value % to_keys
            elif new_value < 0:
                new_value = to_keys - 1 + (new_value + 1) % to_keys
            array[i] = new_value
            counter += 1
        array_col = list(range(height_MTX))
        mask[array_col, array] = True
    matrix[mask] = 1
    return matrix


def str_to_array(input_string):
    # 将输入字符串按逗号分隔，转换为数字列表
    return [int(num) for num in input_string.split(',')]


def get_in_LN_position(MTX_hold_time, MTX_start_time, flag_out_LN=False):
    MTX = np.maximum.accumulate(MTX_hold_time, axis=0)
    mask = np.zeros_like(MTX, dtype=bool)
    mask[1:] = MTX[1:] > MTX[:-1]
    flag_in_LN = MTX + 100 > MTX_start_time[:, None]
    flag_in_LN[mask & (np.roll(flag_in_LN, 1, axis=0) == False)] = False
    if flag_out_LN:
        return ~flag_in_LN
    else:
        return flag_in_LN


def traverse_and_concat(n):
    # 生成0到n-1的列表
    lst = list(range(n))
    # 从外往中间遍历
    outer_to_middle = []
    left, right = 0, n - 1
    while left <= right:
        outer_to_middle.append(lst[left])
        if left != right:
            outer_to_middle.append(lst[right])
        left += 1
        right -= 1
    # 从中间往外遍历
    middle_to_outer = []
    if n % 2 == 0:
        left, right = (n // 2) - 1, (n // 2)
    else:
        left, right = (n // 2) - 1, (n // 2) + 1
    while left >= 0 and right < n:
        middle_to_outer.append(lst[left])
        middle_to_outer.append(lst[right])
        left -= 1
        right += 1
    # 拼接结果
    result = list(chain(outer_to_middle, middle_to_outer, reversed(outer_to_middle), reversed(middle_to_outer)))
    return result


def insert_itertools(org_keys, add_num):
    pass_flag = [True] * add_num
    array_cycle = []
    for i in range(add_num):
        ran = org_keys + i
        array1 = list(range(ran))
        n = len(array1)
        array1 = array1 + [n] + array1[n - 1:0:-1]
        iter_tem = cycle(array1)
        array_cycle.append(iter_tem)

    def general_lst():
        nonlocal pass_flag, array_cycle
        for i in range(add_num):
            if pass_flag[i]:
                pass_num = random.randint(0, (org_keys + i) * 2 - 2)
                for num in range(pass_num):
                    next(array_cycle[i])
                pass_flag[i] = False

        return [next(array_cycle[x]) for x in range(add_num)]

    return general_lst


def insert_blank_itertools(org_keys, add_num):
    pass_flag = [True] * add_num
    array_cycle = []
    pass_numbers = []
    for i in range(add_num):
        array1 = traverse_and_concat(org_keys + i + 1)
        array_cycle.append(cycle(array1))
    pass_num = random.randint(0, (org_keys + 1 + 1))
    for i in (range(add_num)):
        pass_numbers.append(pass_num + i)

    def general_lst():
        nonlocal pass_flag, array_cycle
        for i in range(add_num):
            if pass_flag[i]:
                for num in range(pass_num[i]):
                    next(array_cycle[i])
                pass_flag[i] = False
        return [next(array_cycle[x]) for x in range(add_num)]

    return general_lst


def delete_itertools(org_keys, del_num):
    pass_flag = [True] * del_num
    array_cycle = []
    for i in range(del_num):
        ran = org_keys - i
        array1 = list(range(ran))
        n = len(array1)
        array1 = array1 + array1[n - 2:0:-1]
        iter_tem = cycle(array1)
        array_cycle.append(iter_tem)

    def general_lst():
        nonlocal pass_flag, array_cycle
        for i in range(del_num):
            if pass_flag[i]:
                pass_num = random.randint(0, (org_keys + i) * 2 - 2)
                for num in range(pass_num):
                    next(array_cycle[i])
                pass_flag[i] = False

        return [next(array_cycle[x]) for x in range(del_num)]

    return general_lst


def become_m_itertools(org_keys, become_num):
    pass_flag = [True] * become_num
    array_cycle = []
    array1 = traverse_and_concat(org_keys)
    numbers = list(range(org_keys))
    array_cycle = tee(array1, become_num)

    def general_lst():
        nonlocal pass_flag, array_cycle
        pass_num = random.sample(numbers, become_num)
        for i in range(become_num):
            if pass_flag[i]:
                for _ in range(pass_num[i]):
                    next(array_cycle[i])
                pass_flag[i] = False

        return [next(array_cycle[x]) for x in range(become_num)]

    return general_lst


## 7 to 10


def format_milliseconds(milliseconds):
    # 计算总秒数
    total_seconds = milliseconds // 1000
    remaining_milliseconds = milliseconds % 1000

    # 计算分钟和秒
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    # 将毫秒转换为字符串并补零
    formatted_milliseconds = f"{remaining_milliseconds:03}"

    # 输出格式
    formatted_time = f"{minutes:02}:{seconds:02}:{formatted_milliseconds}"
    return formatted_time
