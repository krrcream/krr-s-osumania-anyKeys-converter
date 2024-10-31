"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""
import os

import hitobject
from functions import *
from hitobject import *
from concurrent.futures import ThreadPoolExecutor


def NtoNC_convert_array(keys, to_keys, blank):
    # 初始化一个 [0, 1, 2, ..., keys-1] 的数组
    keys_list = list(range(keys))
    if keys < to_keys:
        add_num = to_keys - keys
        add = random.choices(keys_list, k=add_num - blank)
        become = 0
        add_blank_num = 0
        # 将 add 中的数字随机插入到 keys_list 中
        iteradd = insert_itertools(keys, add_num - blank)
        indices = iteradd()
        for i, index in enumerate(indices):
            keys_list.insert(index, add[i])

        if blank > 0:
            if blank + keys <= to_keys:
                add_blank_num = blank
            else:
                add_blank_num = to_keys - keys - blank
                become = blank - (to_keys - keys)
        if add_blank_num > 0:
            keys_list = inserter_m1(keys_list, add_blank_num)
        if become > 0:
            keys_list = inserter_b1(keys_list, become)
        return keys_list
    elif keys == to_keys:
        return keys_list
    elif keys > to_keys:
        while len(keys_list) > to_keys:
            keys_list = deleter_b1(keys_list, keys - to_keys)
        keys_list = inserter_b1(keys_list, blank)
        return keys_list


# def NtoNC_convert_array(keys, to_keys, blank): 老办法备份
#     # 初始化一个 [0, 1, 2, ..., keys-1] 的数组
#     keys_list = list(range(keys))
#     if keys + blank < to_keys:
#         add_num = to_keys - keys - blank
#         add_list = random.choices(keys_list, k=int(add_num))
#         # 将 add_list 中的数字随机插入到 keys_list 中
#         keys_list = inserter_lst(keys_list, add_list)
#         # 插入 blank 个 -1
#         keys_list = inserter_m1(keys_list, blank)
#         return keys_list
#     elif keys + blank == to_keys:
#         keys_list = inserter_m1(keys_list, blank)
#         return keys_list
#     elif keys <= to_keys < keys + blank:
#         keys_list = inserter_m1(keys_list, to_keys - keys)
#         keys_list = inserter_b1(keys_list, blank + keys - to_keys)
#         return keys_list
#     elif keys > to_keys:  # 从keys_list中在左半边和右半边轮流删除数字，直到长度为to_keys
#         while len(keys_list) > to_keys:
#             keys_list = deleter_b1(keys_list, keys - to_keys)
#         keys_list = inserter_b1(keys_list, blank)
#         return keys_list


# def NtoNC_convert_MTX(keys,to_keys,blank, MTX_start_time, Interval=400, different_num_Ratio=0.5):
#     convert_MTX = []
#     #执行NtoNC_convert_array(keys,to_keys,blank)得到第一个list
#     list1 = NtoNC_convert_array(keys,to_keys,blank)
#     convert_MTX.append(list1)
#     # 从第二个MTX_start_time开始,计算每个start_time减去上一个start_time，得到间隔时间
#     time_flag = 0
#     for i in range(1,len(MTX_start_time)):
#         time_flag += (MTX_start_time[i] - MTX_start_time[i-1])
#         # 如果间隔时间小于Interval，则将上一个list复制到当前位置，并加上间隔时间
#         if time_flag < Interval:
#             convert_MTX.append(convert_MTX[-1])
#         else:
#             temp = NtoNC_convert_array(keys,to_keys,blank)
#             if different_num(temp,convert_MTX[-1]) > to_keys * different_num_Ratio:
#                 flag = True
#                 while flag:
#                     temp = NtoNC_convert_array(keys,to_keys,blank)
#                     if different_num(temp,convert_MTX[-1]) <= to_keys * different_num_Ratio:
#                         flag = False
#             convert_MTX.append(temp)
#     return convert_MTX

# 生成新的class HitObjects:并继承hitobject.py中HitObjects的属性和方法
class NtoNC_HitObjects(hitobject.HitObjects):

    def NtoNC_convert_MTX(self, to_keys, blank, Interval=1600, beat_time=400, del_jack_flag=True, density=10,
                          different_num_ratio=0.5):

        keys = self.keys
        convert_MTX = []
        list1 = NtoNC_convert_array(keys, to_keys, blank)
        convert_MTX.append(list1)
        time_intervals = [self.MTX_start_time[i] - self.MTX_start_time[i - 1] for i in
                          range(1, len(self.MTX_start_time))]
        time_flag = 0
        with ThreadPoolExecutor(max_workers=min(os.cpu_count() + 4, 4)) as executor:  # 使用线程池并行处理
            for i, interval_time in enumerate(time_intervals, start=1):
                time_flag += interval_time
                if time_flag >= Interval:
                    try:
                        temp = executor.submit(NtoNC_convert_array, keys, to_keys, blank).result()  # 并行生成新列表
                        count = 0
                        while (different_num(temp, convert_MTX[-1]) > to_keys * different_num_ratio) and (count < 4):
                            count += 1
                            temp = executor.submit(NtoNC_convert_array, keys, to_keys, blank).result()
                    except Exception as e:
                        temp = convert_MTX[-1][:]  # 出现错误时，使用上一个结果
                    time_flag = 0
                else:
                    temp = convert_MTX[-1][:]  # 间隔时间不够，使用上一个结果
                convert_MTX.append(temp)
        convert_MTX = np.array(convert_MTX)
        convert_hold_time_MTX = self.MTX_hold_time[np.arange(self.MTX_hold_time.shape[0])[:, None], convert_MTX][
                                :]  # 更新convert_hold_time
        convert_in_LN_MTX = get_in_LN_position(convert_hold_time_MTX, self.MTX_start_time)  # 获取面条中的位置
        convert_MTX[convert_in_LN_MTX] = -1
        if del_jack_flag:
            convert_MTX = MTX_del_jack(self.MTX_start_time, convert_MTX, beat_time)

        if 0 <= density < 10:
            MTX_density_b1(convert_MTX, density)

        return convert_MTX
