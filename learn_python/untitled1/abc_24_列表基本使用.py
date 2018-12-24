name_list = ["zhangsan", "lisi", "wangwu"]

#1.取值和取索引
print(name_list[1])

#知道数据的内容，想确定数据在列表中的位置
print(name_list.index("wangwu"))	#self见之后面向对象

#2.修改
# name_list[1]= '李四'
#3.增加
name_list.append("王小二")
name_list.insert(1,"abc")
temp_list = ["123","456","lisi"]
name_list.extend(temp_list)
#4.删除
# name_list.remove("lisi")
# name_list.pop(3)
# name_list.clear()	#打印的时候只有[]
del name_list[0]	#直接从内存中删除，若要删除，尽量使用列表所提供的函数

print(name_list)
print(len(name_list))