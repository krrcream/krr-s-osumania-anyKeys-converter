"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""
import numpy as np

def generate_stream_matrix(height_MTX, to_keys, stream_num=1, jack_use=False):
    matrix = np.zeros((height_MTX, to_keys))
    mask = np.zeros((height_MTX, to_keys), dtype=bool)
    for _ in range(stream_num):
        array = np.zeros(height_MTX, dtype=int)
        array[0] = np.random.randint(0, to_keys)
        # 初始化方向和计数器
        direction = np.random.choice([-1, 1])
        counter = 0
        # 生成数组的其他位置
        for i in range(0, height_MTX):
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
            cound_flag = 0
            while mask[i, new_value] and cound_flag < 10:
                if jack_use:
                    false_indices = np.where(~mask[i])[0]
                    new_value = np.random.choice(false_indices)
                else:  # 寻找上下两行都是false的列重新插入
                    if i == 0:
                        valid_columns = mask[i + 1, :] == False
                    elif i == height_MTX - 1:
                        valid_columns = mask[i - 1, :] == False
                    else:
                        valid_columns = (mask[i - 1, :] == False) & (mask[i + 1, :] == False)
                    index = np.where(valid_columns)[0]
                    if index.size > 0:
                        new_value = np.random.choice(index)
                    cound_flag += 1

            array[i] = new_value
            counter += 1
            mask[i, array[i]] = True
    matrix[mask] = 1
    return matrix


def generate_jack_matrix(height_MTX, to_keys, blank_num=1):
    matrix = np.ones((height_MTX, to_keys))
    mask = np.zeros((height_MTX, to_keys), dtype=bool)
    for _ in range(blank_num):
        array = np.ones(height_MTX, dtype=int)
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
    matrix[mask] = 0
    return matrix


def check_jack_matrix(matrix):
    consecutive = (matrix[:-1, :] == 1) & (matrix[1:, :] == 1)
    result = matrix.copy()
    result[:-1, :][consecutive] = 0
    return result


def check_blank_row(matrix, add_num=1):
    rows_with_few_ones = np.where(np.sum(matrix == 1, axis=1) < add_num)[0]
    height_MTX = matrix.shape[0]
    result = matrix.copy()
    for row in rows_with_few_ones:
        #寻找上下两行都是0的列重新插入
        if row == 0:
            valid_columns = result[row + 1, :] == 0
        elif row == height_MTX - 1:
            valid_columns = result[row - 1, :] == 0
        else:
            valid_columns = (result[row - 1, :] == 0) & (result[row + 1, :] == 0)
        index = np.where(valid_columns)[0]
        if index.size > 0:
            num_to_add = min(add_num, index.size)
            new_values = np.random.choice(index, num_to_add, replace=False)
            result[row, new_values] = 1
    return result


def add_noise(matrix, noise_rate=0.1):
    noise_num = int(matrix.size * noise_rate)
    noise_index = np.random.choice(matrix.size, noise_num, replace=False)
    noise_prob = np.random.rand(noise_num)  # 生成 [0, 1) 之间的随机数
    noise_value = (noise_prob < (0.5 + 0.5 * noise_prob)).astype(int)  # 根据概率生成噪声值
    matrix.flat[noise_index] = noise_value
    return matrix


def generate_matrix_everything_to_stream(height_MTX, to_keys, stream_num=1, noise_num=0):
    add_num = 1 if stream_num == 1 else stream_num - 1
    matrix = generate_stream_matrix(height_MTX, to_keys, stream_num)
    matrix = add_noise(matrix, noise_num)
    matrix = check_jack_matrix(matrix)
    matrix = check_blank_row(matrix, add_num)
    return matrix.astype(int)


def generate_matrix_everything_to_jack(height_MTX, to_keys, jack_num=1, noise_num=0):
    jack_num = 1 if to_keys - jack_num == 1 else to_keys - jack_num
    result = generate_stream_matrix(height_MTX, to_keys, jack_num, True)
    result = 1 - result
    result = add_noise(result, noise_num)
    return result.astype(int)


###加键系列
def get_vertical_coordinates(matrix):  # 获取纵向为1的坐标
    vertical_coords = []
    for col in range(matrix.shape[1]):  # 遍历每一列
        rows_with_1 = np.where(matrix[:, col] == 1)[0]  # 找到该列中为1的行索引
        if rows_with_1.size > 0:
            vertical_coords.append((rows_with_1.tolist(), col))
    return vertical_coords


# 获取横向为1的坐标
def get_horizontal_coordinates(matrix):  # 获取横向为1的坐标
    horizontal_coords = []
    for row in range(matrix.shape[0]):  # 遍历每一行
        cols_with_1 = np.where(matrix[row, :] == 1)[0]  # 找到该行中为1的列索引
        if cols_with_1.size > 0:
            horizontal_coords.append((row, cols_with_1.tolist()))
    return horizontal_coords


def update_matrix_mask(matrix, vertical_density=0.5,
                       horizontal_density=0,
                       vertical_add_num=1, ):
    vertical_coordinates = get_vertical_coordinates(matrix)
    horizontal_coordinates = get_horizontal_coordinates(matrix)
    #建立一个mask矩阵，全是false
    mask = np.zeros(matrix.shape, dtype=bool)
    # 处理横向坐标
    # 处理纵向坐标
    for rows, col in vertical_coordinates:
        num_to_select = int(len(rows) * vertical_density)  # 选择的数量
        # 使用 np.random.choice 进行随机抽样，注意用 replace=False 不重复选择
        selected_rows = np.random.choice(rows, size=num_to_select, replace=False)

        # 在这些行的纵向坐标加1的位置生成1
        for row in selected_rows:
            if row + 1 + vertical_add_num < matrix.shape[0] and matrix[row + 1 + vertical_add_num, col] == 0:  # 确保不越界
                for j in range(vertical_add_num):
                    mask[row + j, col] = True  # 在纵向坐标+1的位置生成1

    if horizontal_density > 0:
        for row, cols in horizontal_coordinates:
            add_to = matrix.shape[1] * horizontal_density
            if len(cols) < add_to:
                num_to_add = add_to - len(cols)  # 需要添加的数量
                available_cols = [c for c in range(matrix.shape[1]) if c not in cols]  # 可用的列
                if len(available_cols) >= num_to_add:  # 确保有足够的可用列
                    selected_cols = np.random.choice(available_cols, size=int(num_to_add), replace=False)  # 随机选择要添加的列
                    for col in selected_cols:
                        mask[row, col] = True  # 将这些列对应的行设置为1
    return mask


def update_matrix(matrix, mask_update, mask_no_in_LN):
    result = matrix.copy()
    mask_update_true = np.where(mask_update & mask_no_in_LN)
    result[mask_update_true] = 1
    return result
