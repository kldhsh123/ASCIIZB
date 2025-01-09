import numpy as np
from PIL import ImageGrab, Image, ImageTk
import time
import os
import pygetwindow as gw
import win32gui, win32con
import sys
import tkinter as tk

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=240):  
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    scale_factor = 255 // (len(ASCII_CHARS) - 1)

    for pixel_row in pixels:
        for pixel in pixel_row:
            ascii_str += ASCII_CHARS[pixel // scale_factor]
        ascii_str += "\n"
    return ascii_str

def capture_window(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        left, top, right, bottom = window.left, window.top, window.right, window.bottom
        return ImageGrab.grab(bbox=(left, top, right, bottom))
    except IndexError:
        print(f"窗口 '{window_title}' 未找到。")
        sys.exit()

def update_display(window_title, canvas, text_label):
    if window_title:
        screen = capture_window(window_title)
    else:
        screen = ImageGrab.grab()

    tk_image = ImageTk.PhotoImage(screen)
    canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.image = tk_image  

    ascii_image = pixels_to_ascii(grayscale_image(resize_image(screen, new_width=240)))  # 宽度
    text_label.config(text=ascii_image)

    # 每100毫秒刷新一次
    text_label.after(100, update_display, window_title, canvas, text_label)

if __name__ == "__main__":
    window_title = input("请输入窗口标题（按回车键跳过以捕获全屏）：").strip()

    root = tk.Tk()
    root.title("屏幕界面ASCII字符展示")
    root.configure(bg="black")

    canvas = tk.Canvas(root, width=1200, height=800)  
    canvas.pack()

    text_label = tk.Label(root, text="", font=("Courier", 8), fg="white", bg="black", justify="left")  
    text_label.place(x=10, y=10) 

    update_display(window_title if window_title else None, canvas, text_label)

    root.mainloop()
