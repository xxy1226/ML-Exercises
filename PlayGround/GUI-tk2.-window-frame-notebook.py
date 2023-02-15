from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)
frame.pack()
frame.config(height=100, width=200)
frame.config(relief=RIDGE)
root.title('tk')

ttk.Button(frame, text='Click Me').grid()
frame.config(padding=(30, 15))
ttk.LabelFrame(root, height=100, width=200, text='My Frame').pack()

window = Toplevel(root)
window.title('New Window')
# root.lower() # 放到后面
# root.lift(window)
# window.state('zoomed') # 最大化窗口
# root.state('withdrawn') # 隐藏（任务管理器也看不到）
window.state('iconic') # 最小化
# window.state('normal') # 正常化
window.iconify() # 最小化
window.deiconify() # 取消最小化

window.geometry('640x480+50+100') # 宽640，高480，左边距离50，上边距离100
window.resizable(False, False) # 宽，高

window.maxsize(640, 480) # 最大宽高
window.minsize(200, 200) # 最小宽高
window.resizable(True, True) # 允许拉伸

panedwindow = ttk.PanedWindow(window, orient=HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=True)
frame1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
frame2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)
panedwindow.add(frame1, weight=1) # 宽>0 随窗口宽度改变；0 则固定不变
panedwindow.add(frame2, weight=4)

frame3 = ttk.Frame(panedwindow, width=50, height=400, relief=SUNKEN)
panedwindow.insert(1, frame3)

# panedwindow.forget(1) # 去掉第2个框架


window1 = Toplevel(root)
window1.title('Notebook')
notebook = ttk.Notebook(window1)
notebook.pack()

def print_id():
    print(notebook.select()) # 当前页的id，好像只有Top窗口可以用
    
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)
notebook.add(frame4, text='One')
notebook.add(frame5, text='Two')
ttk.Button(frame4, text='Click Me', command=print_id).pack()
frame6 = ttk.Frame(notebook)
notebook.insert(1, frame6, text='Three') # 把这一页插入第2位置
notebook.forget(1) # 插错位置了，删掉
notebook.add(frame6, text='Three')

notebook.tab(1, state='disabled') # 禁用标签页
notebook.tab(2, state='hidden') # 隐藏标签页
notebook.tab(2, state='normal') # 正常化标签页
print(notebook.tab(1, 'text'))



# window.destroy() # 关闭窗口

root.mainloop()