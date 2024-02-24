import tkinter as tk
from tkinter import filedialog
import socket


def select_folder():
    global last_selected_path
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)
    last_selected_path = folder_path


def upload_files():
    folder_path = folder_entry.get()
    ip_address = "your_target_ip"

    # 在这里实现文件上传功能，使用Socket传输文件
    # 这部分的代码需要根据具体需求和通信协议进行实现


def save_last_selected_path_to_txt():
    global last_selected_path
    with open("last_selected_path.txt", "w") as file:
        file.write(last_selected_path)
    window.destroy()  # 关闭窗口


def load_last_selected_path_from_txt() -> str:
    try:
        with open("last_selected_path.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""


# 创建GUI窗口
window = tk.Tk()
window.title("文件上传器")

# 创建Entry组件，用于显示和修改文件夹路径
folder_entry = tk.Entry(window, width=50, state="readonly")
folder_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# 创建"选择文件夹"按钮，用于选择文件夹路径
select_folder_button = tk.Button(window, text="选择", command=select_folder)
select_folder_button.grid(row=1, column=0, padx=10, pady=10)

# 创建"上传文件"按钮，用于触发文件上传动作
upload_button = tk.Button(window, text="上传", command=upload_files)
upload_button.grid(row=1, column=1, padx=10, pady=10)

# 在程序启动时尝试加载最新选择的地址
# 全局变量，用于保存最新文件夹路径
last_selected_path = load_last_selected_path_from_txt()
if last_selected_path:
    folder_entry.insert(0, last_selected_path)

# 绑定窗口关闭时的回调函数，保存最新选择的地址到txt文档中，并关闭窗口
window.protocol("WM_DELETE_WINDOW", save_last_selected_path_to_txt)

# 设置窗口不可调整大小
window.resizable(False, False)

# 进入主循环，等待用户操作
window.mainloop()
