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

text.replace('1.0', '1.0 lineend', 'This is the first line.') # 将第一行的内容替换

text.config(state='disabled') # 禁用文本框
text.delete('1.0', 'end') # 此时不会删除内容，因为文本框被禁用
text.config(state='normal') # 恢复文本框

text.tag_add('my_tag', '1.0', '1.0 wordend') # 给第1行第1个词语添加一个看不见的标签 my_tag
text.tag_configure('my_tag', background='yellow') # 将被标签 my_tag 的内容背景改为黄色
text.tag_remove('my_tag', '1.1', '1.3') # 在标签 my_tag 中将第2和第3个字符去标签，根据上面2个操作，第1行第1个词语的第1个字符以及从第4个字符开始背景为黄色
text.tag_ranges('my_tag') # 返回标签的各个起点和终点的集合
text.tag_names() # 返回包含所有标签名的集合，其中有一个 sel 是选中的文字
text.tag_names('1.0') # 返回特殊字段所属的标签
text.replace('my_tag.first', 'my_tag.last', 'That') # 将文本中 标签 my_tag 的开头位 至 标签 my_tag 结束位 中所有文本替换位 That
text.tag_delete('my_tag') # 去除标签 my_tag

# 标注 mark 和 标签 tag 类似
text.mark_names() # 返回包含所有标注名的集合，有 insert 、 current
# insert： 插入游标的当前索引
# current： 鼠标位置下的字符索引
text.insert('insert', '_') # 在插入游标处插入 _
text.mark_set('my_mark', 'end') # 在末尾处设置标注 my_mark
text.mark_gravity('my_mark', 'right')
text.mark_unset('my_mark')

img = PhotoImage(file='D:\\Users\\Andrew\\文档\\Python\\ML-Exercises\\PlayGround\\python_logo.gif')
text.image_create('insert', image = img) # 在文本框中添加图片
button = Button(text, text='Click Me')
text.window_create('insert', window=button) # 在文本框中添加按钮

root.mainloop()