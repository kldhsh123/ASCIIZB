# 原理简述

1. **截图**：捕获窗口或屏幕内容。
2. **灰度转换**：将图像转换为灰度，以便处理亮度。
3. **ASCII 转换**：根据亮度将灰度图像映射成字符集合，从暗到亮依次使用不同的字符。
4. **实时更新**：每 100 毫秒刷新 ASCII 图像，实现实时显示。

---

# 使用方式

1. **安装 Python 环境**  
2. **运行 `启动.bat`**  
   - 选择 `1`：安装依赖（可能需要代理）  
   - 安装成功后选择 `2`：启动  

---

# 版权声明

版权所有 © 2024 开朗的火山河123  

**许可依据**：  
本代码为自由开源项目，遵循 GPL-3.0 license 许可协议发布。您可以自由使用、修改和分发本代码，但需保留上述版权声明和许可声明。

---

# 所使用的依赖及来源

- **numpy**  
  - 来源：https://numpy.org  
  - 作用：处理图像像素数据，将图像转换为数组，便于像素值的计算与操作。

- **Pillow (PIL)**  
  - 来源：https://python-pillow.org  
  - 作用：提供屏幕截图功能（`ImageGrab`）、图像处理（灰度化、调整大小）、以及将图像嵌入 Tkinter GUI（`ImageTk`）。

- **pygetwindow**  
  - 来源：https://pypi.org/project/PyGetWindow  
  - 作用：获取当前系统中所有窗口的属性，支持定位特定窗口的边界。

- **pywin32（包含 win32gui 和 win32con 模块）**  
  - 来源：https://github.com/mhammond/pywin32  
  - 作用：用于与 Windows 图形用户界面 (GUI) 进行交互（代码中未显式使用）。

- **tkinter（Python 标准库）**  
  - 来源：https://docs.python.org/3/library/tkinter.html  
  - 作用：构建图形用户界面，用于显示捕获的屏幕截图和 ASCII 转换后的图像。

- **sys（Python 标准库）**  
  - 来源：https://docs.python.org/3/library/sys.html  
  - 作用：支持与 Python 解释器交互，用于程序退出。

---

# 许可声明

上述依赖库均遵循其各自的许可协议，具体许可条款请参阅相关库的官方文档。

---

# 免责声明

本代码按“原样”提供，无任何明示或暗示的保证，包括但不限于对适销性、特定用途适用性或不侵权的保证。  
在任何情况下，作者不对因使用本代码而导致的任何损害或损失负责。
