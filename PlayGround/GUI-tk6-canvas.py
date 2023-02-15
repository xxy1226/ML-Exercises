from tkinter import *

root = Tk()

canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)
line = canvas.create_line(160, 360, 480, 120, fill='blue', width=5) # 画一条蓝线
canvas.itemconfigure(line, fill='green') # 将蓝线变为绿线
canvas.coords(line) # 返回线的坐标
canvas.coords(line, 0, 0, 320, 240, 640, 0) # 将线变为三个顶点的折现
canvas.itemconfigure(line, smooth=True) # 将折现变为曲线
canvas.itemconfigure(line, splinesteps=5) # 将曲线变为分成5段的折线
canvas.delete(line) # 将线删除

rect = canvas.create_rectangle(160, 120, 480, 360)
canvas.itemconfigure(rect, fill='yellow')
oval = canvas.create_oval(160, 120, 480, 360)
arc = canvas.create_arc(160, 1, 480, 240)
canvas.itemconfigure(arc, start=0, extent=180, fill='green')
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill='blue')
text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))
logo = PhotoImage(file='D:\\Users\\Andrew\\文档\\Python\\ML-Exercises\\PlayGround\\python_logo.gif')
image = canvas.create_image(320, 240, image=logo)
canvas.lift(text) # 将文字置顶
canvas.lower(image) # 将图片置底
button = Button(canvas, text='Click Me')
canvas.create_window(320, 60, window=button) # 按钮

# 使用标签
canvas.itemconfigure(rect, tag=('shape'))
canvas.itemconfigure(oval, tag=('shape', 'round'))
canvas.itemconfigure('shape', fill='grey')
canvas.gettags(oval) # 取得 oval 的标签

root.mainloop()