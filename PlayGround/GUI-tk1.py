from tkinter import *
from tkinter import ttk

class HelloApp:
    def __init__(self, master):
        self.label = ttk.Label(master, text="你好, 安德烈")
        self.label.grid(row=0, column=0, columnspan=3)
        
        self.bt1 = ttk.Button(master, text="中文", command=self.chinese_hello)
        self.bt1.grid(row=1, column=0)
        self.bt2 = ttk.Button(master, text="English", command=self.english_hello)
        self.bt2.grid(row=1, column=1)
        self.bt3 = ttk.Button(master, text="Русский", command=self.russian_hello)
        self.bt3.grid(row=1, column=2)
        
        self.longlabel = ttk.Label(master, text="你好安德烈，我们上次见面已经有一段时间了。 很高兴再次见到你！")
        self.longlabel.grid(row=2, column=0, columnspan=3)
        self.longlabel.config(wraplength=150)
        self.longlabel.config(justify=CENTER)
        self.longlabel.config(foreground='blue', background='yellow')
        self.longlabel.config(font=('Courier', 12, 'bold'))
        
    def chinese_hello(self):
        self.label.config(text="你好，安德烈")
        self.longlabel.config(text="你好安德烈，我们上次见面已经有一段时间了。 很高兴再次见到你！")

    def english_hello(self):
        self.label.config(text="Hello, Andrew")
        self.longlabel.config(text="Hello Andrew, It's been a while since we last met. Great to see you again!")
        
    def russian_hello(self):
        self.label.config(text='Привет, Андре')
        self.longlabel.config(text="Привет Андре, Прошло много времени с тех пор, как мы в последний раз встречались. Здорово видеть вас снова!")
        

if __name__ == '__main__':
    root = Tk()
    
    # 使用类
    app = HelloApp(root)
    
    # 图片（+文字）    
    # cadog = PhotoImage(file='DALLE1.png')
    # logo = PhotoImage(file='python_logo.gif')
    # small_logo = logo.subsample(5, 5)
    
    img = ttk.Label(root, text='cadog')
    # img.grid(row=3, column=0, columnspan=2)
    # img.config(image=logo)
    img.config(compound='text')
    img.config(compound='center')
    img.config(compound='left')
    
    # 按钮功能
    btn1 = ttk.Button(root, text='Click Me')
    btn1.grid(row=4, column=0)
    def btn1callback():
        print('Clicked!')
    btn1.config(command=btn1callback)
    # btn1.config(image=small_logo, compound=LEFT)
    btn1.invoke()
    
    # 灰按钮
    btn2 = ttk.Button(root, text='Click Me')
    btn2.grid(row=4, column=2)
    btn2.config(command=btn1callback)
    # btn2.config(image=small_logo, compound=LEFT)
    btn2.state(['disabled'])
    
    # 勾选按钮
    checkbutton = ttk.Checkbutton(root, text="打包")
    checkbutton.grid(row=5, column=1)
    spam = StringVar()
    spam.set('打包')
    checkbutton.config(variable=spam, onvalue='打包', offvalue='堂食')
    
    # 选择按钮
    breakfast = StringVar()
    breakfast.set('餐具')
    rbtn1 = ttk.Radiobutton(root, text='鸡蛋培根', variable=breakfast, value='刀叉')
    rbtn1.grid(row=6, column=0)
    rbtn2 = ttk.Radiobutton(root, text='豆浆油条', variable=breakfast, value='碗筷')
    rbtn2.grid(row=6, column=1)
    rlabel = ttk.Checkbutton(root, textvariable=breakfast)
    rlabel.grid(row=6, column=2)
    
    # 文本框
    note_label = ttk.Label(root, text="备注")
    note_label.grid(row=7, column=0)
    entry = ttk.Entry(root, width = 50)
    entry.grid(row=8, column=0, columnspan=3)
    entry.delete(0, END) # 用于删除文字内容
    # entry.config(show='*') # 用于遮挡密码
    # entry.state(['readonly']) # 只读，不可更改
    
    # 下拉框
    month = StringVar()
    combobox = ttk.Combobox(root, textvariable=month)
    combobox.grid(row=9, column=1)
    combobox.config(values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    year = StringVar()
    spinbox = ttk.Spinbox(root, from_=1990, to=2023, textvariable=year)
    spinbox.grid(row=10, column=1)
    
    progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
    progressbar.grid(row=10, column=0, columnspan=3)
    # progressbar.config(mode='indeterminate') # 进度条来回移动模式
    progressbar.start()
    progressbar.stop() 
    progressbar.config(maximum=11.0, value=1.0)
    progressbar.config(value=6.0)
    progressbar.step()
    progressbar.step(5)
    pro_value = DoubleVar()
    progressbar.config(variable=pro_value)
    
    # 拖动条
    scale = ttk.Scale(root, orient=HORIZONTAL, length=400, variable=pro_value, from_ = 0.0, to= 11.0)
    scale.grid(row=11, column=0, columnspan=3)
    scale.set(9.9)
    
    
    root.mainloop()

# ttk.Button.config 包含：
# {
    # 'command': (
        # 'command', 
        # 'command', 
        # 'Command', 
        # '', 
        # ''
    # ), 
    # 'default': (
        # 'default', 
        # 'default', 
        # 'Default', 
        # <string object: 'normal'>, 
        # <string object: 'normal'>
    # ), 
    # 'takefocus': (
        # 'takefocus', 
        # 'takeFocus',
        # 'TakeFocus',
        # 'ttk::takefocus',
        # 'ttk::takefocus'
    # ),
    # 'text': (
        # 'text',
        # 'text',
        # 'Text', 
        # '',
        # 'abc'
    # ), 
    # 'textvariable': (
        # 'textvariable',
        # 'textVariable', 
        # 'Variable', 
        # '', 
        # ''
    # ), 
    # 'underline': (
        # 'underline',
        # 'underline',
        # 'Underline', 
        # -1, 
        # -1
    # ), 
    # 'width': (
        # 'width',
        # 'width',
        # 'Width',
        # '',
        # ''
    # ),
    # 'image': (
        # 'image',
        # 'image',
        # 'Image', 
        # '',
        # ''
    # ), 
    # 'compound': (
        # 'compound',
        # 'compound',
        # 'Compound',
        # '',
        # ''
    # ), 
    # 'padding': (
        # 'padding',
        # 'padding',
        # 'Pad', 
        # '',
        # ''
    # ), 
    # 'state': (
        # 'state', 
        # 'state',
        # 'State', 
        # <string object: 'normal'>,
        # <string object: 'normal'>
    # ),
    # 'cursor': (
        # 'cursor',
        # 'cursor',
        # 'Cursor',
        # '',
        # ''
    # ),
    # 'style': (
        # 'style',
        # 'style',
        # 'Style', 
        # '',
        # ''
    # ), 
    # 'class': (
        # 'class',
        # '',
        # '',
        # '',
        # ''
    # )
# }