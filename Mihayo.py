import tkinter as tk
import os
from _pyrepl import commands
from email.mime import image
from PIL import Image, ImageTk
import time

time.sleep(2)

#提前配置
win_width = 1200
win_height = 678
but_width = 150
#游戏
gamecon = {
    'rj':{
        'name': 'RiddleJoker',
        'img': "D:/李空的下载/迅雷下载/rj.png",
        'path': "D:/steam/steamapps/common/Riddle Joker/RiddleJoker.exe"
    },
    'qlwh':{
        'name': '千恋万花',
        'img': "D:/李空的下载/迅雷下载/qlwh.jpg",
        'path': "D:/steam/steamapps/common/SenrenBanka/SenrenBanka.exe"
    },
    'kf':{
        'name':'星光咖啡馆与死神之蝶',
        'img': "D:/李空的下载/迅雷下载/kf.png",
        'path': "D:/steam/steamapps/common/CafeStella/CafeStella.exe"
    }

}

#证人保护计划
current_game_key = None
global_tk_image = None

#窗口

root = tk.Tk()
root.title('米哈柚启动器')
root.geometry('{}x{}'.format(win_width,win_height))
root.resizable(width=False, height=False)

showname = tk.StringVar(value='RiddleJoker')

left_frame = tk.Frame(root,width=but_width,bg = 'white')
left_frame.pack(side='left',fill='y')
left_frame.pack_propagate(False)

main_canvas = tk.Canvas(root,width=win_width - but_width,height=win_height)
main_canvas.pack(side = 'right',fill='both',expand=True)
main_canvas.create_text(
    ((win_width - but_width)/2),
    40.0,
    #textvariable = showname,
    font=('微软雅黑',20,'bold'),
    fill = 'white'
)

startbut = tk.Button(
    root,
    text = '开始游戏',
    font = ('微软雅黑',16),
    width = 12,
    height = 2,
    bg  = '#008844',
    fg = 'white',
    state = 'disabled',
    command = lambda:launch_game()
)

startbut.place(
    x = win_width - 190,
    y = win_height - 100,
)

def switch_game(game_key):
    global current_game_key, global_tk_image
    current_game_key = game_key
    info = gamecon[game_key]

    # 1. 更新界面顶部游戏名称
    showname.set(f"当前游戏：{info['name']}")

    # 2. 清空画布旧背景
    main_canvas.delete("all")

    # 3. 加载并缩放游戏专属背景图
    try:
        raw_img = Image.open(info["img"])
        # 缩放图片适配画布大小
        raw_img = raw_img.resize((win_width - but_width, win_height), Image.Resampling.LANCZOS)
        global_tk_image = ImageTk.PhotoImage(raw_img)
        # 绘制背景，左上角锚点铺满画布
        main_canvas.create_image(0, 0, anchor="nw", image=global_tk_image)
    except Exception as e:
        # 图片缺失时填充黑色背景+提示文字
        main_canvas.config(bg="#111111")
        main_canvas.create_text(
            (win_width - but_width)/2, win_height/2,
            text=f"背景图 {info['img']} 未找到", fill="red", font=("微软雅黑", 14)
        )
        print(f"图片加载失败：{e}")

    main_canvas.create_text(
        #textvariable = showname,
        (win_width - but_width) / 2, 40,

        font=("微软雅黑", 20, "bold"),
        fill="white"
    )

    startbut.config(state="normal")

def launch_game():
    if not current_game_key:
        return
    game_path = gamecon[current_game_key]["path"]
    try:
        os.startfile(game_path)
    except Exception as e:
        tk.messagebox.showerror("启动失败", f"游戏路径错误或文件不存在：\n{game_path}\n{e}")

import tkinter.messagebox as msgbox

btn_y_offset = 80
btn_height = 45
btn_gap = 15
for key, data in gamecon.items():
    game_btn = tk.Button(
        left_frame, text=data["name"], font=("微软雅黑", 12),
        width=14, height=2, bg="#336699", fg="white",
        command=lambda k=key: switch_game(k)  # lambda绑定当前游戏key
    )
    game_btn.place(x=10, y=btn_y_offset)
    btn_y_offset += btn_height + btn_gap

root.mainloop()

#ciallo~