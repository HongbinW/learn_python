#Idea 1
"""
i = 0
while i<5:
	print("*"*(i+1))
	i +=1
"""

#Idea 2
row = 1
while row <= 5:
	col = 1
	# print("第 %d 行" % row)
	while col <= row:
		print("*", end="")	#如果不指定end，那么print函数在末尾自动加换行
		col += 1
	print("")	#在每一行末尾加换行
	row += 1
