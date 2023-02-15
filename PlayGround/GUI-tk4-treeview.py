from tkinter import *
from tkinter import ttk
root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()
treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', 'end', 'item3', text='Third Item')
logo = PhotoImage(file='D:\\Users\\Andrew\\文档\\Python\\ML-Exercises\\PlayGround\\python_logo.gif').subsample(10, 10)
treeview.insert('item2', 'end', 'python', text='Python', image=logo) # 在 item2 下增加子条目 Python 机器图标
treeview.config(height=5)

treeview.move('item2', 'item1', 'end') # 将 item2 移成 item1 的子条目
treeview.item('item1', open=True) # 将 item1 展开
treeview.item('item1', 'open') # 同上

treeview.detach('item3') # 从树中移除 item3，但 item3 仍然保留在内存里
treeview.move('item3', 'item2', '0') # 将内存中的 item3 移成 item2 的第一个子条目
treeview.delete('item3') # 彻底删除 item3

treeview.config(columns=('version')) # 设置列 version
treeview.column('version', width=50, anchor='center') # 将列 version 的宽度设为50， 内容居中
treeview.column('#0', width=150) # 将第一列的宽度设为150像素
treeview.heading('version', text='Version') # 将列 version 的文字名称设为 Version
treeview.set('python', 'version', '3.10.4') # 将行 python 的 version 值设为 3.10.4

treeview.item('python', tags=('software')) # 给 python 添加标签 software
treeview.tag_configure('software', background='yellow') # 将标签为 software 的行背景设为 yellow

def callback(event):
    print(treeview.selection()) # 打印选中选项的集合（可多选）

treeview.bind('<<TreeviewSelect>>', callback)

treeview.config(selectmode='browse') # 单选
treeview.config(selectmode='none') # 无法选择
treeview.config(selectmode='extended') # 多选

treeview.selection_add('python') # 将 python 设为选中
treeview.selection_remove('python') # 将 python 设为未选中
treeview.selection_toggle()





root.mainloop()