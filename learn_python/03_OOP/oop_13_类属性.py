class Tool(object):

	#使用类属性，记录所有工具对象的数量
	count = 0

	def __init__(self,name):
		Tool.count += 1
		self.count = 1

tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("剪刀")

print(Tool.count)
print(tool2.count)
print(tool3.count)
