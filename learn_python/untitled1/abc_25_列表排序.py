name_list = ["zhangsan","lisi","wangwu","wangxiaoer"]
num_list = [6,8,4,1,10]
ran = ['abc','def','123',7,8,9]
#升序
# name_list.sort()	#按英文字母
# num_list.sort()
# ran.sort()	#error
# 降序
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)
#逆序
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)
print(ran)