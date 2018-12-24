#1.
file_read = open("readme.txt")
file_write = open("readme[复件].txt",'w')
"""方法1
text = file_read.read()
file_write.write(text)
"""
#方法2
while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()