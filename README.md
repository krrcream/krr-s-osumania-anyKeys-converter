# krr-s-osumania-anyKeys-converter

> Matrix based anyKeys-converter, Supports 4-20keys arbitrary conversion.
> 基于矩阵变换的任意keys转换器，支持4-20键转谱

## Introduce 介绍

Supports 4-20keys arbitrary conversion. If you encounter bugs, please [create an issue](https://github.com/krrcream/krr-s-osumania-anyKeys-converter/issues/new/choose) or contact me. Thank you for your support!  
支持 4-20 键任意转谱。程序可能会有 BUG，如遇到 BUG 请[提出 Issue](https://github.com/krrcream/krr-s-osumania-anyKeys-converter/issues/new/choose) 或者用下面列出联系方式联系我，感谢您的支持！

### How to use? 如何使用？

#### Windows

Download the built binary (with .exe extension) from [Google Drive](https://drive.google.com/drive/folders/15aLQ7iQLbkQ_ynVnyI92QTk3DfA7QcrP) or [Baidu Netdisk](https://pan.baidu.com/share/init?surl=VBhS-RCG402KkjoX9obQNw&pwd=kr8k) and run it.  
从[百度网盘](https://pan.baidu.com/share/init?surl=VBhS-RCG402KkjoX9obQNw&pwd=kr8k)或 [Google Drive](https://drive.google.com/drive/folders/15aLQ7iQLbkQ_ynVnyI92QTk3DfA7QcrP) 下载构建好的二进制文件（以 .exe 为后缀）后运行即可

#### MacOS & Linux

Download the project source code and go to the project root directory. After deploying the Python environment locally, and run the following commands. You can run the project from the source code.  
下载项目源码，然后进入到项目根目录。在本地部署 Python 环境后，运行以下指令。即可从源码运行此项目。

</pre> 
</details>
```bash
pip install -r requirements.txt
```

```bash
python main.py
```

#### 使用说明 Instructions

1. 填好目录，或者选择保存到原路径 
2. 把谱面文件.osu或者包含谱面的文件夹拖入到程序窗口中，程序会自动识别并转换。  
<details> 
<summary>3. V0.5版本使用案例图(case diagram)</summary> 
<pre>
E.g①:7to8
![image](https://github.com/krrcream/krr-s-osumania-anyKeys-converter/blob/main/img(External%20link%20use)/1-7to8.png)

E.g②:7to14
![image](https://github.com/krrcream/krr-s-osumania-anyKeys-converter/blob/main/img(External%20link%20use)/2%207to14k.png)

E.g②:7to10
![image](https://github.com/krrcream/krr-s-osumania-anyKeys-converter/blob/main/img(External%20link%20use)/3%207to10k.png)

E.g④:Everything to Jack And Stream(It's not much use just for fun)
![image](https://github.com/krrcream/krr-s-osumania-anyKeys-converter/blob/main/img(External%20link%20use)/4%20Everything.png)

E.g⑤:Jack World(Jack Stream trainer)
![image](https://github.com/krrcream/krr-s-osumania-anyKeys-converter/blob/main/img(External%20link%20use)/5%20Jack%20world.png)



### Other presentations about this project 此项目的其他介绍

[腾讯文档](https://docs.qq.com/aio/DUXlZS2tYdXZXdnJs?from_page=doc_home_gw_product&templateId=gqa966yujp83587sz7eth7xydc&create_type=2&aid_position=templatemall&aid_pos=templatemall&p=L9BXUFFFFgFLeFRZ5bvqs0&client_hint=0), [Document(English)](https://docs.qq.com/aio/DUXlZS2tYdXZXdnJs?from_page=doc_home_gw_product&templateId=gqa966yujp83587sz7eth7xydc&create_type=2&aid_position=templatemall&aid_pos=templatemall&p=zsy2KRXWddpeuvB4tLdjIb&client_hint=0), [Bilibili video](https://www.bilibili.com/video/BV1Tt421F7xw/)

### How to find me 如何联系我

[Bilibili](https://space.bilibili.com/), [Osu!](https://osu.ppy.sh/users/14769563)

## Getting started 开始此项目的开发

Install package.  
安装项目所需的包。

```bash
pip install -r requirements.txt
```

## Changelog 更新日志

V0.8 2024/8/18
1. 增加保存到原路径的功能，只生成新的.osu文件，不生成音频及背景文件
2. 修复一些NOTE排列的逻辑问题
1. Added the function of saving to the original path, generating only new.osu files, not audio and background files
2. Fixed some issues with note arrangement logic

V0.7 2024/8/10
1. 跳过文件出错避免崩坏
1. Skip file errors to avoid crash

V0.5 2024/5/4
1. 支持高转低，实现任意 keys 转谱
2. 增加万物化叠，万物化切，杰克世界功能
3. 增加插入空列的功能，更好地控制密度
4. 批量转谱，支持拖入多个文件以及文件夹
5. 修复 BG 和 Audio 同名错误问题
1. Support column more to column less change, to achieve any keys spectrum
2. Increase the function of [Everything to Jack] [Everything to Stream] [Jack world]
3. Increase the function of inserting empty columns to better control the density
4. Supports drag-and-drop file or folder batch converter
5. Fixed a bug with the same name for BG and Audio

V0.3 2024/5/1
1. 重写 matadata 逻辑，减少文件名 BUG。
2. 改善自动加键功能，修复加键后又出现子弹的问题。
1. Rewrite metadata logic to reduce file name bugs。
2. Improved auto-add note function, fixed an issue where new jack appeared after the notes was added.

V0.2 2024/4/20
1. 更换转换方法，增加应对删子弹时空行的自动补键策略。
2. 增加英语支持。
1. Change the conversion method and add the auto-add notes strategy to deal with the convert space rows.
2. Add English support.


