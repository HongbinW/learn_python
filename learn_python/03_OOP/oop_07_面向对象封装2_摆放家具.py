"""
需求：
1.房子(House)有户型、总面积和家具名称列表（新房中没有家具）
2.家具(Houseitem)有名字和占地面积，其中
席梦思(bed)占地4平米
衣柜(chest)占地2平米
餐桌(table)占地1.5平米
3.将以上三件家具添加到房子中
4.打印房子是，要求输出：户型、总面积、剩余面积、家具名称列表
"""
class HouseItem:
	def __init__(self,name,area):
		self.name = name
		self.area = area
	def __str__(self):
		return "%s 占地 %.2f平方米" %(self.name,self.area)


class House:
	def __init__(self,house_type,area):
		self.house_type = house_type
		self.area = area

		self.free_area = area	#这俩参数可内部搞定，不需要外部形参
		self.item_list = []
	def __str__(self):
		#Python 能够自动将一对括号内的代码连接在一起
		return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
				%(self.house_type,self.area,
				  self.free_area,self.item_list))
	def add_item(self,item):
		print("要添加 %s" % item)
		"""
		需求：
		1.判断家具面积是否超过剩余面积，如果超过，则提示不能添加这件家具
		2.将家具名称添加到家具名称列表中
		3.用房子剩余面积-家具面积
		"""
		if item.area > self.free_area:
			print("%s的面积太大了，无法添加"%item.name)
			return											#既然放不下了，那就不需要运行下面的代码了,return可以不返回任何东西
		self.item_list.append(item.name)
		self.free_area -= item.area

#1.创建家具
bed = HouseItem("席梦思",40)
chest = HouseItem("衣柜",21)
table = HouseItem("餐桌",1.5)
# print(bed,chest,table)

#2.创建房子对象
my_home = House("两室一厅",60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)