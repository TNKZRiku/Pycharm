# 牢智决定自己搞一个能够修复op的小程序
# 乃乃花老师😭什么时候能成为像你一样优秀的人啊😭
# 来源：B站 炫彩小云雀

# 整理一下思路 tk窗口可视化交互 媒体播放器判定 屏幕监测 游戏静音 播放op 音量恢复 输入监测

# tmmk你还修不修 我这可是看在阿锦面子上才这么做的


import subprocess
import time
import pyautogui
import numpy as np
from winreg import OpenKey, QueryValueEx, HKEY_LOCAL_MACHINE
import os
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from pynput import keyboard, mouse
import tkinter as tk
from tkinter import ttk, messagebox

# 我草怎么这么多库

env_checked = False
btn_env = None
TARGET_PROCESS_NAME = "hamidashi.exe"
VIDEO_FILE = "op1.mp4"
player_process = None
global_stop_flag = False
keyboard_listener = None
mouse_listener = None


def create_main_window():
    root = tk.Tk()
    root.title("MadoSoft你就是这么对待我们正版玩家的么 我可是花了141买的😭")
    root.geometry("700x450")
    root.resizable(False, False)
    return root


def create_widgets(root):
    text_show = tk.Text(root, width=85, height=18)
    text_show.pack(pady=15, padx=10)

    fixed_content = """制作 炫彩小云雀

    首先 这个小程序只有和泉智宏能用
    进行身份认证 认证通过可以继续进行
    请将游戏调为最大化窗口化
    请确定游戏章节在“于是回到原点”
    身份认证通过后 点击取消 则会关闭小程序
    点击确定 三秒后开始运行 请在三秒内回到游戏窗口

    """
    text_show.insert(tk.END, fixed_content)
    text_show.config(state='disabled')

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    btn_test = ttk.Button(
        btn_frame,
        text="常磐！向TMMK劈下桃木剑",
        command=test_btn_func
    )
    btn_test.grid(row=0, column=0, padx=10)

    btn_check_env = ttk.Button(
        btn_frame,
        text="身份认证",
        command=check_env_btn_func
    )
    btn_check_env.grid(row=0, column=1, padx=10)

    btn_confirm = ttk.Button(
        btn_frame,
        text="取消",
        command=confirm_btn_func
    )
    btn_confirm.grid(row=0, column=2, padx=10)

    btn_cancel = ttk.Button(
        btn_frame,
        text="启动",
        command=cancel_btn_func
    )

    btn_cancel.grid(row=0, column=3, padx=10)
    return text_show

def check_env_btn_func():
    append_text(log_text, "------ 开始身份认证 ------")
    time.sleep(1)
    wmp_path = get_wmplayer_path()
    if wmp_path:
        append_text(log_text, f"认证成功 是和泉智宏本人 允许使用")
        append_text(log_text, "------ 身份验证完成 ------\n")
    else:
        append_text(log_text, "验证失败 您不是和泉智宏 无法使用")
        messagebox.showerror("身份验证失败", "你不是和泉智宏 你是谁！不允许学长以外的人接近阿锦！")
        append_text(log_text, "------ 离小天使远点！ ------\n")

def confirm_btn_func():
    append_text(log_text, '杂鱼~这就要退出了么')
    global aaa
    aaa = -1
    time.sleep(1)
    root.destroy()

def cancel_btn_func():
    append_text(log_text, '感谢支持！')
    global aaa
    aaa = 1
    time.sleep(1)
    root.destroy()

def append_text(text_widget, msg):
    text_widget.config(state=tk.NORMAL)
    text_widget.insert(tk.END, f"{msg}\n")
    text_widget.see(tk.END)
    text_widget.config(state=tk.DISABLED)
    text_widget.update()

def test_btn_func():
    append_text(log_text, "TMMK受到了高额伤害！ HP-18")

# 嘻嘻 好好玩

# tk库 我们之前考试考过 但是我正好到那一节没学到

def get_wmplayer_path() -> str | None:
    reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\wmplayer.exe"
    try:
        with OpenKey(HKEY_LOCAL_MACHINE, reg_path) as key:
            exe_path, _ = QueryValueEx(key, "")
            if os.path.isfile(exe_path):
                return exe_path
    except Exception:
        pass

    candidates = [
        r"%ProgramFiles%\Windows Media Player\wmplayer.exe",
        r"%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe"
    ]
    for raw_path in candidates:
        full_path = os.path.expandvars(raw_path)
        if os.path.isfile(full_path):
            return full_path
    # 失败
    return None
    # 朋友们 查不到的话我也没法了 本来想写个手动输入路径 但是我懒嘻嘻

def capture_monitor_area(region):
    screenshot = pyautogui.screenshot(region=region)
    gray_img = screenshot.convert("L")
    return np.array(gray_img)

def is_area_dark(gray_img, dark_threshold=250, dark_ratio=0.3):
    dark_pixel_count = np.sum(gray_img > dark_threshold)
    total_pixel = gray_img.size
    current_dark_rate = dark_pixel_count / total_pixel
    return current_dark_rate >= dark_ratio

# 好高级啊 居然可以判断画面

def rec_func():
    MONITOR_REGION = (200, 200, 600, 400)
    img_data = capture_monitor_area(MONITOR_REGION)
    h, w = img_data.shape
    print(f"截图成功，图像尺寸：宽{w} 高{h}")
    return img_data

def is_dark():
    while True:
        a = is_area_dark(rec_func())
        time.sleep(0.3)
        if a:
            return 1

def get_target_audio_state():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        proc = session.Process
        if proc is None:
            continue
        if proc.name().lower() == TARGET_PROCESS_NAME.lower():
            vol_ctrl = session._ctl.QueryInterface(ISimpleAudioVolume)
            vol = vol_ctrl.GetMasterVolume()
            mute = vol_ctrl.GetMute()
            return (vol, mute)
    return None

def set_target_mute_status(is_mute: bool):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        proc = session.Process
        if proc is None:
            continue
        if proc.name().lower() == TARGET_PROCESS_NAME.lower():
            vol_ctrl = session._ctl.QueryInterface(ISimpleAudioVolume)
            vol_ctrl.SetMute(is_mute, None)
            return True
    return False

def audio_0():
    audio_info = get_target_audio_state()
    if audio_info is not None:
        original_vol, original_mute = audio_info
        set_target_mute_status(True)

def audio_1():
    set_target_mute_status(False)

def play_fullscreen_video(wmp_exe_path):
    global player_process
    full_video_path = os.path.abspath(VIDEO_FILE)
    if not os.path.exists(full_video_path):
        return None

    try:
        args = [
            wmp_exe_path,
            full_video_path,
            "/fullscreen",
            "/play",
            "/close"
        ]
        player_process = subprocess.Popen(args)
        return player_process
    except Exception as e:
        return None

def close_video_player():
    global player_process
    if player_process is not None:
        try:
            player_process.terminate()
            player_process.wait()
        except Exception as e:
            pass
        player_process = None

def wait_video_finish():
    global player_process
    if player_process is None:
        return

    while True:
        if global_stop_flag:
            close_video_player()
            break
        ret_code = player_process.poll()
        if ret_code is not None:
            player_process = None
            break
        time.sleep(0.2)

def on_any_key_press(key):
    global global_stop_flag
    global_stop_flag = True

def on_any_mouse_click(x, y, button, pressed):
    global global_stop_flag
    if pressed:
        global_stop_flag = True

def start_input_listener():
    global keyboard_listener, mouse_listener
    keyboard_listener = keyboard.Listener(on_press=on_any_key_press)
    keyboard_listener.start()
    mouse_listener = mouse.Listener(on_click=on_any_mouse_click)
    mouse_listener.start()

def stop_input_listener():
    global keyboard_listener, mouse_listener, global_stop_flag
    if keyboard_listener is not None:
        keyboard_listener.stop()
    if mouse_listener is not None:
        mouse_listener.stop()
    global_stop_flag = False

# if __name__ == "__main__":
aaa = None
root = create_main_window()
log_text = create_widgets(root)
root.mainloop()
time.sleep(3)
aa = is_dark()
if aaa == 1:
    audio_0()
    start_input_listener()
    play_fullscreen_video(get_wmplayer_path())
    wait_video_finish()
    stop_input_listener()
    audio_1()
# 豆老师 你还没老











