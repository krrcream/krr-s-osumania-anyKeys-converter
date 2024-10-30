# krr-s-osumania-anyKeys-converter

> Matrix based anyKeys-converter, Supports 4-20keys arbitrary conversion.
> 基于矩阵变换的任意keys转换器，支持4-20键转谱

## Introduce 介绍

Supports 4-20keys arbitrary conversion. If you encounter bugs, please [create an issue](https://github.com/krrcream/krr-s-osumania-anyKeys-converter/issues/new/choose) or contact me. Thank you for your support!  
支持 4-20 键任意转谱。程序可能会有 BUG，如遇到 BUG 请[提出 Issue](https://github.com/krrcream/krr-s-osumania-anyKeys-converter/issues/new/choose) 或者用下面列出联系方式联系我，感谢您的支持！

-------
### How to use? 如何使用？
Usage: Drag and drop your.osu file or folder containing.osu files into this program window to convert them all.
1. Presets: Multiple preset options are provided for quick setup. If you are not familiar with detailed settings, you can directly choose a preset to operate.
2. Upper Half of theProgram interface: 
    2.1. OD and HP settings: If you want to keep the original OD and HP values, leave them empty. If you need to modify them, enter the new values.
    2.2. Save Path: Check 'Save to Original Path' to generate new maps in the original location. If you want to store all converted maps in a folder, uncheck it and specify a new folder path.
    2.3. Seed Function: Use the same number as the seed to get the same converted result (most of the time).
3. Gale Insertion (NtoNC): 
    3.1. Conversion Speed: The larger the value, the faster the arrangement changes, and the arrangement becomes more random. The smaller the value, the less randomness.
    3.2. Target Keys: Specify the number of keys you want to generate.
    3.3. Insert blank Columns: If you feel that the density of the map is too high, you can use this to insert empty columns in the map.
    3.4. Density Adjustment: This is an experimental function that reduces the density of the map may remove some details of the original map.
    3.5. Delete generated jacks: In different arrangement changes, MiniJacks may be generated. If you want to keep these Jacks, please uncheck this option.
    3.6. Filter: This function can automatically identify and filter out the specified keys in batch processing.
4. Simple Matrix (NtoNS): Please refer to the detailed explanation in the tab.
5. Everything to Jack or Stream: These are two experimental functions, which extract the start_time of the original map and randomly generate a slice or unravel (poop).
6. Jack World: This is also an experimental function, which adds notes horizontally and vertically based on the original map, further adding jack elements (poop).

使用方法：只需将.osu文件或包含.osu文件的文件夹拖入本程序窗口，即可完成批量转谱操作
1. 预设功能：提供了多种预设选项，方便您快速上手。如果您不熟悉详细设置，可以直接选择预设进行操作
2. 程序界面上半部分：
    2.1. OD和HP设置：如果您希望保留原谱的OD（Overall Difficulty）和HP（Hurt Points）值，请留空；如需修改，请输入新的数值并保存
    2.2. 保存路径：勾选“保存到原路径”将在原谱文件所在位置生成新谱；若您希望将所有转谱文件集中存储，请取消勾选并指定新的文件夹路径
    2.3. Seed功能：使用相同的数字作为seed，将得到相同的转谱结果（大部分情况下）
3. 狂风插入：
    3.1. 转换速度：该数值越大，排列变换速度越快，排列越随机；数值越小，随机性越小
    3.2. 目标键数：指定您希望生成的键数
    3.3. 插入空列：如果您觉得谱面密度过高，可以使用此功能在谱中插入空白列
    3.4. 密度调整：这是一个试验性功能，降低密度可能会移除原谱的一些细节
    3.5. Jack处理：在不同排列变换过程中可能会生成MiniJack，如果您希望保留这些Jack，请取消勾选
    3.6. 筛选器：在批量处理文件时，此功能可以自动识别并筛选出您指定的键数
4. 简单矩阵：请查看选项卡中的详细说明
5. 万物化叠和万物化切：这是两个试验性功能，它们会取原谱的start_time，并随机生成切或叠（大便）
6. 杰克世界：这也是一个试验性功能，它在原谱的基础上，通过横向和纵向增加note，进一步加入jack元素（大便）
#### Windows

Download the built binary (with .exe extension) from [Google Drive](https://drive.google.com/drive/folders/15aLQ7iQLbkQ_ynVnyI92QTk3DfA7QcrP) or [Baidu Netdisk](https://pan.baidu.com/share/init?surl=VBhS-RCG402KkjoX9obQNw&pwd=kr8k) and run it.  
从[百度网盘](https://pan.baidu.com/share/init?surl=VBhS-RCG402KkjoX9obQNw&pwd=kr8k)或 [Google Drive](https://drive.google.com/drive/folders/15aLQ7iQLbkQ_ynVnyI92QTk3DfA7QcrP) 下载构建好的二进制文件（以 .exe 为后缀）后运行即可

#### MacOS & Linux

Download the project source code and go to the project root directory. After deploying the Python environment locally, and run the following commands. You can run the project from the source code.  
下载项目源码，然后进入到项目根目录。在本地部署 Python 环境后，运行以下指令。即可从源码运行此项目。

```bash
pip install -r requirements.txt
```

```bash
python main.py
```

-------
### Other presentations about this project 此项目的其他介绍

[腾讯文档（旧的）](https://docs.qq.com/aio/DUXlZS2tYdXZXdnJs?from_page=doc_home_gw_product&templateId=gqa966yujp83587sz7eth7xydc&create_type=2&aid_position=templatemall&aid_pos=templatemall&p=L9BXUFFFFgFLeFRZ5bvqs0&client_hint=0), [Document(Old)](https://docs.qq.com/aio/DUXlZS2tYdXZXdnJs?from_page=doc_home_gw_product&templateId=gqa966yujp83587sz7eth7xydc&create_type=2&aid_position=templatemall&aid_pos=templatemall&p=zsy2KRXWddpeuvB4tLdjIb&client_hint=0), [Bilibili video(Old)](https://www.bilibili.com/video/BV1Tt421F7xw/)

-------
### How to find me 如何联系我

[Bilibili](https://space.bilibili.com/), [Osu!](https://osu.ppy.sh/users/14769563)

-------
## Changelog 更新日志
V1.0.0 2024/10/30
1. Rewritten the window using TK in version 1.0.0, optimized the code, and added preset methods so that even those who are not familiar with the setup can easily get started.
-------
1. V1.0.0 用TK重新写了窗口，对代码进行优化，增加了预设方法，不会设置的人也可以直接上手。


V0.90 2024/9/18
1. 更新种子功能，使用相同的种子值进行多次谱面转换，将确保每次得到的谱面结果保持一致性。
-------
1. Update the seed feature, using the same seed value for multiple beatmap conversions ensures that the resulting beatmaps are consistent each time.

-------
V0.81 2024/8/18
1. 修复了一些[HitObjects]格式问题，使程序能正确处理一些特殊的谱面(其他转谱器的铺面)。
-------
1. Fixed some [HitObjects] formatting issues, allowing the program to correctly handle some special beatmap files(other converter's layout).
<details> 
<summary>像这些(like this):</summary> 
<pre>
 "192,192,9974,1,0"
 " "
 "100,100,12600,6,1,B|200:200|250:200|250:200|300:150,2,310.123,2|1|2,0:0|0:0|0:2,0:0:0:0:"
 "155.60000000000002,192,17423,128,0,17659:0:0:0:0:"
</pre> 
</details>

-------
V0.8 2024/8/18
1. 增加保存到原路径的功能，只生成新的.osu文件，不生成音频及背景文件
2. 修复一些NOTE排列的逻辑问题
3. 修复因为文件名等程序崩溃的问题
-------
1. Added the function of saving to the original path, generating only new.osu files, not audio and background files
2. Fixed some issues with note arrangement logic
3. Fixed the issue where the program would crash due to problems with filenames

-------
V0.7 2024/8/10
1. 一些格式不正确的[metadata]和一些格式不正确的[HitObjects] ，它们与当前的官方.osu文件格式不匹配会导致程序崩溃。唯一的解决办法就是在游戏中重新保存文件格式。我实现了一个功能，跳过无法解决的错误，以避免崩溃
-------
1. Some incorrectly formatted [metadata] and some incorrectly formatted notes , which don't match the current official .osu file format,will cause the program crash. The only solution for this is to refresh the file format by resaving it in the game. I implemented a feature that skip the unsolvable errors to avoid crash

-------
V0.5 2024/5/4
1. 支持高转低，实现任意 keys 转谱
2. 增加万物化叠，万物化切，杰克世界功能
3. 增加插入空列的功能，更好地控制密度
4. 批量转谱，支持拖入多个文件以及文件夹
5. 修复 BG 和 Audio 同名错误问题
-------
1. Support column more to column less change, to achieve any keys spectrum
2. Increase the function of [Everything to Jack] [Everything to Stream] [Jack world]
3. Increase the function of inserting empty columns to better control the density
4. Supports drag-and-drop file or folder batch converter
5. Fixed a bug with the same name for BG and Audio
-------
V0.3 2024/5/1
1. 重写 matadata 逻辑，减少文件名 BUG。
2. 改善自动加键功能，修复加键后又出现子弹的问题。
-------
1. Rewrite metadata logic to reduce file name bugs。
2. Improved auto-add note function, fixed an issue where new jack appeared after the notes was added.

-------
V0.2 2024/4/20
1. 更换转换方法，增加应对删子弹时空行的自动补键策略。
2. 增加英语支持。
-------
1. Change the conversion method and add the auto-add notes strategy to deal with the convert space rows.
2. Add English support.


