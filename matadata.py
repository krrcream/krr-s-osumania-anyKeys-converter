"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""
from functions import *

class MataData:
    #lines 传入按行分割好的文本
    def __init__(self, lines):
        self.mata = lines
        self.keys = [
            "AudioFilename", "Title", "Artist", "Creator",
            "Version", "Source", "Tags", "BeatmapID", "BeatmapSetID", "HPDrainRate", "CircleSize", "OverallDifficulty",
            "Background", "beat_time"
        ]
        # 初始化字典来存储键值对
        self.data = {"AudioFilename": "null",
                     "Title": "null",
                     "Artist": "null",
                     "Creator": "null",
                     "Version": "null",
                     "Source": "null",
                     "Tags": "null",
                     "BeatmapID": "null",
                     "BeatmapSetID": "null",
                     "HPDrainRate": "null",
                     "CircleSize": "null",
                     "OverallDifficulty": "null",
                     "Background": "null",
                     "beat_time": "null"  #默认bpm150
                     }

        event_flag = False  # 标记是否在 [Events] 区块内
        time_flag = False  # 标记是否在 [TimingPoints] 区块内
        for key in self.keys:
            i = 0  # 这是行数
            title_flag = 0
            artist_flag = 0
            for i in range(len(lines)):
                if key in lines[i] and key != "Background" and key != "part_time":
                    try:
                        self.data[key] = [lines[i].split(':', 1)[1], i]
                        break
                    except IndexError:
                        print(f"{self.data['Title']} error:{key}")
                        break

                if event_flag == False and "Background and Video event" in lines[i]:  #获得背景图片路径
                    event_flag = True
                    if "0,0," in lines[i + 1] and ",0,0" in lines[i + 1]:  #背景图片路径
                        self.data['Background'] = [lines[i + 1][5:-5], i + 1]  #lines[i + 1] 去掉前5个字符和后5个字符
                        break
                if time_flag == False and lines[i].strip() == "[TimingPoints]":  #获得节拍时间
                    time_flag = True
                    # 获取下一行并去掉首尾空格
                    timing_line = lines[i + 1].strip()
                    # 分割字符串
                    parts = timing_line.split(',')
                    if float(parts[1]) < 187.5 or float(parts[1]) > 1000:  #如果BPM大于320或者小于60，给默认值150
                        self.data['beat_time'] = [400, i + 1]
                    else:
                        self.data['beat_time'] = [float(parts[1]), i + 1]
                    break
        # 如果"krrcream converter"不在self.data['Tags'][0]:中，则加上
        if "krrcream converter" not in self.data['Tags'][0]:
            self.data['Tags'][0] = "krrcream converter " + self.data['Tags'][0]
        if "krr conv. & " not in self.data['Creator'][0]:
            self.data['Creator'][0] = "krr conv. " + self.data['Creator'][0]
        self.data['BeatmapSetID'][0] = -1
        self.data['BeatmapID'][0] = 0
        self.set_data("Tags", self.data['Tags'][0])
        self.set_data("Creator", self.data['Creator'][0])
        self.set_data("BeatmapSetID", self.data['BeatmapSetID'][0])
        self.set_data("BeatmapID", self.data['BeatmapID'][0])
    def print_data(self):
        for key, value in self.data.items():
            print(f"{key}: {value}")

    def get_data(self, key):
        return self.data[key]

    def set_data(self, key, new_value):
        self.data[key][0] = new_value
        if key == "Background" and self.data[key][0] != "null":
            self.mata[self.data[key][1]] = f'0,0,"{new_value}",0,0'
        elif key == "Title":
            self.mata[self.data[key][1]] = f"{key}:{new_value}"
            self.mata[self.data[key][1] + 1] = f"{key}Unicode:{new_value}"
        elif key == "Artist":
            self.mata[self.data[key][1]] = f"{key}:{new_value}"
            self.mata[self.data[key][1] + 1] = f"{key}Unicode:{new_value}"
        else:
            self.mata[self.data[key][1]] = f"{key}:{new_value}"

    def get_new_lines(self):
        return self.mata

    def get_save_file_name(self):
        artist = sanitize_filename(self.data["Artist"][0])
        title = sanitize_filename(self.data["Title"][0])
        creator = sanitize_filename(self.data["Creator"][0])
        version = sanitize_filename(self.data["Version"][0])

        file_name_osu = f"{artist} - {title} ({creator}) [{version}].osu"
        file_name_audio = self.data["AudioFilename"][0].strip()
        file_name_BG = self.data["Background"][0]
        return file_name_osu, file_name_audio, file_name_BG
