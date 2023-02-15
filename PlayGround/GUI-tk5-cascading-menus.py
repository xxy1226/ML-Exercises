from tkinter import *
root = Tk()
root.option_add('*tearOff', False)
menubar = Menu(root)
root.config(menu=menubar)
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
menubar.add_cascade(menu=file, label="File")
menubar.add_cascade(menu=edit, label="Edit")
menubar.add_cascade(menu=help_, label="Help")

file.add_command(label='New', command=lambda:print('New File'))
file.add_separator()
file.add_command(label='Open...', command=lambda: print('Opening File...'))
file.add_command(label='Save', command = lambda: print('Save File'))
file.entryconfig('New', accelerator='Ctrl + N')
logo = PhotoImage(file='D:\\Users\\Andrew\\文档\\Python\\ML-Exercises\\PlayGround\\python_logo.gif').subsample(10, 10)
file.entryconfig('Open...', image=logo, compound = 'left')
file.entryconfig('Open...', state='disabled')
file.delete('Save')
save = Menu(file)
file.add_cascade(menu=save, label="Save")
save.add_cascade(label='Save As', command=lambda:print('Saving As...'))
save.add_cascade(label='Save All', command=lambda:print('Saving All...'))

choice = IntVar()
edit.add_radiobutton(label='One', variable=choice, value=1)
edit.add_radiobutton(label='Two', variable=choice, value=2)
edit.add_radiobutton(label='Three', variable=choice, value=3)

file.post(1080, 300) # 将菜单在屏幕的指定位置上打开（仅单次）

root.mainloop()