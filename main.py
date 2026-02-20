import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt

# ----------------- 功能函数 -----------------
def refresh_visual_trails():
    try:
        # 刷新桌面残影：重启 explorer.exe
        subprocess.run("taskkill /f /im explorer.exe", shell=True)
        subprocess.run("start explorer.exe", shell=True)
        print("桌面视觉刷新完成！")
        QMessageBox.information(window, "提示", "桌面视觉刷新完成！")
    except Exception as e:
        print(f"错误：{e}")
        QMessageBox.warning(window, "错误", f"刷新失败：{e}")

def fix_wallpaper_render():
    try:
        # 修复壁纸黑屏：刷新系统壁纸
        import ctypes
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, None, 3)
        print("壁纸渲染修复完成！")
        QMessageBox.information(window, "提示", "壁纸渲染修复完成！")
    except Exception as e:
        print(f"错误：{e}")
        QMessageBox.warning(window, "错误", f"修复壁纸失败：{e}")

def fix_icon_display():
    try:
        # 修复桌面白图标：删除图标缓存并重启 explorer
        icon_cache = os.path.expandvars(r"%localappdata%\IconCache.db")
        if os.path.exists(icon_cache):
            os.remove(icon_cache)
        subprocess.run("taskkill /f /im explorer.exe", shell=True)
        subprocess.run("start explorer.exe", shell=True)
        print("图标显示修复完成！")
        QMessageBox.information(window, "提示", "图标显示修复完成！")
    except Exception as e:
        print(f"错误：{e}")
        QMessageBox.warning(window, "错误", f"图标修复失败：{e}")

def toggle_language():
    global current_language
    current_language = 'EN' if current_language == 'CN' else 'CN'
    update_texts()

# ----------------- UI 更新 -----------------
def update_texts():
    if current_language == 'CN':
        btn_refresh.setText("桌面视觉刷新")
        btn_wallpaper.setText("壁纸渲染修复")
        btn_icon.setText("图标显示修复")
        btn_language.setText("切换到英文")
        lbl_title.setText("知枢桌面工具")
        lbl_info.setText("设计：AGRAYSON\n公司：知枢科技\n邮箱：wishubinttech@gmail.com")
    else:
        btn_refresh.setText("Refresh Visual Trails")
        btn_wallpaper.setText("Fix Wallpaper Rendering")
        btn_icon.setText("Fix Icon Display")
        btn_language.setText("Switch to Chinese")
        lbl_title.setText("WisdomHub Desktop Tool")
        lbl_info.setText("Design: AGRAYSON\nCompany: WisdomHub Intelligent Technology Co., Ltd\nEmail: wishubinttech@gmail.com")

# ----------------- 主程序 -----------------
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("WisdomHub Desktop Tool")
window.setFixedSize(400, 500)

current_language = 'CN'

# UI 元素
lbl_title = QLabel()
lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
lbl_title.setStyleSheet("font-size: 20px; font-weight: bold;")

lbl_info = QLabel()
lbl_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
lbl_info.setStyleSheet("font-size: 12px; color: gray;")

btn_refresh = QPushButton()
btn_refresh.clicked.connect(refresh_visual_trails)
btn_refresh.setFixedHeight(40)

btn_wallpaper = QPushButton()
btn_wallpaper.clicked.connect(fix_wallpaper_render)
btn_wallpaper.setFixedHeight(40)

btn_icon = QPushButton()
btn_icon.clicked.connect(fix_icon_display)
btn_icon.setFixedHeight(40)

btn_language = QPushButton()
btn_language.clicked.connect(toggle_language)
btn_language.setFixedHeight(35)

# 布局
layout = QVBoxLayout()
layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
layout.setSpacing(15)
layout.addWidget(lbl_title)
layout.addWidget(btn_refresh)
layout.addWidget(btn_wallpaper)
layout.addWidget(btn_icon)
layout.addWidget(btn_language)
layout.addWidget(lbl_info)

window.setLayout(layout)
update_texts()
window.show()
sys.exit(app.exec())