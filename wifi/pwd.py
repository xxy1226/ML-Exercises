import itertools as its

words = "1234567890"
r = its.product(words, repeat=5)

# 保存在文件中
with open("pass", "a") as dic:
    for i in r:
        dic.write("".join(i))
        dic.write("".join("\n"))