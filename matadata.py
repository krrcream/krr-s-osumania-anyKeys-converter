import re

# 等待优化，metadata处有问题 title重复出现，现直接在文本里替换可使用
class MataData:
    def __init__(self,lines):
        self.keys = [
            "AudioFilename", "TitleUnicode", "ArtistUnicode", "Creator",
            "Version", "Source", "Tags", "BeatmapID", "BeatmapSetID", "HPDrainRate", "CircleSize", "OverallDifficulty"
        ]
        # 初始化字典来存储键值对
        self.data = {"AudioFilename": "null", "TitleUnicode": "null", "ArtistUnicode": "null",
                 "Creator": "null",
                "Version": "null", "Source": "null", "Tags": "null", "BeatmapID": "null", "BeatmapSetID": "null",
                "HPDrainRate": "null", "CircleSize": "null", "OverallDifficulty": "null", "Background": "null"}
        self.mata_new = lines
        for key in self.keys:
            i = 0  # 这是行数
            for i in range(len(lines)):
                if key in lines[i]:
                    try:
                        self.data[key] = [lines[i].split(':', 1)[1], i]
                    except IndexError:
                        break
        # 正则表达式匹配 //Background and Video events 下的所有行
        pattern = r'\/\/Background and Video events\n(.*?)(?=\n\/\/|$)'
        # 使用正则表达式查找所有匹配项
        matches = re.findall(pattern, "\n".join(lines), re.DOTALL)
        # 提取文件名
        file_name = [match for match in matches if match]
        for part in str(file_name).split(","):
            if part.startswith('"') and part.endswith('"'):
                file_name = part[1:-1]  # 引号
                break
        for i in range(len(lines)):
            try:
                if file_name in lines[i]:
                    self.data["Background"] = [file_name,i]
                    break
            except TypeError:
                print("文件背景格式不对，请重新保存osu文件更新格式")
                break

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def meta_alter(self, key1, new_value):
        # if key1 == "Title" or "Artist":
        #     self.mata_new[self.data[key1][1]-1] = f"{key1}:{new_value}"

        self.mata_new[self.data[key1][1]] = f"{key1}:{new_value}"


    def get_new_lines(self):
        return self.mata_new

    def artist_bug_repair(self,original_string):
        # 找到第一个"Title:"出现的位置
        first_title_pos = original_string.find("Title:")
        # 找到第二个"Title:"出现的位置
        second_title_pos = original_string.find("Title:", first_title_pos + 1)
        # 如果找到了第二个"Title:"，则进行修改
        if second_title_pos != -1:
            # 确定修改的内容
            new_content = "Artist:"
            # 截取第一部分文本，直到第二个"Title:"
            pre_second_title = original_string[:second_title_pos]
            # 截取从第二个"Title:"之后到字符串末尾的部分
            post_second_title = original_string[second_title_pos + len("Title:"):]
            # 拼接新的字符串
            new_string = pre_second_title + new_content + post_second_title
            return new_string
        else:
            return original_string


