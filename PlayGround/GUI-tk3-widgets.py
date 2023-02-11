from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root)
frm.pack()
frm.config(padding=(5, 5))

text = Text(frm, width=40, height=10)
text.pack()
text.config(wrap='word') # word / char / none

text.get('1.0', 'end') # 从第1行第0个位置开始到全文终点（包括换行）

text.get('1.0', '1.end') # 从第1行第0个位置开始到第一行终点（不包括换行）

text.insert('1.0 + 2 lines', 'Inserted message') # 在第1行第0个位置之后的2行开头位置插入消息

text.insert('1.0 + 2 lines lineend', 'and\nmore and\nmore') # 在行末插入更多消息

text.delete('1.0') # 删除第1行第0个位置的字符

text.delete('1.0', '1.0 lineend') # 删除第1行（不包括换行）

text.delete('1.0', '3.0 lineend + 1 chars') # 删除前3行，外加第3行的换行

root.mainloop()