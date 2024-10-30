"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""
from NtoNC_HitObjects import *
from concurrent.futures import ThreadPoolExecutor


class Preset_HitObjects(NtoNC_HitObjects):

    def NKDPTOOL(self):
        array = list(range(self.keys))
        return array * 2

    def NKDPMTOOL(self):
        array = list(range(self.keys))
        return array + array[::-1][:]

    def fourK_to7(self):
        pass_flag = True
        array = [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
        array_cycle = cycle(array)
        convert_list = [[0, 1, 2, 3, 0, 1, 2],
                        [0, 1, 2, 3, 2, 1, 0],
                        [0, 1, 2, 3, 3, 2, 1],
                        [0, 1, 2, 3, 1, 2, 3],
                        [3, 2, 1, 0, 1, 2, 3],
                        [1, 2, 3, 0, 1, 2, 3],
                        [2, 1, 0, 0, 1, 2, 3],
                        [0, 1, 2, 0, 1, 2, 3]]

        def general_lst():
            nonlocal pass_flag, array_cycle
            if pass_flag:
                pass_num = random.randint(0, 14)
                for i in range(pass_num):
                    next(array_cycle)
                pass_flag = False
            return convert_list[next(array_cycle)][:]

        return general_lst

    def fourK_to7to_10K(self):
        pass_flag = True
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3,
                 2, 1]
        array_cycle = cycle(array)
        convert_list = [[-1, 0, 1, 2, 3, 0, 1, -1, 2],
                        [0, -1, 1, 2, 3, 2, 1, 0, -1],
                        [-1, 0, 1, 2, 3, 3, 2, -1, 1],
                        [0, -1, 1, 2, 3, 1, 2, 3, -1],
                        [-1, 3, 2, 1, 0, 1, 2, -1, 3],
                        [1, -1, 2, 3, 0, 1, 2, 3, -1],
                        [-1, 2, 1, 0, 0, 1, 2, -1, 3],
                        [0, -1, 1, 2, 0, 1, 2, 3, -1],
                        [-1, 0, 1, 2, 3, 0, 1, -1, 2],
                        [0, -1, 1, 2, 3, 2, 1, 0, -1],
                        [-1, 0, 1, 2, 3, 3, 2, -1, 1],
                        [0, -1, 1, 2, 3, 1, 2, 3, -1],
                        [-1, 3, 2, 1, 0, 1, 2, -1, 3],
                        [1, -1, 2, 3, 0, 1, 2, 3, -1],
                        [-1, 2, 1, 0, 0, 1, 2, -1, 3],
                        [0, -1, 1, 2, 0, 1, 2, 3, -1]]

        def general_lst():
            nonlocal pass_flag, array_cycle
            if pass_flag:
                pass_num = random.randint(0, 17)
                for i in range(pass_num):
                    next(array_cycle)
                pass_flag = False
            return convert_list[next(array_cycle)][:]

        return general_lst

    # iter1 = fourK_to7to_10K_iter()
    # for i in range(20):
    #     print(iter1())

    ## 4kdp 10
    def fourK_dp_to_10K(self):
        pass_flag = True
        array = [0, 1, 2, 3, 4, 3, 2, 1]
        array_cycle1, array_cycle2 = tee(cycle(array), 2)
        convert_list = [[-1, 0, 1, 2, 3],
                        [0, -1, 1, 2, 3],
                        [0, 1, -1, 2, 3],
                        [0, 1, 2, -1, 3],
                        [0, 1, 2, 3, -1]]

        def general_lst():
            nonlocal pass_flag, array_cycle1, array_cycle2
            if pass_flag:
                pass_num1, pass_num2 = random.randint(0, 7), random.randint(0, 7)
                for _ in range(pass_num1):
                    next(array_cycle1)
                for _ in range(pass_num2):
                    next(array_cycle2)
                pass_flag = False
            return convert_list[next(array_cycle1)][:] + convert_list[next(array_cycle2)][:]

        return general_lst

    # iter1 = fourKDP_to_10K()
    # for i in range(20):
    #     print(iter1())

    # 4KDPM TO 10K
    def fourK_dpm_to_10K(self):
        pass_flag = True
        array = [0, 1, 2, 3, 4, 3, 2, 1]
        array_cycle1, array_cycle2 = tee(cycle(array), 2)
        convert_list_l = [[-1, 0, 1, 2, 3],
                          [0, -1, 1, 2, 3],
                          [0, 1, -1, 2, 3],
                          [0, 1, 2, -1, 3],
                          [0, 1, 2, 3, -1]]

        convert_list_r = [[-1, 3, 2, 1, 0],
                          [3, -1, 2, 1, 0],
                          [3, 2, -1, 1, 0],
                          [3, 2, 1, -1, 0],
                          [3, 2, 1, 0, -1]]

        def general_lst():
            nonlocal pass_flag, array_cycle1, array_cycle2
            if pass_flag:
                pass_num1, pass_num2 = random.randint(0, 7), random.randint(0, 7)
                for _ in range(pass_num1):
                    next(array_cycle1)
                for _ in range(pass_num2):
                    next(array_cycle2)
                pass_flag = False
            return convert_list_l[next(array_cycle1)][:] + convert_list_r[next(array_cycle2)][:]

        return general_lst

    def sixK_to_10K(self):
        if self.keys != 6:
            return False
        array_l = [0, 1, 2]
        array_r = [3, 4, 5]
        array_l.insert(random.randint(0, 3), -1)
        array_r.insert(random.randint(0, 3), -1)
        array_l.insert(random.randint(0, 4), -1)
        array_r.insert(random.randint(0, 4), -1)
        return array_l + array_r

    def sevenK_to_10K(self):
        pass_flag = True
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        array_cycle = cycle(array)
        convert_list = [[-1, 6, 0, 1, 2, 3, 4, 5, -1, 6],
                        [0, -1, 5, 1, 2, 3, 4, 5, 6, -1],
                        [-1, 0, 1, 4, 2, 3, 4, 5, -1, 6],
                        [0, -1, 1, 2, 3, 3, 4, 5, 6, -1],
                        [-1, 0, 1, 2, 3, 2, 4, 5, -1, 6],
                        [0, -1, 1, 2, 3, 4, 1, 5, 6, -1],
                        [-1, 0, 1, 2, 3, 4, 5, 0, -1, 6],
                        [0, -1, 1, 2, 3, 4, 5, 6, 0, -1],
                        [-1, 0, 1, 2, 3, 4, 5, 1, -1, 6],
                        [0, -1, 1, 2, 3, 4, 2, 5, 6, -1],
                        [-1, 0, 1, 2, 3, 3, 4, 5, -1, 6],
                        [0, -1, 1, 2, 4, 3, 4, 5, 6, -1],
                        [-1, 0, 1, 5, 2, 3, 4, 5, -1, 6],
                        [0, -1, 6, 1, 2, 3, 4, 5, 6, -1]]

        def general_lst():
            nonlocal pass_flag, array_cycle
            if pass_flag:
                pass_num1 = random.randint(0, 13)
                for _ in range(pass_num1):
                    next(array_cycle)
                pass_flag = False
            return convert_list[next(array_cycle)][:]

        return general_lst

    def fourK_to6to_10K(self):
        if self.keys != 4:
            return False
        array = [0, 1, 2, 3]
        array_l = array.copy()
        array_l.pop(random.randint(0, 3))
        array_r = array.copy()
        array_r.pop(random.randint(0, 3))
        array_l.insert(random.randint(0, 3), -1)
        array_r.insert(random.randint(0, 3), -1)
        array_l.insert(random.randint(0, 4), -1)
        array_r.insert(random.randint(0, 4), -1)
        return array_l + array_r

    def preset_convert_MTX(self, func=None, Interval=500, beat_time=400, del_jack_flag=True,
                           density=10):
        converter = func()
        # 检查返回值的类型
        if isinstance(converter, (list, tuple)):  # 如果是列表或元组
            converter = func  # 直接赋值

        list1 = converter()
        convert_MTX = []
        convert_MTX.append(list1)
        time_intervals = [self.MTX_start_time[i] - self.MTX_start_time[i - 1] for i in
                          range(1, len(self.MTX_start_time))]
        time_flag = 0
        with ThreadPoolExecutor(max_workers=min(os.cpu_count() + 4, 4)) as executor:  # 使用线程池并行处理
            for i, interval_time in enumerate(time_intervals, start=1):
                time_flag += interval_time
                if time_flag >= Interval:
                    try:
                        temp = executor.submit(converter).result()  # 并行生成新列表

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
