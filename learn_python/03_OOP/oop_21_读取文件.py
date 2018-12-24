#1.打开文件
file = open("C:\\Users\\whb\\Desktop\\新建文本文档.txt")

#2.读取文件内容
text = file.read()
print(text)
#3.关闭文件
file.close()
