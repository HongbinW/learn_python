class A:

	def __init__(self):
		self.num1 = 100
		self.__num2 = 200

	def __test(self):
		print("私有方法 %d %d"%(self.num1,self.__num2))
	def test(self):
		print("私有方法 %d %d"%(self.num1,self.__num2))
		self.__test()
class B(A):
	def demo(self):
		#1.子类不能访问父类私有属性
		#2.子类访问父类私有方法
		print("")



b = B()
print(b)
b.test()
#在外界不能直接访问对象的私有属性或调用私有方法
# print(b.__num2)
# b.__test