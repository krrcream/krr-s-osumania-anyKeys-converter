import os
import threading
from pathlib import Path
from tkinter import *
from tkinterdnd2 import *  # 导入TkinterDnD2模块
import functions

audio_extensions = {'.mp3', '.wav', '.ogg'}
bg_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}
def on_drop(event):
    paths = root.splitlist(event.data)

    def process_file(file):
        try:
            #打开文件，按行读取
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                #遍历每一行，查找AudioFilename和BackgroundFilename
            for i in range(len(lines)):
                if "AudioFilename" in lines[i]:
                    #修改line[i]中的AudioFilename
                    lines[i] = "AudioFilename: " + str(entry_audio.get()) + "\n"

                if "Background and Video event" in lines[i]:  #获得背景图片路径
                    if "0,0," in lines[i + 1] and ",0,0" in lines[i + 1]:
                        lines[i + 1] = f'0,0,"{str(entry_bg.get())}",0,0\n'
                        break
            #把内容写入文件
            with open(file, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            textbox.insert(END, f"{file} 处理成功\n")

        except Exception as e:
            print("出错")
    def handle_path(path):
        path = Path(path)
        if path.exists():
            if path.is_file():
                if functions.if_osu_file(str(path)):
                    process_file(str(path))  # 直接处理文件
                # 如果文件后缀名是音频比如mp3,wav,ogg等重命名
                elif path.suffix in audio_extensions:
                    # 重命名文件
                    audio_new_name = entry_audio.get()  # 新的文件名
                    new_path = path.with_name(audio_new_name)  # 生成新的文件完整路径
                    os.rename(str(path), str(new_path))
                elif path.suffix in bg_extensions:
                    # 重命名文件
                    bg_new_name = entry_bg.get()  # 新的文件名
                    new_path = path.with_name(bg_new_name)  # 生成新的文件完整路径
                    os.rename(str(path), str(new_path))


            elif path.is_dir():
                for root_dir, dirs, files in os.walk(path):
                    root_dir = Path(root_dir)
                    for name in files:
                        file_path = root_dir / name
                        if functions.if_osu_file(str(file_path)):
                            process_file(str(file_path))  # 直接处理文件

    threading.BoundedSemaphore(value=min(len(paths), os.cpu_count() + 4, 10))
    threads = []  # 新建一个线程列表
    for path in paths:
        thread = threading.Thread(target=handle_path, args=(path,))  # 创建线程
        thread.start()  # 启动线程
        threads.append(thread)  # 添加到线程列表

# 创建主窗口
root = TkinterDnD.Tk()
root.title("文件拖放示例")
root.geometry("500x400")

# 创建标签和输入框
label_audio = Label(root, text="Audio:")
label_audio.pack(pady=5)

entry_audio = Entry(root, width=40)
entry_audio.pack(pady=5)

label_bg = Label(root, text="BG:")
label_bg.pack(pady=5)

entry_bg = Entry(root, width=40)
entry_bg.pack(pady=5)

# 创建文本框
textbox = Text(root, height=15, width=60)
textbox.pack(padx=10, pady=10)

# 注册文本框为拖放目标
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

# 运行主循环
root.mainloop()
