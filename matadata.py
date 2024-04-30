import re


# 等待优化，metadata处有问题 title重复出现，现直接在文本里替换可使用
class MataData:
    def __init__(self, lines):
        self.mata = lines
        global bg_file
        self.keys = [
            "AudioFilename", "Title", "Artist", "Creator",
            "Version", "Source", "Tags", "BeatmapID", "BeatmapSetID", "HPDrainRate", "CircleSize", "OverallDifficulty"
        ]
        # 初始化字典来存储键值对
        self.data = {"AudioFilename": "null", "Title": "null", "Artist": "null",
                     "Creator": "null",
                     "Version": "null", "Source": "null", "Tags": "null", "BeatmapID": "null", "BeatmapSetID": "null",
                     "HPDrainRate": "null", "CircleSize": "null", "OverallDifficulty": "null", "Background": "null"}
        for key in self.keys:
            i = 0  # 这是行数
            for i in range(len(lines)):
                if key in lines[i] and "Unicode" not in lines[i] and key != "Background":

                    try:
                        self.data[key] = [lines[i].split(':', 1)[1], i]
                    except IndexError:
                        break


        x = [(index, line) for index, line in enumerate(lines) if "Background and Video events" in line]
        if x:
            index = x[0][0]+1
            if self.extract_full_image_filenames(self.mata[index]):
                bg_file = self.extract_full_image_filenames(self.mata[index])
                self.mata[index] = f'0,0,"{bg_file}",0,0'
                self.data["Background"] = [bg_file, index]

            else:
                bg_file = "null.jpg"
                lines.insert(index+1, f'0,0,"{bg_file}",0,0')
                self.data["Background"] = [bg_file, index]

        print(self.data["Background"])
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def extract_full_image_filenames(self,text):
        pattern = r'(.*)\b\w+\.(jpg|jpeg|png|gif|bmp)\b'
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0).split('"')[1]
        else:
            return None
    def meta_alter(self, key1, new_value):
        # if key1 == "Title" or "Artist":
        #     self.mata_new[self.data[key1][1]-1] = f"{key1}:{new_value}"
        if key1 == "Background":
            self.mata[self.data[key1][1]] = f'0,0,"{new_value}",0,0'
        elif key1 == "Title":
            self.mata[self.data[key1][1]] = f"{key1}:{new_value}"
            self.mata[self.data[key1][1]+1] = f"{key1}Unicode:{new_value}"
        elif key1 == "Artist":
            self.mata[self.data[key1][1]] = f"{key1}:{new_value}"
            self.mata[self.data[key1][1]+1] = f"{key1}Unicode:{new_value}"
        else:
            self.mata[self.data[key1][1]] = f"{key1}:{new_value}"

    def get_new_lines(self):
        return self.mata

    # def artist_bug_repair(self,original_string):
    #     # 找到第一个"Title:"出现的位置
    #     first_title_pos = original_string.find("Title:")
    #     # 找到第二个"Title:"出现的位置
    #     second_title_pos = original_string.find("Title:", first_title_pos + 1)
    #     # 如果找到了第二个"Title:"，则进行修改
    #     if second_title_pos != -1:
    #         # 确定修改的内容
    #         new_content = "Artist:"
    #         # 截取第一部分文本，直到第二个"Title:"
    #         pre_second_title = original_string[:second_title_pos]
    #         # 截取从第二个"Title:"之后到字符串末尾的部分
    #         post_second_title = original_string[second_title_pos + len("Title:"):]
    #         # 拼接新的字符串
    #         new_string = pre_second_title + new_content + post_second_title
    #         return new_string
    #     else:
    #         return original_string


test_string = """osu file format v12

[General]
AudioFilename: Lv19 Akasagarbha.mp3
AudioLeadIn: 0
PreviewTime: -1
Countdown: 0
SampleSet: Soft
StackLeniency: 0.7
Mode: 3
LetterboxInBreaks: 1

[Editor]
DistanceSpacing: 2
BeatDivisor: 12
GridSize: 16

[Metadata]
Title:Akasagarbha
TitleUnicode:Akasagarbha
Artist:wa. vs ETIA.
ArtistUnicode:wa. vs ETIA.
Creator:Davteezy
Version:Lv.19
Source:BMS
Tags:
BeatmapID:0
BeatmapSetID:-1

[Difficulty]
HPDrainRate:7
CircleSize:7
OverallDifficulty:7
ApproachRate:5
SliderMultiplier:1.4
SliderTickRate:1

[Events]
//Background and Video events
0,0,"_title.png",0,0
//Break Periods
//Storyboard Layer 0 (Background)
//Storyboard Layer 1 (Fail)
//Storyboard Layer 2 (Pass)
//Storyboard Layer 3 (Foreground)
//Storyboard Sound Samples
Sample,2500,0,"pad_in_a1.wav",70
Sample,12578,0,"hat1.wav",70
Sample,12656,0,"hat1.wav",70
Sample,12812,0,"hat1.wav",70
Sample,12890,0,"hat1.wav",70
Sample,13125,0,"hat1.wav",70
Sample,13203,0,"hat1.wav",70
Sample,13281,0,"hat1.wav",70
Sample,13437,0,"hat1.wav",70
Sample,13515,0,"hat1.wav",70
Sample,13593,0,"hat1.wav",70
Sample,12656,0,"hat2.wav",70
Sample,12968,0,"hat2.wav",70
Sample,13281,0,"hat2.wav",70
Sample,13593,0,"hat2.wav",70
Sample,12812,0,"clap1.wav",70
Sample,13437,0,"clap1.wav",70
Sample,12656,0,"bass1.wav",70
Sample,12968,0,"bass1.wav",70
Sample,13281,0,"bass1.wav",70
Sample,13593,0,"bass1.wav",70
Sample,13828,0,"hat1.wav",70
Sample,14140,0,"hat1.wav",70
Sample,14453,0,"hat1.wav",70
Sample,14531,0,"hat1.wav",70
Sample,14765,0,"hat1.wav",70
Sample,14843,0,"hat1.wav",70
Sample,13906,0,"hat2.wav",70
Sample,14218,0,"hat2.wav",70
Sample,14531,0,"hat2.wav",70
Sample,14843,0,"hat2.wav",70
Sample,14062,0,"clap1.wav",70
Sample,14687,0,"clap1.wav",70
Sample,13906,0,"bass2.wav",70
Sample,14218,0,"bass2.wav",70
Sample,14531,0,"bass4.wav",70
Sample,14843,0,"bass5.wav",70
Sample,15078,0,"hat1.wav",70"""


# mata = MataData(test_string.split('\n'))
# mata.meta_alter("Title", "测试")
# mata.meta_alter("Artist", "艺术家")
# mata.meta_alter("Background", "333422.jpg")
# print(mata.data["Background"])
# new_lines = mata.get_new_lines()
# for line in new_lines:
#     print(line)