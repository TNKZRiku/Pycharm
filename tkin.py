import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_name.get()
    password = entry_pwd.get()
    if username == "大一学生" and password == "123456":
        messagebox.showinfo("提示", "欢迎进入")
    else:
        messagebox.showerror("错误", "用户名和密码错误")

def reset():
    entry_name.delete(0, tk.END)
    entry_pwd.delete(0, tk.END)

def exit_window():
    root.destroy()

# 主窗口
root = tk.Tk()
root.title("用户登录")
root.geometry("320x220")

# 姓名
label_name = tk.Label(root, text="姓名：")
label_name.place(x=80, y=40)
entry_name = tk.Entry(root)
entry_name.place(x=140, y=40, width=120)

# 密码
label_pwd = tk.Label(root, text="密码：")
label_pwd.place(x=80, y=80)
entry_pwd = tk.Entry(root, show="*")  
entry_pwd.place(x=140, y=80, width=120)

btn_login = tk.Button(root, text="登录", command=login)
btn_login.place(x=60, y=130, width=70)

btn_reset = tk.Button(root, text="重置", command=reset)
btn_reset.place(x=135, y=130, width=70)

btn_exit = tk.Button(root, text="退出", command=exit_window)
btn_exit.place(x=210, y=130, width=70)

root.mainloop()