"""
© Copyright 2024 krrcream
https://github.com/krrcream/krr-s-osumania-anyKeys-converter/
"""
# 导入布局文件
from ui import Win as MainWin
# 导入窗口控制器
from controller import Controller as MainUIController
# 将窗口控制器 传递给UI
app = MainWin(MainUIController())
if __name__ == "__main__":
    # 启动
    app.mainloop()

