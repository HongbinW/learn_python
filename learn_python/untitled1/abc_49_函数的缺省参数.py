# gl_list = [6,3,9]
#
# #gl_list.sort()		#默认升序排序
# gl_list.sort(reverse=True)
#
# print(gl_list)

def print_info(name ,gender=True):
	"""

	:param name: 班上同学的姓名
	:param gender: True 男生 False 女生
	"""
	gender_text = "男生"
	if not gender:
		gender_text = "女生"

	print("%s 是 %s"%(name,gender_text))

print_info("小明",False)